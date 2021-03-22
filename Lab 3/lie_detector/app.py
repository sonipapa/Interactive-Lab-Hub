import eventlet
eventlet.monkey_patch()

from flask import Flask, Response,render_template, jsonify
from flask_socketio import SocketIO, send, emit
from subprocess import Popen, call

import time
import board
import busio
import adafruit_mpu6050
import json
import socket

import signal
import sys
from queue import Queue

import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
import webcolors
import urllib.request
import urllib.parse
import textwrap
import random

import RPi.GPIO as GPIO

#button
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buttonPin = 18

GPIO.setup(buttonPin, GPIO.IN, GPIO.PUD_UP)

# while 1:
#     if GPIO.input(buttonPin) == 1:
#         time.sleep(0.02)
#         if(GPIO.input(buttonPin)==1):
#             while(GPIO.input(buttonPin) == 1):
#                 pass
#             print('key press')

 
i2c = busio.I2C(board.SCL, board.SDA)
# mpu = adafruit_mpu6050.MPU6050(i2c)


cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    rotation=90,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

if display.rotation % 180 == 90:
    height = display.width  # we swap height/width to rotate it to landscape!
    width = display.height
else:
    width = display.width  # we swap height/width to rotate it to landscape!
    height = display.height


redColor = (255, 0, 0) #red
greenColor = (85,200,85) #green
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

def greeting_disp():
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    Greeting = "Don't you dare"
    Greeting2 = "lie to me!"
    x = 35
    y = height //2 -30
    draw.text((x,y), Greeting, font=font, fill=(255, 255, 255))
    x = 70
    y += font.getsize(Greeting)[1]
    draw.text((x,y), Greeting2, font=font, fill=(255, 255, 255))
    display.image(image)

greeting_disp()

def result_disp(lie):
    if lie:
        thisColor = redColor
        Text = "You are lying!"
        Text2 = "Electric Shock..."
        x = 45
        x2 = 30
    else:
        thisColor = greenColor
        Text = "You are honest :)"
        Text2 = "Applause for you..."
        x = 30
        x2 = 20
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=thisColor)
    y = height //2 -30
    draw.text((x,y), Text, font=font, fill=(255, 255, 255))
    y += font.getsize(Text)[1]
    draw.text((x2,y), Text2, font=font, fill=(255, 255, 255))
    display.image(image)




# hostname = socket.gethostname()
hostname = '192.168.31.240' # I have the pi name not set to ixe00, so I need to set it manually here
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)
audio_stream = Popen("/usr/bin/cvlc alsa://"+hardware+" --sout='#transcode{vcodec=none,acodec=mp3,ab=256,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}' --no-sout-all --sout-keep", shell=True)

@socketio.on('speak')
def handel_speak(val):
    call(f"espeak -s125 '{val}'", shell=True)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('tft-display')
def tft_display(lie):
    result_disp(lie)
    time.sleep(3)
    greeting_disp()

@socketio.on('question')
def question_disp(question):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=(255, 255, 255))
    Question = textwrap.wrap(question, width=18)
    x = 10
    y = 10
    for i in Question:
        draw.text((x,y), i, font=font, fill=(0,0,0))
        y += 25
        # draw.text((x,y), Description, font=font, fill="#FFFFFF")
    display.image(image)

# @socketio.on('pressBtn')
# def press_button():
# 	if (GPIO.input(buttonPin) == 1):
# 		time.sleep(0.02)
# 		if(GPIO.input(buttonPin)==1):
# 			while(GPIO.input(buttonPin) == 1):
# 				pass
# 				print('button press')
# 	else:
# 		pass

# @socketio.on('ping-gps')
# def handle_message(val):
#     # print(mpu.acceleration)
#     emit('pong-gps', mpu.acceleration) 


# this route only handle the rendering of index.html
@app.route("/")
def index():
   return render_template('index.html',hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    audio_stream.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# this route handling the request send to the /update url
@app.route("/update")
def update():
	# Read Sensors Status
	if GPIO.input(buttonPin) == 1:
		buttonSts = 'Button is pressed!'
	else:
		buttonSts = ''
	templateData = {'title':'GPIO input Status!','button': buttonSts}
	return jsonify(templateData),200

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)


