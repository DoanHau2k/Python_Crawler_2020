import requests #send http request
from bs4 import BeautifulSoup #Support html parser
baseurl = 'https://www.bachhoaxanh.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'#using linux and chrome
}

# productDetailList=[]#contain detail of product
# productLinks=[]#contain link of product take from producLinks
# file=open("productLinks.txt",'r')
# lines = file.readlines()
# for line in lines:
# 	link=line.replace("\n","/")
# 	productLinks.append(link)
# file.close()

# for item in productLinks:
r=requests.get('https://www.bachhoaxanh.com/binh-giu-nhiet/binh-giu-nhiet-inox-500ml-dien-may-xanh-ynqe-3011')
soup=BeautifulSoup(r.content,'lxml')
name=soup.find('h1',class_='nameproduct').text.strip()
price=int(soup.find('div',class_='boxprice').text.strip().replace('₫','').replace('.',''))

imgTab=soup.find('img',class_='owl-lazy')
imgTabTemp=repr(imgTab)
imgLink=imgTabTemp.partition('data-src="')[2].partition('"')[0]#take image source

moreInforTab=soup.find('ul',class_='infoproduct nospeci')
moreInforTemp=repr(moreInforTab).replace('</span>','').replace('<span>','').replace('<ul class="infoproduct nospeci">','').replace('</li>','').replace('<li>','')
moreInforTemp=moreInforTemp.replace('</div>','').replace('<div>','').replace('</ul>','').replace('\n\n','')#take more infor genaral infor

# print(name)
# print(price)
# print(imgLink)
#print(moreInforTemp)
product={
	'name':name,
	'price':price,
	'moreInforTemp':moreInforTemp
}
print(product)

