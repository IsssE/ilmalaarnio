# -*- coding:UTF-8 -*-
import paho.mqtt.client as mqtt

class Connection:
	def __init__(broker_ip, baddr = ""):
		self._ip = broker_ip
		self.client = mqtt.Client(protocol=MQTTv31)
		self.client.on_connect = self.on_connect
		self.on_message = self.on_message

		client.connect(broker_ip)

	def on_connect(self, client, userdata, flags, rc):
		#called when connected
    	print("Connected with result code "+str(rc))
    	client.subscribe("$SYS/#")


	def on_message(self, client, userdata, msg):
    	print(msg.topic+" "+str(msg.payload))

conn = Connection("54.93.150.126")
