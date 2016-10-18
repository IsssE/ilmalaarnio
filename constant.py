import paho.mqtt.client as mqtt
import json
import time

import connection

conn = Connection("54.93.150.126")
cop = Copter(conn)

#time.sleep(1)
while True:
	conn.send(0, 0, 2, 100)
	time.sleep(1)
