
productLinks=[]#contain link of product take from producLinks
file=open('productLinks/productLinks.txt','r')
lines = file.readlines()
for line in lines:
	link=line.replace("\n","/")
	productLinks.append(link)
file.close()
def line_number(fileName):
	file=open(fileName,'r')
	lineNumber = file.readlines()
	file.close()
	return int(lineNumber[0])

fileName='productLinks/lineNumber.txt'
line_number(fileName)

#spilit file to many file if number of line in file greater 100
for x in range(1,10):
	file=open(f'productLinks/productLinks{x}.txt','w')
	start=1+(x-1)*100
	end=x*100
	if (end>line_number(fileName)):
		end=line_number(fileName)
	for i in range(start,end):
		file.write(repr(productLinks[i]).replace("'",""))
		file.write("\n")
	file.close()

