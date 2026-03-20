class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        # Encapsulation: __balance is private
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        # Base logic: Simple withdrawal
        self.__balance -= amount
        print(f"Withdrew ${amount}. Remaining: ${self.__balance}")

    def get_balance(self):
        return self.__balance

# Inheritance: SavingsAccount IS-A BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, balance)
        self.min_balance = 100

    # Polymorphism: Method Overriding
    def withdraw(self, amount):
        current_balance = self.get_balance()
        if current_balance - amount < self.min_balance:
            print("Transaction Denied: Savings accounts must maintain $100.")
        else:
            # Call the parent class's withdraw logic
            super().withdraw(amount)

# --- Execution ---
print("--- Standard Account ---")
basic = BankAccount("John Doe", 500)
basic.withdraw(450) # Works fine

print("\n--- Savings Account ---")
savings = SavingsAccount("Jane Smith", 150)
savings.withdraw(80) # Should be denied (150 - 80 = 70, which is < 100)
