# `Category` class in `budget.py`. It should be able to instantiate objects based
#  on different budget categories like *food*, *clothing*, and *entertainment*. 
# When objects are created, they are passed in the name of the category. The 
# class should have an instance variable called `ledger` that is a list. The 
# class should also contain the following methods:
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # `deposit` method that accepts an amount and description. If no description 
    # is given, it should default to an empty string. The method should append an
    #  object to the ledger list in the form of 
    # `{"amount": amount, "description": description}`.
    def deposit(self, amount, description=""):
        x = {"amount": amount, "description": description}
        self.ledger.append(x)

    # `withdraw` method that is similar to the `deposit` method, but the amount 
    # passed in should be stored in the ledger as a negative number. If there 
    # are not enough funds, nothing should be added to the ledger. This method 
    # should return `True` if the withdrawal took place, and `False` otherwise.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            x = {"amount": -amount, "description": description}
            self.ledger.append(x)
            return True
        else:
            return False

    # `get_balance` method that returns the current balance of the budget 
    # category based on the deposits and withdrawals that have occurred. 
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total = total + item['amount']
        return total

    # `transfer` method that accepts an amount and another budget category 
    # as arguments. The method should add a withdrawal with the amount and
    #  the description "Transfer to [Destination Budget Category]". The 
    # method should then add a deposit to the other budget category with 
    # the amount and the description "Transfer from [Source Budget Category]".
    #  If there are not enough funds, nothing should be added to either ledgers. 
    # This method should return `True` if the transfer took place, and `False` 
    # otherwise.
    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            x = "Transfer to " + budget_category.name
            y = "Transfer from " +  self.name
            self.withdraw(amount, x)
            budget_category.deposit(amount, y)
            return True
        else:
            return False

    # `check_funds` method that accepts an amount as an argument. It returns
    # `False` if the amount is greater than the balance of the budget category
    #  and returns `True` otherwise. This method should be used by both the
    #  `withdraw` method and `transfer` method.
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    # A title line of 30 characters where the name of the category is centered in a line of `*` characters.
    # A list of the items in the ledger. Each line should show the description and amount. The first 23 
    # characters of the description should be displayed, then the amount. The amount should be right aligned,
    #  contain two decimal places, and display a maximum of 7 characters.
    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            x = item['description'][:23].ljust(23) + format(item['amount'], '.2f').rjust(7) + "\n"
            output = output + x
        y = "Total: "+ format(self.get_balance(), '.2f')
        output = output + y
        return output


# Besides the `Category` class, create a function (outside of the class) called 
# `create_spend_chart` that takes a list of categories as an argument. It should
#  return a string that is a bar chart.
def create_spend_chart(categories):
    category_names = []
    spent = []
    spent_percentages = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total = total - item['amount']
        spent.append(round(total, 2))
        category_names.append(category.name)

    for amount in spent:
        x = round(amount / sum(spent), 2) * 100
        spent_percentages.append(x)

    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)

    for label in labels:
        graph = graph + str(label).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= label:
                graph = graph + "o  "
            else:
                graph = graph + "   "
        graph = graph + "\n"

    graph = graph + "    ----" + ("---" * (len(category_names) - 1))
    graph = graph + "\n     "

    longest_name_length = 0

    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)

    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph = graph + name[i] + "  "
            else:
                graph = graph + "   "
        if i < longest_name_length-1:
            graph = graph + "\n     "

    return(graph)
