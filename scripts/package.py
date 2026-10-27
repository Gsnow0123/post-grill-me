#!/usr/bin/env python3
"""Build one deterministic, standalone ZIP per instruction language."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path

from validate import ROOT, SKILLS, validate_repo


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-z0-9.]+)?", args.version):
        parser.error("use a semantic version such as 0.1.0")
    issues = validate_repo()
    if issues:
        print("\n".join(issues))
        return 1
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    checksums = []
    for name in SKILLS:
        source = ROOT / "skills" / name
        archive = output / f"{name}-{args.version}.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as package:
            for path in sorted(source.rglob("*")):
                if not path.is_file():
                    continue
                member = f"{name}/{path.relative_to(source).as_posix()}"
                info = zipfile.ZipInfo(member, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                package.writestr(info, path.read_bytes())
        checksums.append(f"{hashlib.sha256(archive.read_bytes()).hexdigest()}  {archive.name}")
        print(archive.name)
    (output / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
