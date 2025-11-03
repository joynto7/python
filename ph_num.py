# gp_number_generator.py
# Generates Bangladesh GP-style numbers with prefix and fixed last-two digits.
# Example: prefix='013', last_two='29' -> '013' + middle6 + '29' e.g. '013000029'

import random
from typing import Iterator

def gp_number_generator(prefix: str = "013",
                        middle_len: int = 6,
                        last_two: str = "29") -> Iterator[str]:
    """
    Generator that yields numbers as strings, zero-padded.
    Yields numbers like: prefix + middle(6 digits) + last_two
    """
    if len(last_two) != 2:
        raise ValueError("last_two must be exactly 2 digits (e.g. '29').")
    if not prefix.isdigit() or not last_two.isdigit():
        raise ValueError("prefix and last_two must be numeric strings.")
    max_middle = 10 ** middle_len
    for i in range(max_middle):
        middle = f"{i:0{middle_len}d}"   # zero-pad to middle_len
        yield f"{prefix}{middle}{last_two}"

def write_all_to_file(filename: str,
                      prefix: str = "013",
                      middle_len: int = 6,
                      last_two: str = "29"):
    """
    Stream all numbers to a file, one per line.
    Warning: This will create a file with 1,000,000 lines for middle_len=6.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for num in gp_number_generator(prefix, middle_len, last_two):
            f.write(num + "\n")

def random_sample(n: int = 20,
                  prefix: str = "013",
                  middle_len: int = 6,
                  last_two: str = "29",
                  seed: int | None = None) -> list[str]:
    """
    Return a random sample of n distinct numbers from the space.
    This avoids creating the whole list by sampling integers directly.
    """
    if seed is not None:
        random.seed(seed)
    max_middle = 10 ** middle_len
    if n > max_middle:
        raise ValueError("n cannot be larger than the total number of combinations.")
    picks = set()
    while len(picks) < n:
        picks.add(random.randrange(0, max_middle))
    result = [f"{prefix}{i:0{middle_len}d}{last_two}" for i in sorted(picks)]
    return result

def sample_range(start_middle: int, end_middle: int,
                 prefix: str = "013",
                 middle_len: int = 6,
                 last_two: str = "29") -> list[str]:
    """
    Generate numbers where middle runs from start_middle to end_middle inclusive.
    start_middle/end_middle are integers in [0, 10^middle_len - 1].
    """
    max_middle = 10 ** middle_len
    if not (0 <= start_middle <= end_middle < max_middle):
        raise ValueError("start_middle/end_middle out of valid range.")
    return [f"{prefix}{i:0{middle_len}d}{last_two}" for i in range(start_middle, end_middle + 1)]

# Example usage (uncomment to run):
if __name__ == "__main__":
    # 1) Print a random sample of 20:
    sample = random_sample(20, prefix="013", middle_len=6, last_two="29", seed=1)
    print("Random sample of 20 numbers:")
    print("\n".join(sample))

    # 2) Write all 1,000,000 numbers to a file (commented out by default — large file):
    # write_all_to_file("gp_013_xxxxxx_29.txt", prefix="013", middle_len=6, last_two="29")

    # 3) Generate numbers for a sub-range, e.g., middle 1000..1010:
    rng = sample_range(1000, 1010, prefix="013", middle_len=6, last_two="29")
    print("\nRange sample 01300100029 .. 01300101029:")
    print("\n".join(rng))
