# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt
import json
import time

import connection
import copter

conn = connection.Connection("54.93.150.126")
cop = copter.Copter(conn)

while True:
	conn.loop()
	print (conn.get())
	time.sleep(0.5)
	cop.fix_horizon_direction(20)
