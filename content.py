import re
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import MySQLdb
db = MySQLdb.connect("localhost","root","","news" )
cursor = db.cursor()
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
countries=['413','1979','281','371','258']
for id in countries:
	categoryId = id
	sql = 	r"SELECT * FROM  `links` WHERE countryId = "+str(id)
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		url = row[3]
		text = row[4]
		if text == "":
			newsCode = opener.open(url).read()
			news= re.findall(r'<p class="body">(.*?)</p>',newsCode, re.S)
			fullNews= '\n'.join(news); print fullNews
			sql= "UPDATE `links` SET `text` = CONCAT(`text`, '"+MySQLdb.escape_string(fullNews)+"') WHERE id =" + str(row[0])
			cursor.execute(sql)
			db.commit()
			print '---------------------'+str(row[0])+'----Article added to database-----------------------------\n'
			time.sleep(15)
		else :
			print '------------------------------Already Populated--------------------------------\n'
			pass

db.close()
