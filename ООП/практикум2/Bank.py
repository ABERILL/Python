class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
        else:
            print("Error: Account number already exists.")

    def make_deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
        else:
            print("Error: Account number does not exist.")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
            else:
                print("Error: Insufficient funds.")
        else:
            print("Error: Account number does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print("Balance for account", account_number,
                  "is:", self.accounts[account_number])
        else:
            print("Error: Account number does not exist.")


bank = Bank()
acno1 = "SB-123"
damt1 = 1000
print("New account number:", acno1, "Initial balance:", damt1)

bank.create_account(acno1, damt1)
acno2 = "SB-124"
damt2 = 1500
print("New account number:", acno2, "Initial balance:", damt2)

bank.create_account(acno2, damt2)
wamt1 = 600
print("\nDeposit amount", wamt1, "to A/c No.", acno1)

bank.make_deposit(acno1, wamt1)
wamt2 = 350
print("Withdraw amount", wamt2, "From A/c No.", acno2)
bank.make_withdrawal(acno2, wamt2)
print("Account number:", acno1)
bank.check_balance(acno1)
print("Account number:", acno2)
bank.check_balance(acno2)
wamt3 = 1200
print("Withdraw amount", wamt3, "From A/c No.", acno2)
bank.make_withdrawal(acno2, wamt3)
acno3 = "SB-134"
print("A/c. No.", acno3)
bank.check_balance(acno3)  # Non-existent account number
