import math
def sum(a,d,b,r,n):
sum1=0
for i in range(1,n+1):
sum+=((a+(i-1)*d)*(b*math.pow(r,i-1)))
a=1
d=1
b=2
r=2
n=3
print(sum(a,d,b,r,n))
