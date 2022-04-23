import paho.mqtt.client as mqtt

def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("sensor/light")
 
def on_disconnect(client, userdata, flag, rc):
    if rc != 0:
        print("Unexpected disconnection.") 
 
 
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print("Receive message ="+str(msg.payload)+" on topic = "+ msg.topic+ " with Qos "+str(msg.qos))
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
 
try:
    client.connect("192.168.11.8",1883,300)
except:
    print("broker host is not started!! waiting!!")
 
client.loop_forever()