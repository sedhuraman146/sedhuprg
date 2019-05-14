def isEditDistanceOne(s1, s2): 
    m = len(s1) 
    n = len(s2) 
    if abs(m - n) > 1: 
        return false 
    count = 0
    i = 0
    j = 0
    while i < m and j < n: 
        if s1[i] != s2[j]: 
            if count == 1: 
                return false 
           if m > n: 
                i+=1
            elif m < n: 
                j+=1
            else:   
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1
    if i < m or j < n: 
        count+=1
    return count == 1
s1 = input("enter the string1 :")
s2 = input("enter the string2 :")
if isEditDistanceOne(s1, s2): 
    print ("Yes")
else: 
    print ("No")
