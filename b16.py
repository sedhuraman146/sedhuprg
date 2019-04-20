a=int(input("enter the limit:"))
b=int(input("enter the limit:"))
for num in range(a,b+1):
if num>1:
for i in range(2,num):
if(num%1)==0:
break;
else:
print(num)
