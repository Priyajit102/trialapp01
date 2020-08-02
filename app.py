from flask import Flask,render_template,url_for,request,redirect,session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host='remotemysql.com',user="b5l0CiGJb2",password="FShP3SWVKl",database="b5l0CiGJb2")
cursor=conn.cursor()

@app.route('/')
def login():
    return render_template('home.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    file = request.form.get('inputfile')

    cursor.execute("""INSERT INTO `file` (`file`) VALUES
    ('{}')""".format(file))
    conn.commit()
    return "<h3>File Upload Done<h3>"


if __name__=="__main__":
    app.run(debug=True)
