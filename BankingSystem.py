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
    #Login inicial
    agency_user = ("000-1")
    registration = ("Carlos")
    key = ("9292")

    account = BankAccount(registration)

    while True:#Sistema para verificar se login e senha está correto
        login = input("Login: ")
        password = input("Password: ")
        agency = input("Agency: ")

        if login == registration and password == key and agency_user == agency:
            while True:
                print ("\n ---- Banking System ----")
                print("=================")
                print(f"Hello, {registration}!\n Agency: {agency_user}")
                account.check_balance()
                print("=================")
                print (" \n 1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n")


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
        else:
            print("Algum dos dados não está correto!")


if __name__ == "__main__":
    main()
print (__name__)