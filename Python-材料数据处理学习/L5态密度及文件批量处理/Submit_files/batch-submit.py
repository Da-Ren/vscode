""" 
1.获取当前目录下所有的文件和文件夹的名称
2.将文件和文件夹分别筛选出来
3.对所有的文件夹迭代，将除了python脚本外的其它文件移动到文件夹中
4.切换工作目录，在每个文件夹中提交pbs任务。

"""
from distutils import filelist
import os # 引入os库
import shutil    #引入文件操作库
alllist = os.listdir(os.getcwd()) #列出当前目录下所有的文件和文件夹
dirlist = []  #用于存放所有的文件夹
filelist = []  #用于存放所有的文件
for i in alllist:
	if not os.path.isfile(i): #判断是否是文件
		dirlist.append(i)  #往dirlist空列表添加一个文件夹
	else:
		filelist.append(i) #往filelist空列表添加一个文件夹
for j in dirlist:     #对所有文件夹迭代
	for i in filelist:   #对所有文件迭代
		if "batch-submit.py" not in i:  #排除py脚本
			shutil.copy(i,os.path.join(os.getcwd(),j)) #将文件复制到j文件夹中,os.path.join是将os.getcwd() 当前路径和j文件夹进行拼接。
	os.chdir(os.path.join(os.getcwd(),j)) #先把当前目录和j子目录拼接起来，从而将工作目录切换到j文件夹
	#os.system("qsub vasp.pbs") #在j文件夹下提交pbs脚本
	os.chdir("..") #将工作目录切换到先前的目录，用于对下一个文件夹的操作
