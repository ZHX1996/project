import pymysql.cursors

connection = pymysql.connect(host='121.43.190.190',
                             port=3306,
                             user='root',
                             password='613b861c0c',
                             db='locationdata',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

conn = pymysql.connect(host='10.128.0.118',
                       port=3306,
                       user='root',
                       password='123456',
                       db='test',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

try:
    with connection.cursor() as cursor:
        sql = "select * from locationinfo"
        cursor.execute(sql)
        for row in cursor:
            id = str(row['id'])
            time = str(row['time'])
            longitude = str(row['longitude'])
            latitude = str(row['latitude'])
            sql01 = "INSERT INTO `test1` VALUES (%s, %s, %s, %s)"
            cur.execute(sql01, (id, time, longitude, latitude))
            conn.commit()
            print("insert %s success" % id)
            # print(type(id), type(time), type(longitude), type(latitude))
            # break
finally:
    cursor.close()
    cur.close()
    conn.close()
    connection.close()
