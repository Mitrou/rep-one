# def multipliers():
#     return [lambda x, i=i: i * x for i in range(8)]
#
#
# print [m(7) for m in multipliers()]


def multipliers():
    for i in range(4):
        yield lambda x: i * x

print([m(7) for m in multipliers()])
