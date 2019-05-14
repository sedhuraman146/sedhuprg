mod = 1000000007
MAX = 10000
prefix = [0]*(MAX + 1) 
def buildPrefix(): 
    prime = [True]*(MAX + 1) 
    p = 2
    while p * p <= MAX : 
        if (prime[p] == True) : 
            for i in range( p * 2, MAX+1, p): 
                prime[i] = False
        p += 1
    prefix[0] = prefix[1] = 1
    for p in range(2,MAX+1) : 
        prefix[p] = prefix[p - 1] 
        if (prime[p]): 
            prefix[p] = (prefix[p] * p) % mod 
def power(x, y,p): 
    res = 1
    x = x % p 
    while (y > 0) : 
        if (y & 1): 
            res = (res * x) % p 
        y = y >> 1
        x = (x * x) % p 
    return res 
def inverse( n): 
    return power(n, mod - 2, mod) 
def productPrimeRange(L, R): 
    return (prefix[R] * inverse(prefix[L - 1])) % mod 
if __name__ == "__main__": 
    buildPrefix() 
    L = int(input("enter the number1:"))
    R = int(input("enter the number2:"))
    print(productPrimeRange(L, R)) 
