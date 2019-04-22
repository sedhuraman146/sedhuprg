def check(string):
vowels=set("aeiou")
s=set({})
for char in  string:
if char in vowels:
s.add(char)
else:
pass
if len(s)==len(vowels):
print("accepted")
else:
print("not accepted")
if __name__ == "__main__":
string="Seequial"
string=string.lower()
check(string)
