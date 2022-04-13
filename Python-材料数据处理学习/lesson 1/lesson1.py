# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list_case=[1,2,3]

for i in range(0,len(list_case)):
   # print(list_case[i])
   pass

    
    
    
for i in list_case:
    if i == 3:
        print(i)
        break
string_case='123.1(2)'
def appro_float(string_case):
    try:
        return float(string_case)
    except:
   
        to=string_case.index('(')
        substring_case=string_case[0:to]
        return float(substring_case)



lit_case=[string_case,'123','567(1)']
for i in lit_case:
    print(appro_float(i))
    

#lit_case=[string_case,'123','567(1)']
