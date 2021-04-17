# Create a Budget class that can instantiate objects based on
# different budget categories like food, clothing, and entertainment.
#  These objects should allow for
# 1.  Depositing funds to each of the categories
# 2.  Withdrawing funds from each category
# 3.  Computing category balances
# 4.  Transferring balance amounts between categories

# Push your code to GitHub, and submit the repo link.

class Category():
    # create the instance of the object
    def __init__(self, name):
        self.name = name
    # Create an empty list of dictionary containing amount and description
    #ledger = [{"amount": amount, "description": description}]
        self.ledger = list()

    def __str__(self):
        items = ""
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + \
                f"{item['amount']:>7.2f}" + '\n'
        output = "Total: " + str(self.get_balance())
        return f"{self.name:*^30}\n" + items + output

    # Deposit Funds
    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})

    # Withdraw Funds
    def withdraw(self, amount, desc=""):
        if(self.get_balance() >= amount):
            self.ledger.append({"amount": -amount, "description": desc})
        else:
            return f"Insufficient Fund"

    # Compute the Balances
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    # Transfer funds from each category
    def transfer(self, amount, category):
        if(self.get_balance() >= amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
