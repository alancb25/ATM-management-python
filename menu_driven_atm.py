class Bank:
    
    def __init__(self,Account_no,Account_holder):
        self.Account_no=Account_no
        self.Account_holder=Account_holder
        self.balance=1000
        
    def balance_enquary(self):
        print(f"Initial balance:{self.balance}")

    def deposit(self):
        self.balance=self.balance+amount
        print(f"Balance After Deposit:{self.balance}")

    def withdraw(self):
        if self.balance>=wamount:
             self.balance=self.balance-wamount
             print(f"Balance After Withdrawed:{self.balance}")
        else:
            print("Insufficient Balance") 

s1=Bank(123456,"Edited Data")

while True:
    choice=int(input("1.Balance Enquiry\n2.Deposit\n3.Withdraw\n4.Exit\nEnter the Choice:"))
    if choice==1:
        s1.balance_enquary()
    elif choice==2:
        amount=int(input("Enter the Amount to Deposit:"))
        s1.deposit()
    elif choice==3:
        wamount=int(input("Enter the Amount to Withdraw:"))
        s1.withdraw()
    elif choice==4:
        print("Thank you")
        break
    else:
        print("Invalid choice")
print("THIS IS A N EDITTED FILE IN GIT")
