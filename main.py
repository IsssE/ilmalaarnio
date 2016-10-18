# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt
import json
import time

import connection
import copter

conn = connection.Connection("54.93.150.126")
cop = Copter(conn)

time.sleep(1)
#conn.send(1, 1, 0, 50)
parameters = (0, 0, 0, 0)
while True:
	command = raw_input("Komento:")
	if command.lower() == "a":
		parameters = (1, 2, 5, 20)
	elif command.lower() == "d":
		parameters = (2, 1, 5, 20)
	elif command.lower() == "w":
		parameters = (1, 1, 5, 50)
	elif command.lower() == "s":
		parameters = (2, 2, 5, 50)
	elif command.lower() == "e":
		parameters = (0, 0, 5, 100)
	elif command.lower() == "q":
		parameters = (0, 0, 0, 50)
	else:
		continue

	conn.send(parameters[0], parameters[1], parameters[2], parameters[3])

	#conn.client.loop(timeout=1.0)
	#entry = json.load(conn.get())
	#copter.horizontal(entry.x)

	#conn.client.loop()
	#entry = conn.get()
	#print(entry)
#	if entry:
#		pass
		#print (entry)
		#json_entry = json.loads(entry)
		#print(json_entry)
		#cop.horizontal(json_entry['x'])

	#conn.send(0, 0, 2, 170)
	#time.sleep(2)
