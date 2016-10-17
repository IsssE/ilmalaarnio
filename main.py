# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt
import json
import time

class Connection:
	def __init__(self, broker_ip, baddr = ""):
		self._ip = broker_ip
		self.client = mqtt.Client(protocol=mqtt.MQTTv31)
			
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message	

		self.client.connect(broker_ip)
		self.client.subscribe("team6_read", 2)

		self.messages = []
	#		self.client.loop_forever()

	def on_connect(self, client, userdata, flags, rc):
		print ("Connected with result code "+str(rc))
		self.client.subscribe("team6_read")	

	def on_subscribe(self, client, userfata, mid, granted_qos):
		print("Subscribed")
	def on_message(self, client, userdata, msg):
		self.messages.append(msg.payload)
		if len(self.messages) > 100:
			self.messages.pop(0)

	def send(self, m1, m2, m_up, time, command_id=0):
		#print("{\"m1\": \"%d\", \"m2\":\"%d\", \"m_up\":\"%d\", \"time\":\"%d\", \"command_id\":\"%d\"}" %(m1, m2, m_up, time, command_id))
		self.client.publish("team6_write", payload = "{\"m1\": \"%d\", \"m2\":\"%d\", \"m_up\":\"%d\", \"time\":\"%d\", \"command_id\":\"%d\"}" %(m1, m2, m_up, time, command_id))


	def get(self):
		try:
			return self.messages.pop()
		except:
			return None


class Copter:
	def __init__(self, conn, control=40):
		self.conn = conn
		self.m_up = 1 		#ascent motor: default speed
		self.x_control = control

	def horizontal(x):
		if (x > self.x_control):
			self.conn.send(2,1, 2, 30)
			time.sleep(0.5)
		elif (x < (self.x_control * -1)):
			self.conn.send(1,2, 2, 30)
			time.sleep(0.5)




conn = Connection("54.93.150.126")
cop = Copter(conn)

#conn.send(0, 0, 1, 50)
while True:
	#conn.client.loop(timeout=1.0)
	entry = json.load(conn.get())
	Copter.horizontal(entry.x)

	#conn.send(0, 0, 2, 170)
	#time.sleep(2)
