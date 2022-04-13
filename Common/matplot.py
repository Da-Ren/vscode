import matplotlib.pyplot as plt   # 引入pyplot 模块   
import numpy as np     # 引入numpy 库   
data = np.loadtxt("BAND-REFORMATTED.dat")  #加载成列表
for i in range(1,data.shape[1]):   #取列数，从第一列开始取一直到最后一列。
	plt.plot(data[:,0],data[:,i])  
plt.ylim(-15,10)   #显示区间数
plt.xlabel('Kpath')
plt.ylabel('Energy E-Efermi')
plt.title("band figure")
plt.show()