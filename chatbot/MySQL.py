import mysql.connector

try:

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    auth_plugin='mysql_native_password',
    port=3307
  )

except mysql.connector.Error as error:
  print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (mydb.is_connected()):
        mydb.close()
        print("MySQL connection is closed")