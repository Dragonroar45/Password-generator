import random
import string
a = string.ascii_lowercase + string.ascii_uppercase + string.digits
sep = ""
c = sep.join(a)
def passw_para(x):
    b = random.choices(a, k = x)
    return b
y = int(input("Enter the length of your password: "))
c = passw_para(y)
d = ''.join(c)
print(d)
