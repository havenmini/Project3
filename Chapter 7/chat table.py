# Function to print table of any number using while loop
def table_of_number():
    number = int(input("Enter the number for which you want the table: "))
    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i += 1

# Call the function
table_of_number()