# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt
import json
import time


import connection
import copter

conn = connection.Connection("54.93.150.126")
cop = copter.Copter(conn)

time_ = time.clock()
control = time_ + 500

while True:
	conn.loop()
	
	if time > control:
		cop.fix_horizon_direction(50)
		time_ = time.clock()
		control = time_ + 500
