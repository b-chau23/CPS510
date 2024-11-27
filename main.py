import oracledb
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import os

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']


try:
    connection = oracledb.connect(
        user=USERNAME,
        password=PASSWORD,
        dsn="(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle12c.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl12c)))"
    )
    # print("Successfully connected to Oracle Database")
    cursor = connection.cursor()

    actor_db_list = [row for row in cursor.execute("SELECT * FROM actor")]
    customer_db_list = [row for row in cursor.execute("SELECT * FROM customer")]
    membership_db_list = [row for row in cursor.execute("SELECT * FROM membership")]
    admin_db_list = [row for row in cursor.execute("SELECT * FROM admin")]
    payment_db_list = [row for row in cursor.execute('SELECT * FROM payment')]
    movie_db_list = [row for row in cursor.execute("SELECT * FROM movie")]
    account_db_list = [row for row in cursor.execute("SELECT * FROM account")]









    # cursor.execute("SELECT table_name FROM user_tables") THIS IS THE FORMAT

    # Close cursor and connection
    cursor.close()
    connection.close()

except oracledb.DatabaseError as e:
    print(f"Error: {str(e)}")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

## TIME to start putting shit in the UI

@app.route('/',methods=['GET','POST'])
def sign_in():
    if request.method =='POST':
        USERNAME = request.form['username']
        PASSWORD = request.form['password']

        for account in account_db_list:
            if account[1] == USERNAME and account[2] == PASSWORD:
                return redirect('home')

    return render_template('loginpage.html',account_db_list=account_db_list)

@app.route('/home')
def edit():
    return render_template('home.html',movie_db_list=movie_db_list)

@app.route('/movie')
def movie():

    return render_template('movie.html')




if __name__ == '__main__':
    app.run(debug=True)
