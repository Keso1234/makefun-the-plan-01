import os

MAX_ENTRY_LENGTH = 280

ENTRY = (
    "Day 1: crawl 500 small Shopify stores losing sales, screenshot broken "
    "checkout links and dead buttons, then email owners the proof free and "
    "offer the fix for $49 via Stripe. Fix 2 faults a day with code. Expect "
    "10 sales in 30 days: $490 revenue, about $540 held after $50 costs."
)


def main():
    if not 1 <= len(ENTRY) <= MAX_ENTRY_LENGTH or not ENTRY.strip():
        raise ValueError(
            f"entry must be 1-{MAX_ENTRY_LENGTH} characters, not only whitespace"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
