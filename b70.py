def power(n):
if(n & not(n&(n-1))):
return n
while(n!=0):
n>>=1
count+=1
return1<<count
n=int(input("enter the number:"))
print(power(n))
