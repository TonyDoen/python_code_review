# -*- coding:utf8 -*-
# Filename: ConvertData.py
# DB config
MongoDBHost='10.140.45.109'
MongoDBPort=9293
MongoDBDataBase='albatross_development'
MongoDBUser='development'
MongoDBPassword='development123'

MySQLHost='10.150.130.222'
MySQLPort=3983
MySQLDataBase='gis_stage_db'
MySQLUser='gis_stage_w'
MySQLPassword='YjRkYmY0NDUzNjk'

def getMongodbCon() :
	from pymongo import MongoClient
	moncon = MongoClient(MongoDBHost, MongoDBPort)
	mondb = moncon[MongoDBDataBase]
	mondb.authenticate(MongoDBUser, MongoDBPassword)
	return mondb

def getMySQLCon() :
	import MySQLdb
	myscon = MySQLdb.connect(host=MySQLHost, port=MySQLPort, db=MySQLDataBase, user=MySQLUser, passwd=MySQLPassword)
	return myscon, myscon.cursor()

def close(*src) :
	for s in src:
		s.close()

def getMysData(sql) :
	myscon, myscur = getMySQLCon()
	myscur.execute(sql)
	data = myscur.fetchall()
	close(myscur, myscon)
	return data

def convertData() :
	num = 1000
	i = 0
	data = getMysMoment(i, num)
	while data :
		# print 'has data'
		for d in data:
			convertMysDataToMongoJson(d)
		i = i+1
		data = getMysMoment(i, num)
	else :
		print 'no data'
	pass

def getMysMoment(index, limit) :
	sql = '''select id,
			lifeshow_id,
			uuid,
			user_id,
			bak_user_id,
			type,
			source,
			message,
			content_type,
			content_id,
			audit_status,
			publish_time,
			likes,
			longitude,
			latitude,
			location_name,
			reserved,
			reserved1,
			version,
			created_time,
			updated_time,
			created_by,
			reserved2,
			updated_by from tbl_moments order by id limit %d, %d ;''' % (index*limit, limit)
	# print sql
	return getMysData(sql)

def getMysImgIdArray(momentId) :
	sql = 'select image_id from tbl_join_moments_images where moment_id = %d ;' % momentId
	res = []
	# return getMysData(sql)
	data = getMysData(sql)
	for i in data :
		for j in i :
			res.append(j)
	return res

def createMongoMoment(json) :
	getMongodbCon().tbl_moments.insert(json)

def convertMysDataToMongoJson(data) :
	# print data
	momentId = data[0]
	lifeShowId = data[1]
	imageId = getMysImgIdArray(momentId)
	uuid = data[2]
	userId = data[3]
	bakUserId = data[4]
	mystype = data[5]
	source = data[6]
	message = data[7]
	contentType = data[8]
	contentId = data[9]
	auditStatus = data[10]
	publishTime = data[11]
	likes = data[12]
	longitude = data[13]
	latitude = data[14]
	locationName = data[15]
	bucketName = data[16]
	objectName = data[17]
	version = data[18]
	createTime = data[19]
	updateTime = data[20]
	res = {
		"_class" : "com.lesports.albatross.data.entity.MomentMongoEntity", 
	   	"momentId":momentId,
	    "lifeShowId":lifeShowId,
	    "imageId":imageId,
	    "uuid":uuid,
	    "userId":userId,
	    "bakUserId":bakUserId,
	    "type":mystype,
	    "source":source,
	    "message":message,
	    "contentType":contentType,
	    "contentId":contentId,
	    "auditStatus":auditStatus,
	    "publishTime":publishTime,
	    "likes":likes,
	    "longitude":longitude,
	    "latitude":latitude,
	    "locationName":locationName,
	    "bucketName":bucketName,
	    "objectName":objectName,
	    "currentLoginedUserId" : "false", 
	    "version" : version, 
    	"createTime" : createTime, 
    	"updateTime" : updateTime
	}
	print res
	createMongoMoment(res)

if __name__ == '__main__' :
    # print 'hello'
    convertData()