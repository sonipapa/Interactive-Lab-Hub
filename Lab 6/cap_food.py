import time
import board
import busio
import adafruit_mpr121

import RPi.GPIO as GPIO
import signal
import time
import board
import busio
from subprocess import Popen, call

import paho.mqtt.client as mqtt
import uuid

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

read_topic = 'IDD/foodserv/button'
send_topic = 'IDD/foodserv/food'


def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(read_topic)
	# you can subsribe to as many topics as you'd like
	# client.subscribe('some/other/topic')


# this is the callback that gets called each time a message is recived
def on_message(cleint, userdata, msg):
	message = msg.payload.decode('UTF-8')
	print(f"topic: {msg.topic} msg: {message}")
	call(f"espeak -s125 '{message}'", shell=True)

client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect('farlab.infosci.cornell.edu',port=8883)

# food_list = {0:'milk',1:'orange'}
food_list = ['orange', 'bread', 'chocolate', 'candy', 'cookie']

while True:
	for i in range(12):
		if mpr121[i].value:
			if i < len(food_list):
				food = food_list[i]
				val = f"" + food + " is touched!"
				# val = f"Banana {i} touched!"
				print(val)
				client.publish(send_topic, val)
	time.sleep(0.5)
client.loop_forever()
