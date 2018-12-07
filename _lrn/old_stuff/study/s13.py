'''__author__ = 'User'
import math
x = input('qweqeqwe')
i = math.factorial(x)
print i

def fact(n):
	if n == 0:
		return 1
	return fact(n - 1) * n

print fact(5)'''


def po(x):
	if x == 2:
		return True
	elif x <= 1:
		return False
	else:
		for i in range(2, x):
			if x % i == 0:
				return False
		return True


print po(25)
