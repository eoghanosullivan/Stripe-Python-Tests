import stripe

def chargeOption():
    print("Current list of functions")
    print("1 - Create a payment intent\n2 - List a number of Payment Intent id's (no pgination)\n3 - Retreive a charge\n4 - Reporting")
    choice = input("Choose which function you wish to use -- ")
    if choice == "1":
        createPi()
    elif choice == "2":
        listPi()
    elif choice == 3:
        print("Still in testing")
    elif choice == 4:
        print("Still in testing")
    else:
        print("Still in testing")

def createPi():
    amount = input("Enter how much you wish to charge ")
    pmid = input("Enter payment method ")

    pi = stripe.PaymentIntent.create(
        amount=amount,
        currency="eur",
        payment_method=str(pmid),
        capture_method="automatic",
        confirm="true",
    )
    print(pi)


def listPi():
    limitPi = input("Enter how many charges you wish to list ")
    lstPi = stripe.PaymentIntent.list(limit=limitPi)

    for pi in lstPi:
        print(pi.id)


def retreiveCharge():
    paymentIntent_id = input("Enter Payment Intent ID: ")
    charge = stripe.PaymentIntent.retrieve(
        paymentIntent_id,
    )
    print(charge)
