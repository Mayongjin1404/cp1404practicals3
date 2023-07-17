MENU = """
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""
bonus = 0

sales = float(input("Enter sales: $"))
BONUS_RATE_BELOW_1000 = 0.10
BONUS_RATE_ABOVE_1000 = 0.15
while sales <= 0:
    if sales < 1000:
        bonus = sales * BONUS_RATE_BELOW_1000
    else:
        bonus = sales * BONUS_RATE_ABOVE_1000
    sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * BONUS_RATE_BELOW_1000
else:
    bonus = sales * BONUS_RATE_ABOVE_1000
print(bonus)
