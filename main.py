from paymentIntents import *
from connect import *

def options():
    print("Current list of functions")
    print("1 - Payment Intents\n2 - Connect\n ")
    choice = input("Choose which function you wish to use -- ")
    if choice == "1":
        paymetnIntents()
    elif choice == "2":
        connect()
    else:
        print("Still in testing")
        
        
        
def paymentIntents():
    print("Current list of functions")
    print("1 - Create Payment Intent\n2 - List Charges\n3 - Retreive Charge")
    chargeChoice = input("Choose which function you wish to use -- ")
    if chargeChoice == "1":
        createPi()
    elif chargeChoice == "2":
        listPi()
    elif chargeChoice == "3":
        retreiveCharge()
    else:
        print("Still in testing")


def connect():
    print("Current list of functions")
    print("1 - Express Dashbpard Account link\n2 - Account Balance\n3 - List Connected accounts")
    chargeChoice = input("Choose which function you wish to use -- ")
    if chargeChoice == "1":
        expressAccount()
    elif chargeChoice == "2":
        ConBal()
    elif chargeChoice=="3":
        lstAccount()
    else:
        print("Still in testing")
        
options()