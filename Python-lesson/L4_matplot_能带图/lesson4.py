import matplotlib.pyplot as plt   # 引入pyplot 模块   
import numpy as np     # 引入numpy 库  

with open("KLABELS",'r') as reader: #从KLABELS 读进来
	all_ = reader.readlines()   #readlines 是 全部读取进来放在一个列表里面,每一行作为list的一个元素，并且每行末含有换行符\n。
klabel_s = []  #创建空列表
kpath_coord = []

for i in all_[1:]:  #按列表里面的元素，逐个打印，变成多行列表。
	tmp = i.split()
	if len(tmp) < 2:  #如果某一行的列数小于2就截止
		break
	else:
		klabel_s.append(tmp[0])      #把tmp的第一个元素增加（append）到上面所创建的空列表里面。
		kpath_coord.append(float(tmp[1]))  #把第二列数字转变为浮点数，并添加到空列表里面。
print(klabel_s,kpath_coord)

data = np.loadtxt("BAND-REFORMATTED.dat")  #加载成列表
for i in range(1,data.shape[1]):   #取列数，从第一列开始取一直到最后一列。
	plt.plot(data[:,0],data[:,i])  
plt.ylim(-15,10)   #显示区间数
plt.xlim(min(kpath_coord),max(kpath_coord))   #设置x的取值范围。
plt.xlabel('Kpath')
plt.ylabel('Energy E-Efermi')
plt.title("band figure")  
plt.xticks(kpath_coord,klabel_s)  #人为在哪些点设置标签  
plt.axhline(y=0, xmin=0, xmax=1 , linestyle="--", color="grey") #位置在y=0的位置。
# 需要在高对称点上加一个竖线，通过迭代的方式进行。
for i in kpath_coord[1:-1]:  #[1:-1]不需要在第一个位置和最后一个位置添加Gamma
	plt.axvline(x=i, ymin=0, ymax=1 , linestyle="--", color="grey")
	print(i)
plt.savefig("band.figure.png",dipi=300)
plt.show()