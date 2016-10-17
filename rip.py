import paho.mqtt.client as mqtt

def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    global message
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    message = msg.payload

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Connect
mqttc.connect("54.93.150.126", 1883,60)

# Start subscribe, with QoS level 0
mqttc.subscribe("team6_read", 0)

# Publish a message
#mqttc.publish("hello/world", "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
   rc = mqttc.loop()