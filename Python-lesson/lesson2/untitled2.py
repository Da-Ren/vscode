# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 10:20:34 2021

@author: macbo
"""

#from __future__ import print_function
def appro_float(string): 
    try: 
        ret=float(string) #先尝试用普通的float()转换
    except: #呀，有括号出错了
        to=string.index('(') #获取(在第几位
        ret=float(string[0:to]) #取前面的有效子字符串再转
    return ret #把转的结果返回给调用者


string_case='123.1(2)' 
testcase=['123',string_case,'0.5(5)'] #有正常的浮点数，也有非正常的
for i in testcase:                    #正常的for 循环
    print(appro_float(i),end=',')
    
print(list(map(appro_float,testcase)))
print([appro_float(i) for i in testcase])