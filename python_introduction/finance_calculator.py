monthly_income = float (input ("Enter your monthly income:"))
monthly_expenses = float (input ("Enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings is:",monthly_savings)
print ("Your projected savings with interest is:",projected_savings)