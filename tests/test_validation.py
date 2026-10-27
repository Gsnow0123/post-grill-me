"""Exercise concrete publication failures; no agent/model calls are made."""

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import check_archive, link_issues, publication_issues


class PublicationTests(unittest.TestCase):
    def test_private_path_is_rejected(self):
        example = "C:" + "/" + "/".join(("Users", "someone", "notes.md"))
        self.assertIn("machine-specific Windows path", publication_issues(example))
        self.assertFalse(publication_issues("docs/feature-recaps"))

    def test_token_like_value_is_rejected(self):
        self.assertIn("token-like string", publication_issues("ghp_" + "a" * 36))
        self.assertFalse(publication_issues("Use your host's existing authentication."))

    def test_local_links_must_exist_and_stay_in_repo(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            page = root / "README.md"
            (root / "guide.md").write_text("guide", encoding="utf-8")
            self.assertFalse(link_issues(page, "[guide](guide.md)", root))
            self.assertTrue(link_issues(page, "[missing](missing.md)", root))
            self.assertTrue(link_issues(page, "[outside](../outside.md)", root))

    def test_release_cannot_include_extra_or_modified_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            skill = root / "example-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_bytes(b"instructions\n")
            archive = root / "skill.zip"
            with zipfile.ZipFile(archive, "w") as package:
                package.writestr("example-skill/SKILL.md", b"instructions\n")
            self.assertFalse(check_archive(archive, skill))
            with zipfile.ZipFile(archive, "w") as package:
                package.writestr("example-skill/SKILL.md", b"changed\n")
                package.writestr("example-skill/private-notes.md", b"unexpected")
            issues = check_archive(archive, skill)
            self.assertEqual(len(issues), 2)


if __name__ == "__main__":
    unittest.main()
