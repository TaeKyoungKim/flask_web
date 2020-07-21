import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='myflaskapp')
cursor = db.cursor()
# sql = ''' 
#         CREATE TABLE users(
#             id INT(11) AUTO_INCREMENT PRIMARY KEY, 
#             name VARCHAR(100),
#             email VARCHAR(100),
#             username VARCHAR(30),
#             password VARCHAR(100),
#             register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
#             ENGINE=InnoDB DEFAULT CHARSET=utf8;
#     '''

sql=''' 
    CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''
cursor.execute(sql)
db.commit()
db.close()