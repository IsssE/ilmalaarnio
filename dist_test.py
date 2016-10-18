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
	
	l = conn.get(20)
	correct = []
	if l:
#		print (l)
		for entry in l:
			json_entry = json.loads(entry)
			baddr = json_entry["baddr"]
#			print(baddr + "/" + "B6:DB:E8:66:C4:E1")
			if baddr == "B6:DB:E8:66:C4:E1":
				#print("JEE")
				correct.append(json_entry["rssi"])
		print (correct)
		if len(correct):
			print(max(correct))

	#time.sleep(0.5)
	#cop.fix_horizon_direction(20)
