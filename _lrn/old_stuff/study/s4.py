__author__ = 'User'
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

"""for i in prices:
    print i
    print "price:" + str(prices[i])
    print "stock:" + str(stock[i])
    print"""
m = 0
for i in prices:
    m += prices[i] * stock[i]
print m