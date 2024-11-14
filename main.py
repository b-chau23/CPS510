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

    movie_db_list = [row for row in cursor.execute("SELECT * FROM movie")]
    customer_db_list = [row for row in cursor.execute("SELECT * FROM customer")]
    membership_db_list = [row for row in cursor.execute("SELECT * FROM membership")]
    admin_db_list = [row for row in cursor.execute("SELECT * FROM admin")]
    payment_db_list = [row for row in cursor.execute('SELECT * FROM payment')]



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
@app.route('/home')
def edit():
    return render_template('home.html')

@app.route('/')
def sign_in():
    return render_template('sign.html')


if __name__ == '__main__':
    app.run(debug=True)
