a=int(input("enter the number"))
temp=a
rev=0
while(a>0):
  dig=a % 10
  rev=rev*10+dig
  a=a//10
if(temp==rev):
  print("the number is palindrome")
else:
  print("the number is not palindrome")
