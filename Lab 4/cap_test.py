import time
import board
import busio
import vlc


import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

keys = ["C","#C","D","#D","E","F","#F","G","#G","A","#A","B"]

while True:
	for i in range(12):
		filepath = "/home/pi/Interactive-Lab-Hub/Lab 4/"+keys[i]+".mp3"
		p = vlc.MediaPlayer(filepath)
		if mpr121[i].value:
			p.play()
			print(f"{keys[i]} touched!")
		else:
			p.stop()
	time.sleep(0.75)  # Small delay to keep from spamming output messages.