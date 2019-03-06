import sqlite3

conn = sqlite3.connect('db.sqlite3')
print("Open database successfully")
c = conn.cursor()
c.execute('''PRAGMA FOREIGN_KEYS=ON;''')#打开外键,sqlite3默认关闭外键限制

c.execute('''create table admin
	(ID  txt primary key not null,
	NAME txt 			 not null,
	PASSWORD txt		 not null,
	TEL  txt			 not null,
	LEVEL INTEGER 		 not null);'''
	)
#管理员表: 用户ID(学号),姓名,密码,电话,等级(用于判定用户和管理员)
conn.commit()
print("create table admin successfully")

c = conn.cursor()
c.execute('''create table user
	(ID  txt primary key not null,
	NAME txt 			 not null,
	PASSWORD txt		 not null,
	TEL  txt			 not null,
	LEVEL INTEGER 		 not null);'''
	)
#用户表: 用户ID(学号),姓名,密码,电话,等级(用于判定用户和管理员)
conn.commit()
print("create table user successfully")

c = conn.cursor()
c.execute('''create table lostitem
	(ID  txt 			 not null,
	NAME txt 			 not null,
	TEL  txt 			 not null,
	LOSTTIME date                ,
	LOSTPLACE txt				 ,
	DETIAL txt					 ,
	IMAGE blob					 ,
	primary key(ID,NAME)
	);'''
	)
#丢失物品表: 用户ID(学号),物品名称,电话,丢失时间(可以无),丢失地点(可以无),细节描述(可以无),物品照片(可以无).
#主键约束(ID,NAME)
conn.commit()
print("create table lostitem successfully")

c = conn.cursor()
c.execute('''create table pickupitem
	(ID  txt 			 not null,
	NAME txt 			 not null,
	TEL  txt 			 not null,
	PICKUPTIME date              ,
	PICKUPPLACE txt				 ,
	DETIAL txt					 ,
	IMAGE blob					 ,
	primary key(ID,NAME) 
	);'''
	)
#拾获物品表: 用户ID(学号),物品名称,电话,拾获时间(可以无),拾获地点(可以无),细节描述(可以无),物品照片(可以无).
#主键约束(ID,NAME)
conn.commit()
print("create table pickupitem successfully")

conn.close()




