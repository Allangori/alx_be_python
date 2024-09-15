income = int (input ("Enter your monthly income:"))
expenses = int (input ("Enter your monthly expenses:"))
savings = income - expenses
projected_savings = savings * 12 + (savings * 12 * 0.05)
print ("Your monthly savings is:",savings)
print ("Your projected savings with interest is:",projected_savings)