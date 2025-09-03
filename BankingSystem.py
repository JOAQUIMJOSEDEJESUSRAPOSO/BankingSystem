#Criei a classe BankAccount para representar uma conta bancária.
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
   
    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            print (f"Deposite${amount}. Current balance: ${self.balance}")
        else:
            print ("Deposit amount must be positive.")
    def withdraw (self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print (f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print (f" Insufficient funds. Current balance: ${self.balance}")
        else:
            print ("Withdraw amount must be positive.")


    def check_balance(self):
        print (f"Current balance: ${self.balance}")



# Função principal para interagir com o usuário
def main():


    account = BankAccount("Anil")


    while True:
        print ("\n ---- Banking System ----")
        print ("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")


        choice = input("Choose an option: ")


        if choice == "1":
            print("\n --- Deposit ---")
            amount = float(input("Enter amount to deposit: R$"))
            account.deposit(amount)
        elif choice == "2":
            print("\n --- Withdraw ---")
            amount = float(input("Enter amount to deposit: R$"))
            account.withdraw(amount)
        elif choice == "3":
            print("\n --- Balance ---")
            account.check_balance()
        elif choice == "4":
            print("\nExiting the banking system. Goodbye !\n")
            break
        else:
            print ("\nInvalid option, Please try again!\n")

#
if __name__ == "__main__":
    main()
print (__name__)