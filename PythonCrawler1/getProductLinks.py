import requests #send http request
from bs4 import BeautifulSoup #Support html parser
baseurl = 'https://www.bachhoaxanh.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'#using linux and chrome
}

cateLinks=[]
file1=open("categoriesLinks/categoriesLinks.txt",'r')
lines = file1.readlines()
for line in lines:
	link=line.replace("\n","/")
	cateLinks.append(link)
file1.close()


productLinks=[] #link to all product still need to fix because a page may have many layer, this only take one layer
for item in cateLinks:
	r=requests.get(item)
	soup=BeautifulSoup(r.content,'lxml')
	productList=soup.find_all('li',class_='hideExpired product hasNotUnit')#List of products
	for item in productList:
		for link in item.find_all('a',href=True):
			productLinks.append(baseurl+link['href'])



#Save product Link to file txt
file=open("productLinks/productLinks.txt",'a')
file.truncate(0)
for item in productLinks:
	file.write(repr(item).replace("'",""))
	file.write("\n")
file.close()