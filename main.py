import stripe

apiKey =raw_input("Enter Secret Test Key (Located - https://dashboard.stripe.com/test/apikeys) ")
def options():
    print("Current list of functions")
    print("1 - Charges\n2 - Connect\n ")
    choice = input("Choose which function you wish to use -- ")
    if choice == 1:
        charges()
    elif choice == 2:
          connect()
    else:
        print("Still in testing")
        
        
        
def charges():
    print("Current list of functions")
    print("1 - Create Payment Intent\n2 - List Charges\n3 - Retreive Charge")
    chargeChoice = raw_input("Choose which function you wish to use -- ")
    if chargeChoice == "1":
        createPi()
    elif chargeChoice == "2":
        listPi()
    elif chargeChoice == "3":
        retreiveCharge()
    else:
        print("Still in testing")
        
        
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
    stripe.api_key=apiKey
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

def connect():
    print("Current list of functions")
    print("1 - Express Dashbpard Account link\n2 - Account Balance")
    chargeChoice = raw_input("Choose which function you wish to use -- ")
    if chargeChoice == "1":
        expressAccount()
    elif chargeChoice == "2":
        ConBal()
    else:
        print("Still in testing")
        
        
        
def expressAccount():
    stripe.api_key = apiKey
    connectedAccountId = raw_input("Enter Connected Account ID -- ")
    loginLink = stripe.Account.create_login_link(
        connectedAccountId,
    )
    
    print(loginLink)

def ConBal():
    stripe.api_key=apiKey
    connectedAccountId = raw_input("Enter Connected Account ID -- ")
    balance = stripe.Balance.retrieve(
        stripe_account=connectedAccountId
    )
    
    print balance

options()