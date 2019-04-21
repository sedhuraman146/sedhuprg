def ispowoftwo(n):
if(n==0):
return false
while(n!=1):
if(n%2!=0):
return false
n=n//2
if(ispowoftwo(31)):
print("yes")
else("no)
if(ispowoftwo(64)):
print("yes")
else:
print("no")
