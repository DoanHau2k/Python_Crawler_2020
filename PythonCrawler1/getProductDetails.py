import requests #send http request
import pymysql
from bs4 import BeautifulSoup #Support html parser
from transCategory import transCate
baseurl = 'https://www.bachhoaxanh.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'#using linux and chrome
}

productLinks=[]#contain link of product take from producLinks
file=open("productLinks/productLinks.txt",'r')
lines = file.readlines()
for line in lines:
	link=line.replace("\n","/")
	productLinks.append(link)
file.close()
i=0
for item in productLinks:
	r = requests.get(item)
	soup = BeautifulSoup(r.content,'lxml')
	try:
		price = int(soup.find('div',class_='boxprice').text.strip().replace('₫','').partition(' ')[0].replace('.',''))
		nameP = soup.find('h1',class_='nameproduct').text.strip()

		imgTab = soup.find('img',class_='owl-lazy')
		imgTabTemp = repr(imgTab)
		imgLink = imgTabTemp.partition('data-src="')[2].partition('"')[0]#take image source

		category=item.partition('.com//')[2].partition('/')[0]
		category=transCate(category)

		moreInforTab = soup.find('ul',class_='infoproduct nospeci')
		moreInforTemp = repr(moreInforTab).replace('</span>','').replace('<span>','').replace('<ul class="infoproduct nospeci">','').replace('</li>','').replace('<li>','')
		moreInforTemp = moreInforTemp.replace('</div>','').replace('<div>','').replace('</ul>','').replace('\n\n','')#take more infor genaral infor

		conn = pymysql.connect(host="localhost",user="root",passwd="",db="shopping3")
		myCursor = conn.cursor()

		sql=('INSERT INTO products (name, price, infor,img,category) VALUES (%s, %s, %s,%s,%s) ',(nameP, price, moreInforTemp,imgLink,category))
		myCursor.execute(*sql)
		conn.commit()
		conn.close()
		print(i)
		i=i+1
	except:
		continue





