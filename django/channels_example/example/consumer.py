from channels.sessions import channel_session
from channels import Group
import time
import json
import numpy as np
import cx_Oracle


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group("chat").add(message.reply_channel)


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def ws_receive(message):
	# conn = cx_Oracle.connect('system', '199621', '127.0.0.1:1521/new')
	# cursor = conn.cursor()

	# cursor.execute("select * from test where tim=(select max(tim) from test)")
	# query1 = cursor.fetchone()
	# cursor.execute("select * from test1 where tim=(select max(tim) from test1)")
	# query2 = cursor.fetchone()
	# cursor.execute("select * from test2 where tim=(select max(tim) from test2)")
	# query3 = cursor.fetchone()
	# cursor.execute("select * from test3 where tim=(select max(tim) from test3)")
	# query4 = cursor.fetchone()
	# cursor.execute("select * from test4 where tim=(select max(tim) from test4)")
	# query5 = cursor.fetchone()

	# m = {"time1": query1[1], "tem1": query1[2], "hum1": query1[3],"time2": query2[1], "tem2": query2[2], "hum2": query2[3],
		 # "time3": query3[1], "tem3": query3[2], "hum3": query3[3], "time4": query4[1], "tem4": query4[2], "hum4": query4[3],
		 # "time5": query5[1], "tem5": query5[2], "hum5": query5[3]}

	# cursor.close()
	# conn.close()

	# message = {"text": json.dumps(m)}
	# Group("chat").send(message)
	pass

# https://blog.csdn.net/jackieliuqihe/article/details/79457264
def ws_message(message):
	conn = cx_Oracle.connect('system', '199621', '127.0.0.1:1521/new')
	cursor = conn.cursor()

	cursor.execute("select * from test where tim=(select max(tim) from test)")
	query1 = cursor.fetchone()
	cursor.execute("select * from test1 where tim=(select max(tim) from test1)")
	query2 = cursor.fetchone()
	cursor.execute("select * from test2 where tim=(select max(tim) from test2)")
	query3 = cursor.fetchone()
	cursor.execute("select * from test3 where tim=(select max(tim) from test3)")
	query4 = cursor.fetchone()
	cursor.execute("select * from test4 where tim=(select max(tim) from test4)")
	query5 = cursor.fetchone()

	m = {"time1": query1[1], "tem1": query1[2], "hum1": query1[3],"time2": query2[1], "tem2": query2[2], "hum2": query2[3],
		 "time3": query3[1], "tem3": query3[2], "hum3": query3[3], "time4": query4[1], "tem4": query4[2], "hum4": query4[3],
		 "time5": query5[1], "tem5": query5[2], "hum5": query5[3]}

	cursor.close()
	conn.close()

	message = {"text": json.dumps(m)}
	Group("chat").send(message)

