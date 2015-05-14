import MySQLdb
db = MySQLdb.connect("localhost","root","","wordvals" )
cursor = db.cursor()
fo = open('positive.txt', 'r')
posList = fo.read().split()
for word in posList:
	
	try:
		sql = r"INSERT INTO words (word, value) VALUES ('"+word+"',1)" 
		print sql
		cursor.execute(sql)
		db.commit()
	except Exception, e:
		db.rollback(); print e
db.close()
