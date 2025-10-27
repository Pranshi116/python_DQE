import random
import string
from typing import List, Dict, Tuple

# Step 1: Data generation

def generate_random_dict() -> Dict[str, int]:
    """Generate one random dictionary with 1–5 unique letter keys and random integer values."""
    num_keys = random.randint(1, 5)
    keys = random.sample(string.ascii_lowercase, num_keys)
    return {key: random.randint(0, 100) for key in keys}


def generate_dict_list() -> List[Dict[str, int]]:
    """Generate a list containing 2–10 random dictionaries."""
    num_dicts = random.randint(2, 10)
    return [generate_random_dict() for _ in range(num_dicts)]

# Step 2: Processing logic

def collect_key_stats(dict_list: List[Dict[str, int]]) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
    """
    Collect statistics about keys:
    - result: max value for each key
    - key_origin: which dictionary had that max
    - key_counts: how many times each key appeared
    """
    result = {}
    key_origin = {}
    key_counts = {}

    for idx, d in enumerate(dict_list, start=1):
        for key, value in d.items():
            key_counts[key] = key_counts.get(key, 0) + 1
            if key not in result or value > result[key]:
                result[key] = value
                key_origin[key] = idx

    return result, key_origin, key_counts


def merge_dictionaries(dict_list: List[Dict[str, int]]) -> Dict[str, int]:
    """Merge all dictionaries according to the given rules."""
    result, key_origin, key_counts = collect_key_stats(dict_list)

    return {
        (f"{key}_{key_origin[key]}" if key_counts[key] > 1 else key): value
        for key, value in result.items()
    }

# Step 3: Main function

def main():
    dict_list = generate_dict_list()
    print("List of random dictionaries:")
    print(dict_list)

    final_result = merge_dictionaries(dict_list)
    print("\nMerged dictionary with max values and renamed keys:")
    print(final_result)

# Script entry point

if __name__ == "__main__":
    main()
