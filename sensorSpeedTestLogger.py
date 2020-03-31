import speedtest
import json
import mysql.connector
servers = []
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
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
#Read data
download = int(s.results.download/1000000)
upload = int(s.results.upload/1000000)
ping = s.results.ping

mycursor = mydb.cursor()

sql = "INSERT INTO " +table+ " (ping, upload, download, connectionTimeOut) VALUES (%s, %s, %s, %s)"
val = (ping, upload, download,False)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted. Download:", download," Upload:", upload, "Ping:", ping)
