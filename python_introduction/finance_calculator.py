# Here we declare variables for income and expenses and let us collect user input directly while converting the string to int with float() or int().
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your montly expenses: "))

# let us calculate the monthly saving while converting the results from the variables to integers.
monthly_savings = monthly_income - monthly_expenses

print("your current monthly savings:", "$", monthly_savings)

# let us calculate the projected annual savings for one year

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print ("projected savings after one year, with interest, is: ", "$",projected_savings)