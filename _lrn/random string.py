import random
import string
random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(10000)])

print(random)