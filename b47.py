l=[]
n=int(input("Enter how many numbers:"))
for i in range(n):
num=int(input("Enter the number:"))
l.append(num)
print("")
print("Maximum number is:",max(l))
print("Minimum number is:",min(l))
