from pathlib import Path

TEXT = "You kneel beside him in the garden at dusk. The can tips. Water falls in a thin thread. The soil darkens, and drinks. A seedling trembles, and stands. His hands move slow. The oak he planted as a boy shades the roof. The seeds you watered will grow on after dark."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
