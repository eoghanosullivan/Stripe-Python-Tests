import stripe
from globalVariables import apiKey

def expressAccount():
    stripe.api_key = apiKey
    connectedAccountId = input("Enter Connected Account ID -- ")
    loginLink = stripe.Account.create_login_link(
        connectedAccountId,
    )
    
    print(loginLink)

def ConBal():
    stripe.api_key=apiKey
    connectedAccountId = input("Enter Connected Account ID -- ")
    balance = stripe.Balance.retrieve(
        stripe_account=connectedAccountId
    )
    
    print(balance)

def lstAccount():
    stripe.api_key=apiKey
    limitAcc = input("Enter how many charges you wish to list ")
    accLst = stripe.Account.list(limit=limitAcc)

    print(accLst)