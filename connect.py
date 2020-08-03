import main
import stripe

def connectoption():
     print("Current list of functions")
    print("1 - Express Account Login link\n2 - Connect\n3 - Billing\n4 - Reporting")
    choice = input("Choose which function you wish to use -- ")
    if choice == "1":
        expressAccount()
    elif choice == 2:
        print("Still in testing")
    elif choice == 3:
        print("Still in testing")
    elif choice == 4:
        print("Still in testing")
    else:
        print("Still in testing")

def expressAccount():
    connectedAccountId = input("Enter Connected Account ID -- ")
    loginLink = stripe.Account.create_login_link(
        connectedAccountId,
    )

    print(loginLink)


def ConBal():
    connectedAccountId = input("Enter Connected Account ID -- ")
    balance = stripe.Balance.retrieve(
        stripe_account=connectedAccountId
    )

    print(balance)
