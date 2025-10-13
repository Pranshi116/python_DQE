import random  # Import random module to generate random numbers

# Step 1: Create a list of 100 random numbers from 0 to 1000
numbers = [random.randint(0, 1000) for _ in range(100)]

# Step 2: Sort the list from min to max without using sort()
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap elements ,if they are in wrong order
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Step 3: Separate even and odd numbers into two lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Step 4: Calculate the average for even numbers
if even_numbers:  # Check to avoid division by zero
    avg_even = sum(even_numbers) / len(even_numbers)
else:
    avg_even = 0

# Step 5: Calculate the average for odd numbers
if odd_numbers:  # Check to avoid division by zero
    avg_odd = sum(odd_numbers) / len(odd_numbers)
else:
    avg_odd = 0

# Step 6: Print the results in the console
print("Average of even numbers:", avg_even)
print("Average of odd numbers:", avg_odd)
