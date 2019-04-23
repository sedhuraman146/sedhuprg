def binary(n):
if n > 1:
binary ( n // 2)
print(n % 2,end="")
dec=int(input("enter the number:")
binary(dec)
