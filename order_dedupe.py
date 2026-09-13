#!/usr/bin/env python3
"""Dedupe fleet order-log CSV by order_id; flag missing email/amount (stdlib)."""
from __future__ import annotations
import argparse, csv, sys
from pathlib import Path

REQUIRED = ("order_id", "customer_email", "amount")

def process(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    rows_in = len(rows)
    seen = set()
    kept, flagged, dups = [], [], 0
    for row in rows:
        oid = (row.get("order_id") or "").strip()
        if oid in seen:
            dups += 1
            continue
        seen.add(oid)
        missing = [k for k in ("customer_email", "amount") if not (row.get(k) or "").strip()]
        if missing:
            flagged.append({**row, "_missing": missing})
            continue
        kept.append(row)
    return {
        "rows_in": rows_in,
        "duplicates_removed": dups,
        "rows_missing_fields": len(flagged),
        "rows_out": len(kept),
        "kept": kept,
        "flagged": flagged,
    }

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path)
    args = p.parse_args()
    r = process(args.input)
    print(f"rows_in={r['rows_in']} duplicates_removed={r['duplicates_removed']} rows_with_missing_fields={r['rows_missing_fields']} rows_out={r['rows_out']}")
    if args.output:
        with args.output.open("w", newline="", encoding="utf-8") as f:
            if r["kept"]:
                w = csv.DictWriter(f, fieldnames=list(r["kept"][0].keys()))
                w.writeheader(); w.writerows(r["kept"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
