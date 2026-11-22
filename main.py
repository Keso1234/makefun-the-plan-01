"""Write one 30-day money plan to /output/entry.txt.

Stdlib only, no network, no randomness: the same text every run.
"""

import os

TEXT = (
    "Day 1: crawl 200 small Shopify stores, test every checkout button "
    "and screenshot each broken one. Email owners the proof free, offer "
    "the $49 Stripe fix. Fix 2 a day yourself with code. Others sell "
    "audits, you sell proof first. $50 costs, 10 sales = $490, hold "
    "~$540 day 30."
)


def main() -> None:
    if not TEXT or not TEXT.strip():
        raise ValueError("entry text must not be empty or only whitespace")
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text is {len(TEXT)} chars, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Round-trip check: what was written is exactly what we validated.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT or not 1 <= len(written) <= 280 or not written.strip():
        raise ValueError("written entry failed the 1-280 char check")


if __name__ == "__main__":
    main()
