import re 
def extract(input): 
numbers = re.findall('\d+',input) 
numbers = map(int,numbers) 
print max(numbers) 
if __name__ == "__main__": 
    alpha = input("enter the alpha numeric:")
    extract(alpha) 
