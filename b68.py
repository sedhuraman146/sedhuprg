def multiple(n):
  if (n<0):
    return multiple(-n)
  if(n==0 or n==7):
    return true
  if(n<10):
    return false
return multiple(n/10-2*(n-n/10*10))
n=int(input("enter the number:"))
if(multiple(n):
  print("yes")
else:
  print("no")
