import paho.mqtt.client as mqtt
import json
import time

import connection

conn = connection.Connection("54.93.150.126")
#cop = Copter(conn)

#time.sleep(1)
while True:
	conn.send(0, 0, 2, 30)
	time.sleep(0.2)
	conn.send(0, 0, 1, 30)
	time.sleep(0.2)
	
