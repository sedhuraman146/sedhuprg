num=[1,2,3,4,5]
n=len(num)
num.sort()
if n%2==0:
median1=num[n//2]
median2=num[n//2-1]
median=(median1+median2)/2
else:
median=num[n//2]
print("median is :"+str(median))
