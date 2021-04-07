
# The following improvements where made to the last course
# i. The current ATM time was dispplayed
#ii. Introduced other introductory messages
#iii. Did a validation for password confirmation (i.e reconfirm password) upon registration.
#iv. Worked on the deposit function and withdrawal operation
# The first option should be to register then you login afterwards.

import datetime
import random
database ={}


def init():
    greetingMessage= "Hello our esteemed Customer, welcome to the Zuri Bank ATM"
    covidMessage = "We want to still bank with you tomorrow, to help us achieve this, adhere to all covid-19 protocols"
    currentTime= datetime.datetime.now()
    visitTimeMessage = "The current time is {}".format(currentTime)
    print(greetingMessage)
    print(covidMessage)
    print(visitTimeMessage)
    isValidOptionSelected=False
    while isValidOptionSelected==False:
        haveAccount= int(input("Are you an existing (1) or New Customer (2)? \n")) 
        if (haveAccount == 1):
            isValidOptionSelected=True
            login()
        elif (haveAccount == 2):
            isValidOptionSelected=True
            register()
        else:
            print("Please select either option 1 or 2")
            

def login ():
    print("******Login to your account******")
    isLoginSuccessful=False
    while isLoginSuccessful == False:
        UseraccountNumber= int(input("Enter account number  \n"))
        password = input("Enter your password  \n")
        
        for accountNumber, userDetails in database.items():
            if(accountNumber == UseraccountNumber):
                if (userDetails[3]==password):
                    isLoginSuccessful=True
            
        # print("Incorrect account number or password")
                
    bankOperation(userDetails)

def register ():
    print("********Register********")
    firstName = input("Enter your first name \n")
    lastName = input("Enter your last name \n")
    email = input("Enter your email address \n")
    password = input("Enter your password \n")
    confirmPassword = input("Please confirm your password \n")
    if (password==confirmPassword):

        accountNumber= generateAccountNumber()  
        database[accountNumber]=[firstName, lastName, email, password]

        print  ("Your Account has been created: {}".format(accountNumber))
        login()
    else:
        print("Passwords do not match")
        register ()
         

def bankOperation(user):
    print("Welcome {} {} ".format(user[0], user[1]))
    


    selectedOption= int(input("what would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))
    if selectedOption==1:
        depositOperation()
    elif (selectedOption==2):
        withdrawalOperation()
    elif (selectedOption==3):
        print("You have successfully logged out")
        logout()
    elif (selectedOption==4):
        exit()
    else:
        print("Invalid Option selected")
        bankOperation()

def depositOperation (): 
    print("*****Deposit Operation*****")
    depositAmt = int(input("Enter amount to deposit \n"))
    print("Your deposit of {} is successful".format(depositAmt))

def withdrawalOperation (): 
    print("*****Withdrawal*****")
    withdrawalAmt = int(input("Enter amount to withdraw  \n"))
    print("Your withdrawal of {} is successful".format(withdrawalAmt))

def generateAccountNumber():
    return random.randrange(1000000000,9999999999)

def logout():
    login()

init()
