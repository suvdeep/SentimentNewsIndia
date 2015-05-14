import re
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
import MySQLdb
db = MySQLdb.connect("localhost","root","","news" )
cursor = db.cursor()
id=1
while id < 1001 :
	sql = 	r"SELECT * FROM  `links` WHERE id = "+str(id)
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		text = BeautifulSoup(row[4]).prettify()
		splat = text.split()
		l= len(splat)
		query = 'UPDATE links SET totWords = %d Where id = %d' % (l,id)
		cursor.execute(query); db.commit()
	id +=1
