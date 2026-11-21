import os

TEXT = "The tide goes out and leaves a pool in the rock. A crab crosses it once, slowly. Then stops. An anemone opens, and closes on nothing. The last wave slides back, and does not return. The water clears. Far above, the stars come out one by one, and the pool holds them all, still."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
