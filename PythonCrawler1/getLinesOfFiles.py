def count_number(fileName):
	file=open(fileName,'r')
	line_count = 0
	lines = file.readlines()
	for line in lines:
		if line != "\n":
			line_count+=1
	file.close()
	return line_count

def export_count_number(count_number,fileName):
	file=open(fileName,'a')
	file.truncate(0)
	file.write(repr(count_number))
	file.close()

categoriesFile='categoriesLinks/categoriesLinks.txt'
categoriesLineFile='categoriesLinks/lineNumber.txt'
export_count_number(count_number(categoriesFile),categoriesLineFile)

productFile='productLinks/productLinks.txt'
productLineFile='productLinks/lineNumber.txt'
export_count_number(count_number(productFile),productLineFile)


