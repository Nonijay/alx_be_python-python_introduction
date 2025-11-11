# lets declare our variables for income and expenses for the month, and let us collect user input directly.
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your montly expenses: ")

# let us calculate the monthly saving while converting the results from the variables to integers.
monthly_savings = float(int(monthly_income) - int(monthly_expenses))

print("your current monthly savings:", "$", monthly_savings)

# let us calculate the projected annual savings for one year

projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print ("projected savings after one year, with interest, is: ", "$",projected_savings)