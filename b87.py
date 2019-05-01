def gcd(n,m): 
    if(m==0): 
        return n 
    else: 
        return gcd(m,n%m) 
n = int(input("enter n:"))
m = int(input("enter m:"))
print ("The gcd is : ",end="") 
print (gcd(n,m)) 
