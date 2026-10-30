"""Offline checks for the standalone Claude and portable plugin."""
import json
import os
import struct
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = "finos-reference-tools"
PACKAGES = {f"finos-{c}": f"finos-mcp-{c}" for c in ("aigf", "cdm", "fdc3")}

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    native = load(".claude-plugin/plugin.json")
    portable = load("plugin.json")
    assert native["name"] == portable["name"] == NAME
    assert native["version"] == portable["version"] == "0.2.1"
    market = load(".claude-plugin/marketplace.json")
    assert market["plugins"][0]["name"] == NAME
    assert market["plugins"][0]["source"] == "./"
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())
    assert set(project["project"]["dependencies"]) == {f"{p}==0.3.2" for p in PACKAGES.values()}
    assert "sources" not in project.get("tool", {}).get("uv", {})
    assert "index" not in project.get("tool", {}).get("uv", {})
    lock = tomllib.loads((ROOT / "uv.lock").read_text())
    for pkg in lock["package"]:
        if pkg["name"] == project["project"]["name"]:
            continue
        assert pkg["source"] == {"registry": "https://pypi.org/simple"}
        artifacts = pkg.get("wheels", []) + ([pkg["sdist"]] if "sdist" in pkg else [])
        assert artifacts and all(a["hash"].startswith("sha256:") for a in artifacts)
    for manifest, root in ((".mcp.json", "${CLAUDE_PLUGIN_ROOT}"), ("mcp.json", "${PLUGIN_ROOT}")):
        servers = load(manifest)["mcpServers"]
        assert set(servers) == set(PACKAGES)
        for key, server in servers.items():
            comp = key.removeprefix("finos-")
            expected = {"command": "uv", "args": ["run", "--frozen", "--directory", root, "python", root + "/servers/" + comp + ".py"]}
            if manifest == "mcp.json":
                expected["type"] = "stdio"
            assert server == expected
            assert (ROOT / "servers" / (comp + ".py")).is_file()
            assert (ROOT / "skills" / key / "SKILL.md").is_file()
    files = []
    for directory, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", ".venv", "__pycache__")]
        files.extend(Path(directory) / name for name in names)
    assert len(files) <= 512
    assert all(f.stat().st_size < 256 * 1024 for f in files)
    icon = (ROOT / ".claude-plugin/icon.png").read_bytes()
    assert icon[:8] == b"\x89PNG\r\n\x1a\n"
    width, height = struct.unpack(">II", icon[16:24])
    assert width == height and 512 <= width <= 2048 and len(icon) < 2 * 1024 * 1024
    print(f"PASS: {len(files)} plugin files, public-PyPI lock, manifests, skills and icon")

if __name__ == "__main__":
    main()
