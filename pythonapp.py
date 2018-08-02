from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from contextlib import closing
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'bucketlist_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Yahoo101'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = '10.138.0.7'
mysql.init_app(app)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
	#read the values coming from UI
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            # All Good, let's call the MySQL
            with closing(mysql.connect()) as conn:
                with closing(conn.cursor()) as cursor:
                    _hashed_password = generate_password_hash(_password)
                    cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
                    data = cursor.fetchall()

                    if len(data) is 0:
                        conn.commit()
                        return json.dumps({'message':'User created successfully !'})
                    else:
                        return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=80)
