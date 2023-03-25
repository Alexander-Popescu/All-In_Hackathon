from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        return render_template('index.html', content='Hello World')
    else:
        return render_template('index.html', content='Hello World')
    
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        data = request.form
        email = data["email"]
        phone_number = data["phone"]
        helper = 0
        try:
            if data["provide_help"] == 'on':
                helper = 1
        except Exception as e:
            print("no checkbox")
        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            print(email)
            print(phone_number)
            print(helper)

            cursor.execute(f"INSERT INTO CONTACTS VALUES ('{email}', '{phone_number}', {helper})")
            sqliteConnection.commit()
            print("Record inserted successfully into CONTACTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return render_template('index.html', content='Hello World')
    else:
        return render_template('add.html', content='Hello World')
    
@app.route('/notification', methods=['GET', 'POST'])
def notification():
    if request.method == "POST":
        data = request.form
        header = data["header"]
        body = data["body"]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            print(header)
            print(body)

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{header}', '{body}', 'notification')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        return render_template('index.html', content='Hello World')
    else:
        return render_template('notification.html', content='Hello World')

@app.route('/help_request', methods=['GET', 'POST'])
def help_request():
    if request.method == "POST":
        data = request.form
        header = data["header"]
        body = data["body"]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            print(header)
            print(body)

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{header}', '{body}', 'help_request')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        return render_template('index.html', content='Hello World')
    else:
        return render_template('help_request.html', content='Hello World')

@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == "POST":
        data = request.form
        header = data["header"]
        body = data["body"]

        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            print(header)
            print(body)

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{header}', '{body}', 'emergency')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        return render_template('index.html', content='Hello World')
        return render_template('index.html', content='Hello World')
    else:
        return render_template('emergency.html', content='Hello World')

if __name__ == "__main__":
    app.run(debug=True)