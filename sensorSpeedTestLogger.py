import speedtest
import json
import mysql.connector

threads = None
with open('config.JSON') as config_file:
    config = json.load(config_file)
data = {}
s = speedtest.Speedtest()

#Read config
database = config['database']
table = config['table']
table = config['table']
user = config['user']
password = config['password']

mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  passwd=password,
  database=database
)

#Read data
download = s.results.download
upload = s.results.upload
ping = s.results.ping

mycursor = mydb.cursor()

sql = "INSERT INTO " +table+ " (ping, upload, download, connectionTimeOut) VALUES (%s, %s, %s, %s)"
val = (ping, upload, download,False)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted. Download:", download," Upload:", upload, "Ping:", ping)
