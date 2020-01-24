import stripe
from globalVariables import apiKey

def createPi():
    stripe.api_key=apiKey
    amount = input("Enter how much you wish to charge ")
    pmid= input("Enter payment method ")
    
    pi=stripe.PaymentIntent.create(
    amount=amount,
    currency="eur",
    payment_method=str(pmid),
    capture_method="automatic",
    confirm="true",
        )
    print(pi)
    
def listPi():
    stripe.api_key=apiKey
    limitPi = input("Enter how many charges you wish to list ")
    lstPi=stripe.PaymentIntent.list(limit=limitPi)
    
    print(lstPi)

def retreiveCharge():
    stripe.api_key=apiKey
    paymentIntent_id = input("Enter Payment Intent ID: ")
    charge = stripe.PaymentIntent.retrieve(
        paymentIntent_id)
    print(charge)
        