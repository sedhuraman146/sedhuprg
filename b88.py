def gcd(n,m): 
if (n == m): 
return n 
if (n > m): 
return gcd(n-m, m) 
return gcd(n, m-n) 
def lcm(n,m): 
return (n*m) / gcd(n,m) 
n=int(input("n:"))
m=int(input("m:"))
print('LCM of', n, 'and', n, 'is', lcm(n, m))
