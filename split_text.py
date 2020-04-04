total_num=17693010
current_num=0
with open('output.txt',encoding='utf-8') as f:
	for i in range(16):
		with open('output'+str(i)+'.txt','w',encoding='utf-8') as fw:
			while True:
				line=f.readline()
				fw.write(line)
				current_num+=1
				if line=='\n' and current_num>=(i+1)*total_num/16:
					break