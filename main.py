# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt
import json
import time

import connection


class Copter:
	def __init__(self, conn, control=40):
		self.conn = conn
		self.m_up = 1 		#ascent motor: default speed
		self.x_control = control

	def horizontal(self, x):
		#print(x)
		if (x > self.x_control):
			print(str(x) + " suurempi " + str(self.x_control))
			self.conn.send(2,1, 2, 30)
			time.sleep(0.5)
		elif (x < (self.x_control * -1)):
			print(str(x) < str(self.x_control * -1))
			self.conn.send(1,2, 2, 30)
			time.sleep(0.5)




conn = Connection("54.93.150.126")
cop = Copter(conn)

time.sleep(1)
conn.send(1, 1, 0, 50)
parameters = (0, 0, 0, 0)
while True:
	command = raw_input("Komento:")
	if command.lower() == "right":
		parameters = (1, 0, 2, 50, 1)

	#conn.client.loop(timeout=1.0)
	entry = json.load(conn.get())
	copter.horizontal(entry.x)

	conn.client.loop()
	entry = conn.get()
	#print(entry)
	if entry:
		pass
		#print (entry)
		#json_entry = json.loads(entry)
		#print(json_entry)
		#cop.horizontal(json_entry['x'])

	#conn.send(0, 0, 2, 170)
	#time.sleep(2)
