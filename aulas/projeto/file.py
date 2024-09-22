import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='python',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

cursor.execute('SHOW DATABASES')

for db in cursor:
    print(db)

