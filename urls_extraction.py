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
#startingLink = 'http://www.thehindu.com/topics/?categoryId='+categoryId+'&articleType=news'
countries=['413','1979','281','371','258']

 
def main():
	for id in countries:
		categoryId = id # U S A http://www.thehindu.com/Topics/?categoryId=413&pageNo=2
		try:
			i=1
			while i < 11 :
				sourceCode = opener.open ('http://www.thehindu.com/topics/?categoryId='+categoryId+'&pageNo='+ str(i)).read()
				#print sourceCode + "\n\n\n"+ "########################################################################################"
				urlNews = re.findall(r'<h2><a href="(.*?)" title="Updated: (.*?) at', sourceCode, re.S)
				for link in urlNews:
					try:
					   	# Execute the SQL command
					   	sql = r"INSERT INTO links(countryId, url, date) VALUES ('"+id+"','"+link[0]+"','"+link[1]+"')"
					   	cursor.execute(sql)
					   	# Commit your changes in the database
					   	db.commit()
					except:
					# Rollback in case there is any error
						db.rollback(); print 'Rollback'
					# disconnect from server
				print 'Updated in database\n '
				i +=1
				time.sleep(5)
		
		except Exception, e:
			print str(e)
			print 'error in the main try'
			time.sleep(555)               
	db.close()
main()