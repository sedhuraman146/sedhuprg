class Solution(object):
def reverse(self, x):
type x: int
rtype: int
negative = False
if(x < 0):
x = x * -1
negative = True
else:
x = x
sum = 0
dig = 1
strX = str(x)
lst = list(strX)
for i in lst:
sum += int(i) * dig
dig *= 10
if(abs(sum) > 2 ** 32):
return 0
elif(negative == True):
return sum * -1
else:
return sum
