import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('flask/database.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS ALERTS")
 
# Creating table
table = """ CREATE TABLE ALERTS (
            Header TEXT NOT NULL,
            Body TEXT NOT NULL,
            Type Text
        ); """
 
cursor_obj.execute(table)
 
print("Table is Ready")
 
# Close the connection
connection_obj.close()