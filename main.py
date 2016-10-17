# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt
import json
import time

class Connection:
	def __init__(self, broker_ip, baddr = ""):
		self._ip = broker_ip
		self.client = mqtt.Client(protocol="MQTTv31")

		def on_connect(client, userdata, flags, rc):
			print ("Connected with result code "+str(rc))
			self.client.subscribe("$SYS/#")	

			
		self.client.on_connect = on_connect
		self.on_message = self.on_message	

		self.client.connect(broker_ip)
		self.client.subscribe("team6_read")

		self.messages = []
		self.client.loop(2)


	def on_message(self, client, userdata, msg):
		self.messages.append(msg)
		print(msg)
		if len(self.messages) > 5:
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
	def __init__(self):
		self.m_up = 1 		#ascent motor: default speed


conn = Connection("54.93.150.126")
conn.send(0, 0, 3, 150)
