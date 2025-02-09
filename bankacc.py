class BankAccount:
    def _init_(self,account_number,account_holder,initial_balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=initial_balance
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            l4.config(text=f"Deposit ${amount}. New balance: ${self.balance}")
        else:
            l4.config(text=f"Invalid amount. Please enter positive value")

    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            l5.config(text=f"withdraw ${amount}. new balance is Rs{self.balance}")
        elif amount>=0:
            l5.config(text=f"Invalid amount. Please enter positive value") 
        else:
            l5.config(text=f"Insufficient balance")

    def check_balance(self):
        l5.config(text=f"Account balance for {self.account_holder} : $ {self.balance}")


def check_balance1():
    account_number=t1.get()
    account.get(account_number)
    if account:
        account.check_balance()
    else:
        l5.config(text=f"Account not found")
def deposite_money():
    account_number=t1.get()
    account=account.get(account_number)
    if account:
        amount=t3.get()
        account.deposit(amount)
    else:
        l4.config(text="Account not found")
def withdraw_money():  
    account_number=t1.get()
    account=account.get(account_number)
    if account:
      account=t3.get()      
            

account={}


def register_account():
    account_number=t1.get()
    username=t2.get()
    initial_balance=t3.get()
    account[account_number]=BankAccount(account_number,username,initial_balance)

    l4.config(text=f"Account for {username} registered with an initial balance of $ {initial_balance}.")

import tkinter as tk
root=tk.Tk()


root.title("Bank App")
l1=tk.Label(root,text="Account Number")
l2=tk.Label(root,text="username")
l3=tk.label(root,text="Amount")
t1=tk.Entry(root)
t2=tk.Entry(root)
t3=tk.Entry(root)
b1=tk.Button(root,text="Registration",command=register_account)
b2=tk.Button(root,text="View Balance",command=check_balance1)
b3=tk.Button(root,text="deposit",command=deposite_money)
b4=tk.Button(root,text="Withdraw",command=withdraw_money)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)


t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)
b1.grid(row=3,column=1)
b2.grid(row=4,column=1)
b3.grid(row=5,column=1)
b4.grid(row=6,column=1)
l4=tk.Label(root,text="",fg="green")
l4.grid(row=7,column=1)
l5=tk.Label(root,text="",fg="green")
l5.grid(row=8,column=1)

tk.mainloop()