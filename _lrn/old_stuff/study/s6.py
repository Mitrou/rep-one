__author__ = 'User'
groceries = ["banana", "orange","apple"]

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

def computeBill(groceries):
    m = 0
    for i in groceries:
        if stock[i] > 0:
            m += prices[i]
            stock[i] -= 1
        else:
            pass
    return m
