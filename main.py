from pathlib import Path

TEXT = "The tide goes out and leaves a pool in the rock. A crab crosses it once, slowly. Then stops. An anemone opens, and closes on nothing. The last wave slides back, and does not return. The water clears. Far above, the stars come out one by one, and the pool holds them all, still."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
