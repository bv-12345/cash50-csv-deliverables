#!/usr/bin/env python3
"""Convert fleet-buyer sample CSV to JSON array (stdlib only)."""
from __future__ import annotations
import argparse, csv, json, sys
from pathlib import Path

def convert(path: Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out = {}
            for k, v in row.items():
                if v is None or v == "":
                    out[k] = None
                elif k == "amount":
                    out[k] = float(v)
                else:
                    out[k] = v
            rows.append(out)
    return rows

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path)
    args = p.parse_args()
    rows = convert(args.input)
    text = json.dumps(rows, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    print(f"row_count={len(rows)}", file=sys.stderr)
    print("sample_first_3=", json.dumps(rows[:3], indent=2), file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
