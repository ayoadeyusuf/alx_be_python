monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# calculating monthly savings
monthly_ savings = monthly_income - monthly_expenses

# calculating projected savings
projected_savings = monthly_savings * 12 * 0.05

# output
print('Your monthly savings are ${monthly_savings}')
print('Projected savings after one year, with interest, is: ${projected_savings}.')
