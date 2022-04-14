file1 = open("new0.dat",'r')
all_data = file1.read()   
file1.seek(0)  #文件指针移到前面位置
all_data_lines = file1.readlines()
all_data_dos=all_data.split("\n\n") # print(all_data.split("\n"))只是把一行进行分割，我们需要前面一段和后面一段进行分割
all_lines = []   #建立一个总列表。
for i in all_data_dos:
	each_line=[]  #新建空的列表存放每一行的数据
	if i.strip("\n") != '':  # 最后空格还有换行符去掉，判断是不是空格，
		lines = i.split("\n") #
		for line in lines:    #对每条线，每一个数据点进行迭代，一个大列表。
			each_line.append(list(map(float,line.split())))   #以空格的方法进行切割,这样就每个数据点切割成 能量和后面的状态数。#在用list(map(float,列表_含有字符串)) 转化成浮点数    
		all_lines.append(each_line)  #前面的列表是第一条线，后面的列表是第二条线。已经把两条线的数据点已经切割开。
#print(len(all_lines))
for i in all_lines[1:]:   #对all_lines 进行迭代 ,第二条线的第二列态密度移到第一条线第二列能量的右侧，变为上半部分的第三列。 all_lines[1:] 代表除了第一条线数据外，其它更多的线和数据
	for index in range(len(i)):
		all_lines[0][index].append(i[index][1])   #对应第一条线上的行index，i[index][1]第i条线的第二列dos数据。
# 输出
with open("reform.dat",'w') as writer:   #对all_lines 每一行进行迭代，在把三个float值[-26.655, 0.0, 0.0]写在文件里
	for i in all_lines[0]:
		writer.write("%7.3f %7.3f %7.3f %7.3f\n " %(i[0],i[1],i[2],i[3]))   #wirte方法只接受字符串，写的时候要写入字符串，采用格式替代的方法。带3位小数。 