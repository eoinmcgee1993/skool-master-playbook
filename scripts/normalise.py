#!/usr/bin/env python3
"""Convert authorised inbox material into a deterministic JSON bundle."""
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INBOX=ROOT/"data"/"inbox"
OUT=ROOT/"data"/"normalised"/"bundle.json"

def read_item(path):
    raw=path.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    text=raw.decode("utf-8", errors="replace")
    return {
        "id": digest[:16],
        "title": path.stem,
        "source": "authorised-inbox",
        "source_locator": str(path.relative_to(ROOT)),
        "source_type": path.suffix.lstrip(".") or "file",
        "claim": text[:4000],
        "action": "",
        "prerequisites": [],
        "tools": [],
        "risks": [],
        "confidence": "source",
        "labels": ["SOURCE"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

def main():
    items=[read_item(p) for p in sorted(INBOX.rglob("*")) if p.is_file() and p.name != ".gitkeep"]
    bundle={
        "manifest":{
            "schema_version":"1.0",
            "generated_at":datetime.now(timezone.utc).isoformat(),
            "source_count":len(items)
        },
        "items":items
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
