import RPi.GPIO as GPIO
import signal
import time
import board
import busio
from subprocess import Popen, call


import paho.mqtt.client as mqtt
import uuid

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buttonPin_R = 18
buttonPin_G = 23

GPIO.setup(buttonPin_R, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(buttonPin_G, GPIO.IN, GPIO.PUD_UP)

i2c = busio.I2C(board.SCL, board.SDA)

send_topic = 'IDD/foodserv/button'
read_topic = 'IDD/foodserv/food'


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
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# client.loop_forever()

while True:
	client.loop()
	if GPIO.input(buttonPin_R) == 1:
		buttonSts = 'Do not touch my food'
		client.publish(send_topic, buttonSts)
		# call(f"espeak -s125 '{buttonSts}'", shell=True)
	if GPIO.input(buttonPin_G) == 1:
		buttonSts = 'Go ahead and enjoy it'
		client.publish(send_topic, buttonSts)
		# call(f"espeak -s125 '{buttonSts}'", shell=True)
