#!/usr/bin/env python3
"""Offline package/link/publication checks. This does not evaluate model behavior."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("post-grill-me", "post-grill-me-zh")
IGNORED_PARTS = {".git", "dist", "__pycache__", ".cache"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yml", ".yaml", ".svg", ".txt"}


def publication_issues(text: str) -> list[str]:
    """Flag concrete machine paths and token-like strings, not all possible secrets."""
    rules = {
        "machine-specific Windows path": r"\b[A-Za-z]:[\\/](?:Users|Workspace)[\\/]",
        "machine-specific home path": r"/(?:Users|home)/[A-Za-z0-9_.-]+/",
        "token-like string": r"\b(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{30,})\b",
        "internal network address": r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b",
    }
    return [label for label, pattern in rules.items() if re.search(pattern, text)]


def link_issues(path: Path, text: str, root: Path) -> list[str]:
    issues = []
    for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
        target = target.strip("<>")
        if target.startswith("#") or urlsplit(target).scheme:
            continue
        relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
        resolved = (path.parent / relative).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            issues.append(f"local link escapes repository: {target}")
            continue
        if not resolved.exists():
            issues.append(f"missing local link: {target}")
    return issues


def check_archive(archive: Path, skill_root: Path) -> list[str]:
    """Require exactly the installable files and bytes from the selected skill."""
    prefix = skill_root.name
    expected = {
        f"{prefix}/{p.relative_to(skill_root).as_posix()}": p.read_bytes()
        for p in skill_root.rglob("*")
        if p.is_file()
    }
    issues = []
    try:
        with zipfile.ZipFile(archive) as package:
            names = package.namelist()
            if len(names) != len(set(names)) or set(names) != set(expected):
                issues.append("archive file set differs from the standalone skill")
            for name in names:
                if name in expected and package.read(name) != expected[name]:
                    issues.append(f"archive content differs: {name}")
    except (OSError, zipfile.BadZipFile) as exc:
        issues.append(str(exc))
    return issues


def validate_repo(root: Path = ROOT) -> list[str]:
    issues = []
    required = ["README.md", "README.zh-CN.md", "LICENSE", "CHANGELOG.md", "evals/cases.json"]
    for relative in required:
        if not (root / relative).is_file():
            issues.append(f"missing required file: {relative}")
    for name in SKILLS:
        skill_root = root / "skills" / name
        for relative in ("SKILL.md", "LICENSE", "references/recap.md", "references/hosts.md", "agents/openai.yaml"):
            if not (skill_root / relative).is_file():
                issues.append(f"{name}: missing {relative}")
        entry = skill_root / "SKILL.md"
        if not entry.exists():
            continue
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            issues.append(f"{name}: missing frontmatter")
            continue
        # The package intentionally uses simple one-line scalar fields.
        fields = dict(re.findall(r"^([a-z-]+): (.+)$", match.group(1), re.M))
        if fields.get("name") != name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            issues.append(f"{name}: invalid or mismatched skill name")
        if not 1 <= len(fields.get("description", "")) <= 1024:
            issues.append(f"{name}: invalid description")
        if fields.get("license") != "MIT":
            issues.append(f"{name}: expected MIT license")
        if (skill_root / "LICENSE").is_file() and (skill_root / "LICENSE").read_bytes() != (root / "LICENSE").read_bytes():
            issues.append(f"{name}: bundled license differs")
        metadata = (skill_root / "agents/openai.yaml").read_text(encoding="utf-8")
        short = re.search(r'^  short_description: "(.+)"$', metadata, re.M)
        if not short or not 25 <= len(short.group(1)) <= 64:
            issues.append(f"{name}: UI description must be 25–64 characters")
        if f"${name}" not in metadata:
            issues.append(f"{name}: default prompt must mention its invocation")
    for path in root.rglob("*"):
        if not path.is_file() or any(part in IGNORED_PARTS for part in path.relative_to(root).parts):
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name not in {"LICENSE", ".gitignore", ".gitattributes"}:
            continue
        text = path.read_text(encoding="utf-8")
        label = path.relative_to(root).as_posix()
        issues.extend(f"{label}: {issue}" for issue in publication_issues(text))
        if path.suffix == ".md":
            issues.extend(f"{label}: {issue}" for issue in link_issues(path, text, root))
        if path.suffix == ".json":
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                issues.append(f"{label}: invalid JSON: {exc}")
        if path.suffix == ".svg":
            try:
                tree = ET.fromstring(text)
                if any(node.tag.rsplit("}", 1)[-1] in {"script", "foreignObject"} for node in tree.iter()):
                    issues.append(f"{label}: SVG contains active/embedded content")
            except ET.ParseError as exc:
                issues.append(f"{label}: invalid SVG: {exc}")
    cases_path = root / "evals/cases.json"
    if cases_path.exists():
        cases = json.loads(cases_path.read_text(encoding="utf-8"))
        ids = [case.get("id") for case in cases]
        if len(ids) != len(set(ids)) or len(ids) < 6:
            issues.append("manual cases need unique IDs and coverage of core branches")
        for case in cases:
            if not all(case.get(key) for key in ("id", "context", "request", "expected", "must_not")):
                issues.append(f"incomplete manual case: {case.get('id')}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archives", type=Path, help="also validate release ZIPs and checksums in this directory")
    args = parser.parse_args()
    issues = validate_repo()
    if args.archives:
        folder = args.archives.resolve()
        archives = sorted(folder.glob("*.zip"))
        if len(archives) != len(SKILLS):
            issues.append("expected one release ZIP per language")
        for archive in archives:
            name = "post-grill-me-zh" if archive.name.startswith("post-grill-me-zh-") else "post-grill-me"
            issues.extend(f"{archive.name}: {issue}" for issue in check_archive(archive, ROOT / "skills" / name))
        sums = folder / "SHA256SUMS"
        if not sums.is_file():
            issues.append("missing release SHA256SUMS")
        else:
            expected = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in archives}
            recorded = {}
            for line in sums.read_text(encoding="utf-8").splitlines():
                digest, name = line.split("  ", 1)
                recorded[name] = digest
            if recorded != expected:
                issues.append("release checksums do not match the ZIPs")
    if issues:
        print("\n".join(f"ERROR: {issue}" for issue in issues))
        return 1
    print("Package, metadata, local-link, and publication checks passed.")
    if args.archives:
        print("Standalone release contents and SHA256 checksums passed.")
    print("These checks do not measure model behavior.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
