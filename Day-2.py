meal_cost = float(input(f"Enter the meal cost: "))
tip_percent = int(input(f"Enter the tip percentage: "))
tax_percent = int(input(f"Enter the tax percentage: "))

tip = meal_cost * (tip_percent / 100)
tax = meal_cost * (tax_percent / 100)

total_cost = round(meal_cost + tip + tax)
print(total_cost)