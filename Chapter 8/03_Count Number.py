# Function to count occurrences of a digit in a given range
def count_digit_in_range(start, end, digit):
    count = 0
    for num in range(start, end + 1):
        count += str(num).count(str(digit))
    return count

# Taking user inputs
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
digit_to_count = int(input("Enter the digit to count: "))

# Counting the digit in the specified range
count = count_digit_in_range(start_range, end_range, digit_to_count)

# Printing the result
print(f"The digit {digit_to_count} appears {count} time(s) in the range {start_range} to {end_range}.")
