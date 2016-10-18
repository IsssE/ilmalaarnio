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
		#print (msg)
		self.messages.append(msg.payload)
		print (self.messages)
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
