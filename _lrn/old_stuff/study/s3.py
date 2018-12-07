def hotelCost(days):
    return 140*days

bill = hotelCost(5)

def addMonthlyInterest(balance):
    return balance * (1 + (0.15 / 12) )

def makePayment(payment, bill):
    newBalance = addMonthlyInterest(bill - payment)
    return "You Still Owe: " + str(newBalance)
print bill
print makePayment(100, bill)
