p_smooth = [1]  
def maxPrimeDivisor(n): 
MPD = -1
if n == 1 :  
return 1
while n % 2 == 0: 
MPD = 2
n = n // 2
size = int(n ** 0.5) + 1
for odd in range( 3, size, 2 ): 
while n % odd == 0: 
MPD = odd 
n = n // odd 
MPD = max (n, MPD)  
return MPD  
def generate_p_smooth(p, MAX_LIMIT):     
global p_smooth 
for i in range(2, MAX_LIMIT + 1): 
if maxPrimeDivisor(i) <= p: 
p_smooth.append(i) 
def find_p_smooth(L, R): 
global p_smooth 
if L <= p_smooth[-1]: 
for w in p_smooth : 
if w > R : break
if w >= L and w <= R : 
print(w, end =" ") 
print("") 
p = 7
L, R = 1, 100
MAX_LIMIT = 1000
generate_p_smooth(p, MAX_LIMIT)  
find_p_smooth(L, R) 
