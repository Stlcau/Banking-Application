import time

print("Hello")
time.sleep(2)
print ("Welcome to Python Banking")
time.sleep(2)

Trials = 3
UserPin = 1234

while Trials != 0:
    Pin = int(input("Please Enter Your 4 Digit Pin Number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Invalid Pin Number, You Have", Trials, "Trials Left")
    else: 
        UserChoice = input("d: Deposit or w: Withdraw ")
        if UserChoice == "d":
            UserDeposit = input("Enter The Amount You Would Like To Deposit: ")
            print(UserDeposit, "$ Has Been Deposited Into Your Account")
        if UserChoice == "w":
            UserWithdraw = input("Enter The Amount You Would Like To Withdraw: ")
            print(UserWithdraw, "$ Has Been Withdrawn From Your Account")

    UserExit = input("Would You Like To Continue? Y/N: ")
    if UserExit == "N":
        print("Thank You For Using Python Banking")
        break
    else:
        continue



 
