def multiplication_table(number):
  """Prints the multiplication table of a given number."""
  # Check if the number is valid (positive integer)
  if not isinstance(number, int) or number <= 0:
    print("Please enter a positive integer.")
    return

  # Print the table header
  print("Multiplication Table of", number)
  print("-" * (len(str(number)) + 13))  # Adjust the length based on number length

  # Loop from 1 to 10 (or a higher limit if desired)
  for i in range(1, 11):
    product = number * i
    print(f"{number} x {i:2} = {product:3}")  # Format for alignment

# Get user input
while True:
  try:
    num = int(input("Enter a number: "))
    break
  except ValueError:
    print("Invalid input. Please enter a number.")

multiplication_table(num)