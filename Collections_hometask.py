import random  # Import random module to generate random numbers
import string  # Import string module to get letters for dictionary keys

# Step 1: Create a list of random number of dictionaries (from 2 to 10)
num_dicts = random.randint(2, 10)
dict_list = []  # Empty list to store all dictionaries

for _ in range(num_dicts):
    # Random number of keys in each dictionary (from 1 to 5)
    num_keys = random.randint(1, 5)
    # Randomly select unique letters for keys
    keys = random.sample(string.ascii_lowercase, num_keys)
    # Create a dictionary with random values (0–100)
    d = {key: random.randint(0, 100) for key in keys}
    dict_list.append(d)  # Add the generated dictionary to the list

# Print the list of generated dictionaries
print("List of random dictionaries:")
print(dict_list)

# Step 2: Create one common dictionary from the list
# Rule:
#  - If dicts have the same key, take the MAX value and rename the key with dict number that had the max value.
#  - If key appears only once, take it as is.

result = {}        # Dictionary to store max values
key_origin = {}    # To store which dictionary number gave the max value
key_counts = {}    # To count how many times each key appears

# First loop — find max value for each key and which dictionary it came from
for idx, d in enumerate(dict_list, start=1):
    for key, value in d.items():
        # Count appearances of each key
        key_counts[key] = key_counts.get(key, 0) + 1

        # If key is new, add it
        if key not in result or value > result[key]:
            result[key] = value
            key_origin[key] = idx  # keep dictionary number of max value

# Second loop — rename keys that appear in more than one dictionary
final_result = {}
for key, value in result.items():
    if key_counts[key] > 1:  # Key appeared multiple times
        final_result[f"{key}_{key_origin[key]}"] = value
    else:
        final_result[key] = value  # Unique key

# Step 3: Print the final merged dictionary
print("\nMerged dictionary with max values and renamed keys:")
print(final_result)
