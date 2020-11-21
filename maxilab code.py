totalchars= 256
def max_distinct_char(str, n): 
    count = [0] * totalchars
    for i in range(n): 
        count[ord(str[i])] += 1     
    max_distinct = 0
    for i in range(totalchars): 
        if (count[i] != 0): 
            max_distinct += 1        
    return max_distinct 


def smallestsub(str): 
    n = len(str)  
    max_distinct = max_distinct_char(str, n) 
    minl = n 
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = max_distinct_char(subs,  
                                                  subs_lenght) 
         
            if (subs_lenght < minl and 
                max_distinct == sub_distinct_char): 
                minl = subs_lenght 
  
    return minl 
str = input() 
l=smallestsub(str)
print(l)