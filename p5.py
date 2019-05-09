class integer:
  def roman(self,s):
      n=('I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000)
      int=0
      for i in range(len(s)):
        if i>0 and n[s[i]]>n[s[i-1]]:
          int +=n[s[i]]-2*n[s[i-1]]
        else:
          int +=n[s[i]]
      return int
print(integer().roman(input("enter the roman:")))
