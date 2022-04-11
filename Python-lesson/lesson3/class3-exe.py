# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:23:01 2021

@author: macbo
"""

import re
# AVector="2.81533649566357,-0.627301893975115,-2.77555756156289e-017"
with open ("CuO111_2.xsd",'r') as reader:
    all=reader.read()
#print(all)
pattern1='[ABC]Vector=\"(.*?)\"'
vectors=re.findall(pattern1,all)
vector_s=[]
for i in vectors:
    vector_s.append([float(j) for j in i.split(',')])
    #da=map(float,i.split(','))
   # print(da)
print(vector_s)

#<Atom3d ID="5" Mapping="66" Parent="2" RestrictedBy="63" RestrictedProperties="FractionalXYZ" Name="CU" UserID="1" DisplayStyle="Ball and Stick" XYZ="0.542901465225596,0.129693970968716,0.187707788215709" Connections="25,45,26,46" Components="Cu"/>
pattern2="<Atom3d(.*?)XYZ=\"(.*?)\".*?Components=\"(.*?)\""
atom_info=re.findall(pattern2,all)
atoms=[]
for i in atom_info:
    if "RestrictedProperties" in i[0]:
        restricted=True
        print("他被固定住了")
    else:
        print("他没有被固定住了")
        restricted=False
    atoms.append((i[-1],i[1],restricted))
print(atoms)

element=[i[0] for i in atoms]
print(element)
element_s=set(element)
def mysorted(i):
    return element.index(i)
element_s=sorted(element_s,key=mysorted)
element_num=[]
for i in element_s:
    element_num.append(element.count(i))
print(element_num)


with open("POSCAR.bak",'w') as writer:
    writer.write("By nxu\n")
    writer.write("1.0\n")
    for i in vector_s:
        writer.write("%7.3f %7.3f %7.3f\n" %(i[0],i[1],i[2]))
    s=''
    for i in element_s:
        s=s+i+' '
    writer.write("%s\n" %(s))
    
    s=''
    for i in element_num:
        s=s+str(i)+' '
    writer.write("%s\n" %(s))
    
    writer.write("Selective\n")
    writer.write("Direct\n")
    
    for i in atoms:
        if i[2] == False:
            suffix=" T T T"
        else:
            suffix=" F F F"
        tmp=[float(j) for j in i[1].split(',')]
        writer.write("%7.3f %7.3f %7.3f %s\n" %(tmp[0],tmp[1],tmp[2],suffix))
        
