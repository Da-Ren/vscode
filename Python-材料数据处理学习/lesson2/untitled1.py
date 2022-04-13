# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:42:32 2021

@author: macbo
"""

file=open('graphene.cif','r') #打开cif文件
content=file.readlines()   # 全部读取cif里的的内容，变成每一行由构成的字符串列表
def striphuanhang(string):
    return string.strip('\r\n').strip('\n')  #去除传进来的字符串的换行符
lengths=[]    #用来存储晶格信息列表
_atom_site_set=[]  #用来存储跟原子信息有关的字段
index=0           #用来告诉我们当前的i是原来的cif里面的文件第几行，帮我们确定最后一个—_atom_site_set的行数
tmp=0  #用来存储最后一个_atom_site_set所在的行数，帮助我们确定包含原子信息的行
for i in content:
    if '_cell_length' in i :   #判断晶格信息是不是在这一行
        lengths.append(float(striphuanhang(i).split()[1]))
    #print(striphuanhang(i))
    if '_atom_site' in i:
        _atom_site_set.append(striphuanhang(i)) #存储'_atom_site 字段用来确定label和xyz分量所有原子中信息中的第几列
        tmp=index
    index=index+1   #每读取一行index+1，也就是index记录的其实就是当前i所在的行数
print(tmp)  
#print(lengths)
#print(_atom_site_set) 
    
for i in range(len(_atom_site_set)):  #迭代_atom_site_set字段
    if '_atom_site_label' in _atom_site_set[i]:
        label_index=i  #存储的是原子的label在原子信息的第几列，帮助我们切割
    if '_atom_site_fract_x' in _atom_site_set[i]:
        x_index=i  #存储的是原子的x在原子信息的第几列
    if '_atom_site_fract_y' in _atom_site_set[i]:
        y_index=i
    if '_atom_site_fract_z' in _atom_site_set[i]:
        z_index=i

print(label_index,x_index,y_index,z_index)
atom=[] #存储的是包含原子label和其对应的分量的坐标
for i in range(tmp+1,len(content)):  #从_atom_site后面开始读，读到文件最后
    if len(content[i].split())==len(_atom_site_set): #如果不符合前面_atom_site的总个数，也就是说不是我们所需要的原子信息
        atom_line=striphuanhang(content[i])
        atom_label=atom_line.split()[label_index] #根据前面所确定的lablel确定的第几列，切割得到的原子信息。
        x=float(atom_line.split()[x_index])#根据前面所确定的x分裂确定的第几列，切割得到的原子信息。
        y=float(atom_line.split()[y_index])
        z=float(atom_line.split()[z_index])
        atom.append([atom_label,x,y,z]) #添加原子label和其对应的分量的坐标
        
print(atom)
#print( _atom_site_set)






#43分钟