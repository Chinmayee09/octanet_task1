class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 1000.0  # Initial balance for demonstration purposes
        self.transaction_history = []

class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to store user data

    def authenticate_user(self, user_id, pin):
        # Authenticates the user based on user_id and PIN
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

    def display_interface(self, user):
        while True:
            print("\nATM MENU")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Show Transaction History")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.check_balance(user)
            elif choice == '2':
                self.perform_withdrawal(user)
            elif choice == '3':
                self.perform_deposit(user)
            elif choice == '4':
                self.show_transaction_history(user)
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def check_balance(self, user):
        print(f"Your balance is ${user.balance:.2f}")

    def perform_withdrawal(self, user):
        amount = float(input("Enter the withdrawal amount: $"))
        if amount <= user.balance:
            user.balance -= amount
            user.transaction_history.append(f"Withdrew ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. Your new balance is ${user.balance:.2f}")
        else:
            print("Insufficient funds for withdrawal.")

    def perform_deposit(self, user):
        amount = float(input("Enter the deposit amount: $"))
        user.balance += amount
        user.transaction_history.append(f"Deposited ${amount:.2f}")
        print(f"Deposited ${amount:.2f}. Your new balance is ${user.balance:.2f}")

    def show_transaction_history(self, user):
        print("\nTransaction History:")
        for transaction in user.transaction_history:
            print(transaction)

if __name__ == "__main__":
    atm = ATM()
    
    # Create user accounts and add them to the ATM's users dictionary
    user1 = User("chinu", "1234")
    user2 = User("mama", "5678")
    user3 = User("rahul", "9012")
    
    atm.users = {
        user1.user_id: user1,
        user2.user_id: user2,
        user3.user_id: user3
    }

    user_id = input("Enter your User ID: ")
    pin = input("Enter your PIN: ")

    user = atm.authenticate_user(user_id, pin)

    if user:
        print(f"Welcome, {user_id}!")
        atm.display_interface(user)
    else:
        print("Authentication failed. Please check your User ID and PIN.")
