# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

print("\n" + 30*"/")
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(100.15, "groceries")
food.withdraw(155.89, "restaurant and more food for dessert")
food.withdraw(25.89, "restaurant with girlfriend")
food.withdraw(5.89, "restaurant coffee")
print(("Food Get Balance").center(30, "-"))
print("Balance: " + str(food.get_balance()))
print(30*"/" + "\n")

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(10)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(150)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)