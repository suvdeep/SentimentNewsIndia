
import MySQLdb
db = MySQLdb.connect("localhost","root","","news" )
cursor = db.cursor()
sql = 	r"SELECT totWords FROM  `links` WHERE countryid = 258"
cursor.execute(sql)
results = cursor.fetchall()
count = 0
for row in results:
	count+= int(row[0])

print count
