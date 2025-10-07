print("=======Welcome to BMS========")
#variables 
Bank_Name= "Meezan Bank"
Account_Type= "Current Account"
Min_Balance= 10000
Current_Balance=10000

#Input from user
Customer_Name=input("ENTER YOUR NAME:")
Customer_Age=int(input("ENTER YOUR AGE:"))
Account_No=int(input("Enter your Account No:"))
Initial_Deposit=int(input("ENTER THE AMOUNT YOU WANT TO DEPOSIT:"))

#display data type of the given inputs
print(type(Customer_Name))
print(type(Customer_Age))
print(type(Account_No))
print(type(Initial_Deposit))

#String Operations
print(Customer_Name.upper())
print(len(Customer_Name))

#Type casting
print(len(str(Account_No)))
print(float(Customer_Age))

#Data Stutures
History=[3000, 5000, 1300]
Available_acount_types=("Current", "Savings", "Fixed")
Account_Info={"Name":Customer_Name,"Age": Customer_Age, "Account No.":Account_No,"Balance": Current_Balance}

#Mathematical operations
Current_Balance=+Initial_Deposit
print(Current_Balance)
Withdrawal=int(input("Enter the amount you want to withdraw:"))
Current_Balance=Current_Balance-Withdrawal
print(Current_Balance)
Interest=Current_Balance*0.5
if Current_Balance%2==0:
    print("The account balance is even.")
else :
    print("The account balance is odd")

#Conditional Stutures
if Current_Balance>=100000:
    print("PREMIUM ACCOUNT HOLDER")
elif Current_Balance>=50000:
    print("GOLD ACCOUNT HOLDER")
elif Current_Balance>=20000:
    print("SILVER ACCOUNT HOLDER")
else:
    print("BASIC ACCOUNT HOLDER")

#While loops
password=input("ENTER YOUR PASSSWORD: ")
while password!="Grade8910@2019":
    password=input("your password is incorrect!! Reenter password:")
print("Login Successfull")
    
#Transaction Counter
for i in range(1, 11):
    print("TRANSACTION #{i}")
