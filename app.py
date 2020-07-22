from flask import Flask ,render_template , flash , redirect , url_for, session, request, logging

import pymysql
from data import Articles

app = Flask(__name__)
app.debug=True


db = pymysql.connect(host='localhost', 
                        port=3306, 
                        user='root', 
                        passwd='1234', 
                        db='myflaskapp')


#init mysql 
# mysql = MySQL(app)
# cur  = mysql.connection.cursor()
# result  = cur.execute("SELECT * FROM users;")

# users  = cur.fetchall()
# print(users)
# print(result)

@app.route('/')
def index():
    print("Success")
    # return "TEST"
    return render_template('home.html',hello="GaryKim")

@app.route('/about')
def about():
    print("Success")
    # return "TEST"
    return render_template('about.html',hello="GaryKim")

@app.route('/register',methods=['GET' ,'POST'])
def register():
    if request.method == 'POST':

        # data = request.body.get('author')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        username = request.form.get('username')
        # name = form.name.data
        if(password == re_password):
            print([name, email , password , re_password , username])
            cursor = db.cursor()
            sql = '''
                INSERT INTO users (name , email , username , password) 
                VALUES (%s ,%s, %s, %s )
             '''
            cursor.execute(sql , (name,email,username,password ))
            db.commit()
            

            # cursor = db.cursor()
            # cursor.execute('SELECT * FROM users;')
            # users = cursor.fetchall()
            
            return "register Success"

        else:
            return "Invalid Password"

        db.close()
    else:
        return render_template('register.html')



@app.route('/articles', methods=['GET','POST'])
def articles():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html',articles=articles)

@app.route('/test')
def show_image():
    return render_template('image.html')

@app.route('/article/<int:id>')
def article(id):
    print(id)
    articles= Articles()[id-1]
    print(articles)
    return render_template('article.html',data =articles)
    # return "Success"

if __name__ =='__main__':
    # app.run(host='0.0.0.0', port='8080')
    app.run()
    