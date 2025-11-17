size_of_pattern = int(input("Enter the size of the pattern: "))
# Here we want to use a while loop and nested for loop to create a square pattern similar to the input
for i in range(size_of_pattern):
    for j in range(size_of_pattern):
        print("*", end = " ")
    print() # For printing in a new line