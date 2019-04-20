def power(base,exp):
  if(exp==1):
    return(base)
  if(exp!=1):
    return(base*power(base,exp-1))
base=int(input("enter base:"))
exp=int("enter exp value:"))
print(power(base,exp))
