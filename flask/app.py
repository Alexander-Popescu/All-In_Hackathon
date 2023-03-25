from flask import Flask, request, render_template, redirect
from email.message import EmailMessage
import ssl
import smtplib
import sqlite3
from twilio.rest import Client
import keys

#twilio stuff
client = Client(keys.account_sid, keys.auth_token)

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    data = cursor.execute("select * from ALERTS")
    entries = []
    for entry in data:
        entries.append(entry)
    entries.reverse()
    return render_template('index.html', entries=entries)
    
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

        return redirect("/")
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

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{header}', '{body}', 'info')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        #send messages to phone and email
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("select * from CONTACTS")
        entries = []
        for entry in data:
            entries.append(entry)

        for entry in entries:#loop over everyone in the contact list
            #send email via Gmail
            em = EmailMessage()
            em['From'] = keys.email_sender
            em['To'] = entry[0] #entry email
            em.set_content(body)

            #secure connection
            context = ssl.create_default_context()

            #login and send email using gmail server
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(keys.email_sender, keys.email_password)
                smtp.sendmail(keys.email_sender, entry[0], em.as_string())
        return redirect("/")
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

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{header}', '{body}', 'warning')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        #send messages to phone and email
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("select * from CONTACTS WHERE Helper=1 ")
        entries = []
        for entry in data:
            entries.append(entry)

        for entry in entries:#loop over everyone in the contact list
            #send SMS via twilio
            message = client.messages.create(
                body=f"{header} {body}",
                from_=keys.twilio_number,
                to=f"+{entry[1]}"
            )
            #send email via Gmail
            em = EmailMessage()
            em['From'] = keys.email_sender
            em['To'] = entry[0] #entry email
            em.set_content(body)

            #secure connection
            context = ssl.create_default_context()

            #login and send email using gmail server
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(keys.email_sender, keys.email_password)
                smtp.sendmail(keys.email_sender, entry[0], em.as_string())
        return redirect("/")
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

            cursor.execute(f"INSERT INTO ALERTS VALUES ('{header}', '{body}', 'danger')")
            sqliteConnection.commit()
            print("Record inserted successfully into ALERTS table ", cursor.rowcount)
            cursor.close()

        #except sqlite3.Error as error:
            #print("Failed to insert data into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
        
        #send messages to phone and email
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        data = cursor.execute("select * from CONTACTS")
        entries = []
        for entry in data:
            entries.append(entry)

        for entry in entries:#loop over everyone in the contact list
            #send SMS via twilio
            message = client.messages.create(
                body=f"{header} {body}",
                from_=keys.twilio_number,
                to=f"+{entry[1]}"
            )
            #send email via Gmail
            em = EmailMessage()
            em['From'] = keys.email_sender
            em['To'] = entry[0] #entry email
            em.set_content(body)

            #secure connection
            context = ssl.create_default_context()

            #login and send email using gmail server
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(keys.email_sender, keys.email_password)
                smtp.sendmail(keys.email_sender, entry[0], em.as_string())

        print(message.body)
        return redirect("/")
    else:
        return render_template('emergency.html', content='Hello World')

if __name__ == "__main__":
    app.run(debug=True)