"""Laugh Track: The Crypto Trading Joke Contest (make.fun).

Writes one original one-line crypto-trading joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback: ./output/entry.txt).

Python standard library only; deterministic; no network.
"""

import os

JOKE = "I set a stop-loss to protect my capital, then moved it down three times to protect my feelings."


def main() -> None:
    # Validate the sealed gate before writing anything.
    assert isinstance(JOKE, str) and JOKE.strip(), "joke must be non-blank text"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    data = JOKE.encode("utf-8")
    assert data.decode("utf-8") == JOKE, "joke must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(".", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
