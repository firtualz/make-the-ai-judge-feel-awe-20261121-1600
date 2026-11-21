from pathlib import Path

TEXT = "Your father splits wood by the fire. The axe falls slower, and slower. A moth settles on the warm log, and does not move. Smoke rises, thin and straight, to the stars that watched the tree grow for a hundred years, and are still watching."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
