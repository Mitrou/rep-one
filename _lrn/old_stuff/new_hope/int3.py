# class Parent(object):
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
# print Parent.x, Child1.x, Child2.x
# # Child1.x = 2
# print Parent.x, Child1.x, Child2.x
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x


# def div1(x, y):
#     print "%s/%s = %s" % (x, y, x / y)
#
#
# def div2(x, y):
#     print "%s//%s = %s" % (x, y, x // y)
#
#
# div1(5, 2)      # 5/3 = 2
# div1(5., 2)     #5.0/3 = 2.5
# div2(5, 2)      #5//3 =
# div2(5., 2)

# list = ['a', 'b', 'c', 'd', 'e']
# print list[2:]

# list = [ [ ] ] * 5
# print list  # output?
# list[0].append(10)
# print list  # output?
# list[1].append(20)
# print list  # output?
# list.append(30)
# print list  # output?
#
# #        0   1   2   3    4    5    6    7    8
# list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
# [x for x in list[::2] if x%2 == 0]


class DefaultDict(dict):
    def __missing__(self, key):
        return []

d = DefaultDict()
d['florp'] = 127
d['www'] = 122

print(d)