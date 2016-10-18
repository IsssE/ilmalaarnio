import paho.mqtt.client as mqtt
import json
import time

import connection

conn = connection.Connection("54.93.150.126")
#cop = Copter(conn)

#time.sleep(1)
t = time.clock()

direction = 0
while True:
	current_time = time.clock()

	if (current_time - time > 10):
		direction = 1
	conn.send(1+ direction, 1+ direction, 2, 100)
	time.sleep(100)
	#conn.send(0, 0, 1, 30)
	#time.sleep(0.2)
	
