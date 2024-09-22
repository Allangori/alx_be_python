# square_pattern.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the user enters a positive integer
while size <= 0:
    size = int(input("Please enter a positive integer: "))

# Use a while loop to go through each row
row = 0
while row < size:
    # Use a for loop to print asterisks (*) side by side for each row
    for col in range(size):
        print("*", end="")  # Print asterisks without advancing to the next line
    print()  # After each row, move to the next line
    row += 1
