#Criei a classe BankAccount para representar uma conta bancária.
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.pix_key = None
        self.password = 9292
   
    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            print (f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print ("Deposit amount must be positive.")

    def withdraw (self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print (f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print (f"Insufficient funds. Current balance: ${self.balance}")
        else:
            print ("Withdraw amount must be positive.")

    def check_balance(self):
        print (f"Current balance: ${self.balance}")

    def has_pix(self):
        return self.pix_key is not None
    
    def get_pix(self):
        if self.has_pix():
            return print (f"\nYour Pix key is: {self.pix_key}\n")
        else:
            print("\nNo Pix key registered.\n")
    
    def set_pix(self, new_key):
        if not new_key or new_key == "":
            return print ("The Pix key cannot be empty.")
        
        if self.has_pix():
            old_key = self.pix_key
            self.pix_key = new_key
            return print (f"Pix key changed from {old_key} to {self.pix_key}")
        else:
            self.pix_key = new_key
            return print (f"Registered Pix key: {self.pix_key}")
        
    def verification_pix(self):
        if self.has_pix():
            return "5. Change Pix"
        else:
            return "5. Register Pix"
        
    def set_password(self, new_password):
        if not new_password or new_password == "":
            return print ("Password cannot be empty!")
        else:
            old_password = self.password
            self.password = new_password
            return print (f"Password changed from {old_password} to {self.password}")

# Função principal para interagir com o usuário
def main():
    #Informações iniciais
    agency_user = ("000-1")
    registration = ("Carlos")

    account = BankAccount(registration)

    while True:#Sistema para verificar se login e senha está correto
        login = input("Login: ")
        password = int(input("Password: "))
        agency = input("Agency: ")

        if login == registration and password == account.password and agency_user == agency:
            while True:
                print ("\n ---- Banking System ----")
                print("=================")
                print(f"Hello, {registration}!\nAgency: {agency_user}")
                account.check_balance()
                print("=================")
                print (f" \n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Consult Pix\n{account.verification_pix()}\n6. Change Password \n7. Exit")


                choice = input("Choose an option: ")


                if choice == "1":
                    print("\n --- Deposit ---")
                    amount = float(input("Enter amount to deposit: R$"))
                    account.deposit(amount)
                elif choice == "2":
                    print("\n --- Withdraw ---")
                    amount = float(input("Enter amount to withdraw: R$"))
                    account.withdraw(amount)
                elif choice == "3":
                    print("\n --- Balance ---")
                    account.check_balance()
                elif choice == "4":
                    account.get_pix()
                elif choice == "5":
                    new_key = int(input("Choose new pix key: "))
                    account.set_pix(new_key)
                elif choice == "6":
                    new_password = int(input("Choose new password: "))
                    account.set_password(new_password)
                elif choice == "7":
                    print("\nExiting the banking system. Goodbye !\n")
                    break
                else:
                    print ("\nInvalid option, Please try again!\n")
        else:
            print("Some data is not correct!")


if __name__ == "__main__":
    main()
print (__name__)