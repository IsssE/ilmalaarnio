# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt

class Connection:
	def __init__(self, broker_ip, baddr = ""):
		self._ip = broker_ip
		self.client = mqtt.Client(protocol="MQTTv31")

		self.client.on_connect = self.on_connect
		self.on_message = self.on_message

		self.client.connect(broker_ip)

	def on_connect(self, client, userdata, flags, rc):
		print ("Connected with result code "+str(rc))
		self.client.subscribe("$SYS/#")


	def on_message(self, client, userdata, msg):
		print (msg.topic+" "+str(msg.payload))

	def send(self, m1, m2, m_up, time, command_id=0):
		print("{\"m1\": \"%d\", \"m2\":\"%d\", \"m_up\":\"%d\", \"time\":\"%d\", \"command_id\":\"%d\"}" %(m1, m2, m_up, time, command_id))
		self.client.publish("team6_write", payload = "{\"m1\": \"%d\", \"m2\":\"%d\", \"m_up\":\"%d\", \"time\":\"%d\", \"command_id\":\"%d\"}" %(m1, m2, m_up, time, command_id))

conn = Connection("54.93.150.126")
conn.send(0, 0, 3, 150)
