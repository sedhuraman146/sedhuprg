def sort(string): 
words = string.split() 
words.sort() 
for i in words: 
print( i )  
if __name__ == '__main__': 
string = input("enter the string:")
print(sort(string)) 
