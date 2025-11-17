number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    #Calculate the product of the input number and the current factor (i)
    product = number * i
    # Print the equation in a clear format
    print (f"{number}*{i} = {product}", end = "\t") 
    #print with tabs for better formatting
# print()
# #move to a new line after each row