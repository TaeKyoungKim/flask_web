import pymysql

db = pymysql.connect(
    host='localhost', 
    port=3306, 
    user='root', 
    passwd='1234', 
    db='myflaskapp')
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

# sql=''' 
#     CREATE TABLE `topic` (
# 	`id` int(11) NOT NULL AUTO_INCREMENT,
# 	`title` varchar(100) NOT NULL,
# 	`body` text NOT NULL,
# 	`author` varchar(30) NOT NULL,
#     `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# 	PRIMARY KEY (id)
# 	) ENGINE=innoDB DEFAULT CHARSET=utf8;
# '''
# cursor.execute(sql)
# db.commit()
# db.close()

sql_1 = 'SELECT name , email FROM users;'
sql_2=  '''
        INSERT INTO users(name, email , username, password) 
        VALUES ('PARK' ,'4@naver.com', 'PARK', '1234');
            '''

# cursor.execute(sql_2)
# db.commit()
# db.close()
# print(result)
# users = cursor.fetchall()
# print(users[0][1])
# cursor.execute(sql_1)
# users = cursor.fetchall()
# print(users)

name = 'GANGNAM' 
email = '6@naver.com'
username = 'GANGNAM'
password = '1234'
sql_3=  '''
        INSERT INTO users(name, email , username, password) 
        VALUES (%s ,%s, %s,%s);
            '''

# cursor.execute(sql_3, (name, email , username, password))
# db.commit()
# db.close()

title='javascript'
body='프로토타입기반의 객체지향 프로그래밍 언어로, 스크립트 언어에 해당된다. 특수한 목적이 아닌 이상 모든 웹 브라우저에 인터프리터가 내장되어 있다. 오늘날 HTML, CSS와 함께 웹을 구성하는 요소 중 하나다. HTML이 웹 페이지의 기본 구조를 담당하고, CSS가 디자인을 담당한다면 JavaScript는 클라이언트 단에서 웹 페이지가 동작하는 것을 담당한다.'
author='Gary'
sql_7=  '''
        INSERT INTO topic(title, body , author) 
        VALUES (%s ,%s, %s);
            '''
# cursor.execute(sql_7 ,(title, body , author ) )
# db.commit()
# db.close()



sql_4='DELETE FROM `users` WHERE  `id`=5;'
# cursor.execute(sql_4)
# db.commit()
# db.close()

sql_5='DELETE FROM users WHERE name="SONG";'
# cursor.execute(sql_5)
# db.commit()
# db.close()

sql_6='UPDATE `users` SET `name`="PARK" WHERE  `id`=6;'
# cursor.execute(sql_6)
# db.commit()
# db.close()


sql_8 = 'SELECT * FROM topic;'

if __name__ == '__main__':
    cursor.execute(sql_8)
    topics = cursor.fetchall()
    print(topics)