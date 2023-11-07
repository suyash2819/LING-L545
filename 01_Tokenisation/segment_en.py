
file=open("segmentation.txt","r")
while(True):
	line=file.readline()
	for text in line.strip().split(' '):
		if(not text):
			continue
		if(text[-1] in '!?'):
			line=line.replace(text[-1],text[-1]+'\n')
		elif(text[-1] == '.'):
			if text in ['etc.','e.g.','i.e.']:
				line=line.replace(text[-1],text[-1]+' ')
			else:
				line=line.replace(text[-1],text[-1]+'\n')
	print(line)
	if(""==line):
		break
file.close()





