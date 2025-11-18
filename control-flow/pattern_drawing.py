# Start a loop for continuous input until a valid number is entered
while True:
    size_of_pattern = int(input("Enter the size of the pattern: "))

    # Input Validation: Check if the string can be converted to an integer
    try:
        size = int(size_of_pattern)
        #break the loop if the conversion is successful
        break
    except : 
        #inform the user and continue the whie loop for new input
        print("Invalid Input. Pleae enter a whole number.")
print(f"\n Generating a {size} x {size} pattern")


# Outer loop(rows). controls how many lines are printed.
for i in range(size_of_pattern):
    # Inner loop (columns): controls how many stars are printed on each row
    for j in range(size_of_pattern):
        # print an Asterisk followed by a space, keeping it on the same line.
        print("*", end = " ")
    # AFter the inner loop finished (one row is complete), move to a new line
    print() # For printing in a new line