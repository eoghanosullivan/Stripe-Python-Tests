import main

def createPi():
    stripe.api_key=apiKey
    amount = input("Enter how much you wish to charge ")
    pmid= raw_input("Enter payment method ")
    
    pi=stripe.PaymentIntent.create(
    amount=amount,
    currency="eur",
    payment_method=str(pmid),
    capture_method="automatic",
    confirm="true",
        )
    print pi
    
def listPi():
    stripe.api_key=main.apiKey
    limitPi = input("Enter how many charges you wish to list ")
    lstPi=stripe.PaymentIntent.list(limit=limitPi)
    
    print lstPi


def retreiveCharge():
	paymentIntent_id = input("Enter Payment Intent ID: ")
        stripe.api_key=apiKey
        
        charge = stripe.PaymentIntent.retrieve(
          paymentIntent_id,
          )
    
        print charge
   