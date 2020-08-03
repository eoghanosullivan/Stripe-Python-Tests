import stripe
from charges import chargeOption
# from connect import *

apiKey = input(
    "Enter Secret Test Key (Located - https://dashboard.stripe.com/test/apikeys) ")

stripe.api_key = apiKey


def options():
    print("Current list of functions")
    print("1 - Charges\n2 - Connect\n3 - Billing\n4 - Reporting")
    choice = input("Choose which function you wish to use -- ")
    if choice == "1":
        chargeOption()
    elif choice == 2:
        print("Still in testing")
    elif choice == 3:
        print("Still in testing")
    elif choice == 4:
        print("Still in testing")
    else:
        print("Still in testing")


options()
