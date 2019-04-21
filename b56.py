def validatestring(s):
letter_flag=false
number_flag=false
for i in s:
if i.isalpha():
letter_flag=true
if i.isdigit():
number_flag=true
return letter_flag and number_flag
print validatestring("hasalphanum23")
print validatestring("some string")
