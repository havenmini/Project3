# Get the list of numbers from the user
numbers = input("Enter a range of numbers separated by spaces: ").split()

# Convert the input strings to integers
numbers = [int(number) for number in numbers]

# Get the number to count from the user
number_to_count = int(input("Enter the number to count: "))

# Initialize the count variable
count = 0

# Loop through the list and count occurrences of the specified number
for number in numbers:
    if number == number_to_count:
        count += 1

# Print the result
print(f"The number {number_to_count} appears {count} times in the list {numbers}.")
