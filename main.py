import budget

food_budget = budget.Budget("food")
food_budget.withdrawal(500)
print(food_budget.category)
print(food_budget.total_budget)
food_budget.deposit(50000,"lunch bill")
food_budget.withdrawal(12000)
print(food_budget.get_balance())

clothing_budget = budget.Budget("clothing")
print(clothing_budget.category)
print(clothing_budget.total_budget)
clothing_budget.deposit(10000,"dinner gown")
clothing_budget.withdrawal(2000)
print(clothing_budget.get_balance())

food_budget.transfer(2000,clothing_budget)
print(food_budget.get_balance())
print(clothing_budget.get_balance())

entertainment_budget = budget.Budget("entertainment")
print(entertainment_budget.category)
print(entertainment_budget.total_budget)
entertainment_budget.deposit(20000,"music")
entertainment_budget.withdrawal(3000)
print(entertainment_budget.get_balance())