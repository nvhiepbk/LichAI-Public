#!/usr/bin/env python3
"""Restore missing fixed-name installers from successful GitHub Actions runs."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

PUBLIC_REPO = "nvhiepbk/LichAI-Public"
TAG = "LichAI-Public"
OUT = Path("recovered-assets")
# Only installers. Do not publish AABs, debug symbols, or JSON metadata as release assets.
SOURCES = [
    ("LichAI-Android", "LichAI-Android-Release-APK", {"LichAI.Android.apk": "app-release.apk"}),
    ("LichAI-TV", "LichAI-TV-01-APK", {"LichAI.TV.apk": "app-release.apk"}),
    ("LichAI-Desktop", "LichAI-Desktop-Windows", {
        "LichAI.Desktop.exe": "*.exe", "LichAI.Desktop.msi": "*.msi"}),
    ("LichAI-Translator", "LichAI-Excel-Translater-Windows-x64", {
        "LichAI-Excel-Translater.exe": "LichAI-Excel-Translater.exe"}),
    ("LichAI-Translator", "LichAI-Word-Translator-Windows-x64", {
        "LichAI-Word-Translator.exe": "LichAI-Word-Translator.exe"}),
    ("LichAI-Studio", "windows-release-candidate", {
        "LichAI-Studio-Windows.exe": "LichAI-Studio-Windows.exe"}),
    ("LichAI-Studio", "android-release-candidate", {
        "LichAI-Studio-Android.apk": "LichAI-Studio-Android.apk"}),
]

def gh(*args):
    p = subprocess.run(["gh", *args], capture_output=True, text=True)
    if p.returncode:
        detail = p.stderr.strip() or p.stdout.strip()
        raise RuntimeError(f"GitHub API/CLI error: {detail}")
    return p.stdout

def api(endpoint):
    return json.loads(gh("api", endpoint))

def current_assets():
    release = api(f"repos/{PUBLIC_REPO}/releases/tags/{TAG}")
    return {a["name"] for a in release["assets"]}

def find_run(repo, artifact_name):
    # Successful runs only. Search the most recent 100 and require a nonexpired artifact.
    runs = api(f"repos/nvhiepbk/{repo}/actions/runs?status=success&per_page=100")["workflow_runs"]
    for run in runs:
        artifacts = api(f"repos/nvhiepbk/{repo}/actions/runs/{run['id']}/artifacts?per_page=100")["artifacts"]
        if any(a["name"] == artifact_name and not a["expired"] for a in artifacts):
            return run["id"]
    raise RuntimeError(f"No successful run with available artifact {repo}/{artifact_name}")

def recover(repo, artifact_name, mapping, missing, expected_hashes):
    selected = {name: pattern for name, pattern in mapping.items() if name in missing}
    if not selected:
        return
    run_id = find_run(repo, artifact_name)
    folder = OUT / f"{repo}-{artifact_name}"
    folder.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {repo} run {run_id}: {artifact_name}", flush=True)
    subprocess.run(["gh", "run", "download", str(run_id), "-R", f"nvhiepbk/{repo}",
                    "-n", artifact_name, "-D", str(folder)], check=True)
    for target, pattern in selected.items():
        matches = [p for p in folder.rglob(pattern) if p.is_file()]
        if len(matches) != 1:
            raise RuntimeError(f"Expected exactly one {pattern} in {folder}, got {len(matches)}")
        destination = OUT / target
        shutil.copy2(matches[0], destination)
        if destination.stat().st_size == 0:
            raise RuntimeError(f"Empty installer: {target}")
        if target in expected_hashes:
            actual = hashlib.sha256(destination.read_bytes()).hexdigest()
            if actual.lower() != expected_hashes[target].lower():
                raise RuntimeError(f"SHA-256 mismatch for {target}; refusing to publish")
        print(f"Recovered {target} ({destination.stat().st_size} bytes)", flush=True)

def main():
    OUT.mkdir(exist_ok=True)
    existing = current_assets()
    wanted = {name for _, _, mapping in SOURCES for name in mapping}
    missing = wanted - existing
    print("Missing:", ", ".join(sorted(missing)) or "none", flush=True)
    if not missing:
        return
    metadata = json.loads(Path("apps/studio.json").read_text(encoding="utf-8"))
    expected_hashes = {
        metadata[platform]["asset"]: metadata[platform]["sha256"]
        for platform in ("windows", "android")
    }
    for repo, artifact, mapping in SOURCES:
        recover(repo, artifact, mapping, missing, expected_hashes)
    uploads = [str(OUT / name) for name in sorted(missing)]
    subprocess.run(["gh", "release", "upload", TAG, "--repo", PUBLIC_REPO,
                    "--clobber", *uploads], check=True)
    after = current_assets()
    if wanted - after:
        raise RuntimeError(f"Still missing release assets: {sorted(wanted - after)}")
    print("All eight fixed download filenames are present.", flush=True)

if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
