import MySQLdb, time
db = MySQLdb.connect("localhost","root","","news" )
cursor = db.cursor()
newsSQL = r"SELECT  * FROM  `links` WHERE id =%d" % (3)
cursor.execute(newsSQL)
readNews=cursor.fetchall(); descriptives = readNews[0][5]
cursor.execute("SELECT word FROM words WHERE value = '-1'")
negativeWords=[]
for negRow in cursor.fetchall():
	negativeWords.append(negRow[0].lower())
print negativeWords

print '\n\n\n'
print descriptives.lower().split(',')