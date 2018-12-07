__author__ = 'User'
groceries = ["banana", "orange","apple"]
food = ["banana", "apple"]
stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15
}

prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3
}

def computeBill(food):
    m = 0
    for i in food:
        m += prices[i]
    return m
print computeBill(food)