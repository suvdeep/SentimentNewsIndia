import MySQLdb, time
db = MySQLdb.connect("localhost","root","","news" )
cursor = db.cursor()
positiveWords=[]
negativeWords=[]

def loadWordArrays():
	cursor.execute("SELECT word FROM words WHERE value = '-1'")
	for negRow in cursor.fetchall():
		#print negRow
		negativeWords.append(negRow[0])
	print 'negative words loaded \n '

	cursor.execute("SELECT word FROM words WHERE value = '1'")
	for posRow in cursor.fetchall():
		positiveWords.append(posRow[0])
	print 'positive Words loaded \n'

def testsent():
	i=1
	while i <=1000:
		newsSQL = r"SELECT  * FROM  `links` WHERE id =%d" % (i)
		cursor.execute(newsSQL)
		readNews=cursor.fetchall(); descriptives = readNews[0][5]
		posCounter = 0; posDesc =[]
		negCounter = 0; negDesc = []
		print '\n__________________________',i,'_______________________________\n '
		#print '\n\n',readNews[0][3],'\n'
		
		for eachPosword in positiveWords:
			if eachPosword in descriptives.lower().split(',') :
				posDesc.append(eachPosword)
				posCounter +=1;
				if eachPosword != '':
					cursor.execute("UPDATE links SET posWords = CONCAT(poswords , ' ', '%s') Where id = %d" % (eachPosword, i)); db.commit()
		
		cursor.execute("UPDATE links SET noPos = %d Where id = %d" % (posCounter, i)); db.commit()
		for eachNegword in negativeWords:			
			if eachNegword in descriptives.lower().split(','):
				negDesc.append(eachNegword)
				negCounter -=1;
				if eachNegword != '':
					cursor.execute("UPDATE links SET negWords = CONCAT(negwords , ' ', '%s') Where id = %d" % (eachNegword, i)); db.commit()
		cursor.execute("UPDATE links SET noNeg = %d Where id = %d" % (negCounter, i)); db.commit()
		
		total = posCounter + (negCounter); print '------',total,'----------'
		cursor.execute("UPDATE links SET sentWords = %d Where id = %d" % (total, i)); db.commit()
		i+=1
loadWordArrays()
testsent()
