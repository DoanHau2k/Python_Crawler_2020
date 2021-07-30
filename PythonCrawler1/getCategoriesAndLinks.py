import requests #send http request
from bs4 import BeautifulSoup #Support html parser

baseurl = 'https://www.bachhoaxanh.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 RuxitSynthetic/1.0 v9262709690 t38550 ath9b965f92 altpub cvcv=2'#using linux
}

r=requests.get('https://www.bachhoaxanh.com/')
soup=BeautifulSoup(r.content,'lxml')
categoriesList=soup.find_all('a',class_='link-hover menu-haschild')#List of categories
#print(categoriesList[1])

categoriesLinks=[]
for item in categoriesList:
	# print(item)
	textTemp=repr(item)
	href=textTemp.partition('href="/')[2].partition('">')[0]
	name=textTemp.partition('">')[2]
	categoriesLinks.append(baseurl+href)
#finish get link to the each categories


#Save categories Link to file txt
file1=open("categoriesLinks/categoriesLinks.txt",'a')
file1.truncate(0)
for item in categoriesLinks:
	file1.write(repr(item).replace("'",""))
	#if (item!=categoriesLinks[-1] ):
	file1.write("\n")
file1.close


