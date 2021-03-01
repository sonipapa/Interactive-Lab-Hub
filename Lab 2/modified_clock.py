import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import urllib.request
import urllib.parse
from weather_graphics import Weather_Graphics


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# You'll need to get a token from openweathermap.org, looks like:
# 'b6907d289e10d714a6e88b30761fae22'
OPEN_WEATHER_TOKEN = "931dae16f137756d5e04f172ff9e4c61"

# Use cityname, country code where countrycode is ISO3166 format.
# E.g. "New York, US" or "London, GB"
LOCATION = "Manhattan,US"
DATA_SOURCE_URL = "http://api.openweathermap.org/data/2.5/weather"

if len(OPEN_WEATHER_TOKEN) == 0:
    raise RuntimeError(
        "You need to set your token first. If you don't already have one, you can register for a free account at https://home.openweathermap.org/users/sign_up"
    )

# Set up where we'll be fetching data from
params = {"q": LOCATION, "appid": OPEN_WEATHER_TOKEN}
data_source = DATA_SOURCE_URL + "?" + urllib.parse.urlencode(params)


# Create the ST7789 display:
display = st7789.ST7789(
    spi,
    # rotation=90, # need this for landscape
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = display.width  # we swap height/width to rotate it to landscape!
width = display.height
image = Image.new("RGB", (width, height))
rotation=90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
display.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

gfx = Weather_Graphics(display, am_pm=True, celsius=False)
weather_refresh = None

while True:
    if buttonB.value and buttonA.value:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 
        Time_mdy = time.strftime("%m/%d/%Y")
        x = width // 2 - font.getsize(Time_mdy)[0] // 2
        y = height // 2 - font.getsize(Time_mdy)[1] // 2 - 10
        draw.text((x,y), Time_mdy, font=font, fill="#FFFFFF")
        Time_hms = time.strftime("%H:%M:%S")
        y = height // 2 - font.getsize(Time_mdy)[1] // 2 - 10+ font.getsize(Time_mdy)[1]
        draw.text((x,y), Time_hms, font=font, fill="#FFFFFF")

        # Display image.
        display.image(image,rotation)
        time.sleep(1)
    else:
        backlight.value = True
    if buttonB.value and not buttonA.value:
        # only query the weather every 10 minutes (and on first run)
        if (not weather_refresh) or (time.monotonic() - weather_refresh) > 600:
            response = urllib.request.urlopen(data_source)
            if response.getcode() == 200:
                value = response.read()
                print("Response is", value)
                gfx.display_weather(value)
                weather_refresh = time.monotonic()
            else:
                print("Unable to retrieve data at {}".format(url))

        gfx.update_time()
        time.sleep(3)  # wait 3 seconds before updating anything again

        

# while True:
#     # Draw a black filled box to clear the image.
#     draw.rectangle((0, 0, width, height), outline=0, fill=0)

#     #TODO: fill in here. You should be able to look in cli_clock.py and stats.py 
#     Time = time.strftime("%m/%d/%Y %H:%M:%S")
#     y = top
#     draw.text((x, y), Time, font=font, fill="#FFFFFF")

#     # Display image.
#     disp.image(image, rotation)
#     time.sleep(1)




# """
# This example queries the Open Weather Maps site API to find out the current
# weather for your location... and display it on a eInk Bonnet!
# """

# spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# ecs = digitalio.DigitalInOut(board.CE0)
# dc = digitalio.DigitalInOut(board.D22)
# rst = digitalio.DigitalInOut(board.D27)
# busy = digitalio.DigitalInOut(board.D17)

# # You'll need to get a token from openweathermap.org, looks like:
# # 'b6907d289e10d714a6e88b30761fae22'
# OPEN_WEATHER_TOKEN = ""

# # Use cityname, country code where countrycode is ISO3166 format.
# # E.g. "New York, US" or "London, GB"
# LOCATION = "Manhattan, US"
# DATA_SOURCE_URL = "http://api.openweathermap.org/data/2.5/weather"

# if len(OPEN_WEATHER_TOKEN) == 0:
#     raise RuntimeError(
#         "You need to set your token first. If you don't already have one, you can register for a free account at https://home.openweathermap.org/users/sign_up"
#     )

# # Set up where we'll be fetching data from
# params = {"q": LOCATION, "appid": OPEN_WEATHER_TOKEN}
# data_source = DATA_SOURCE_URL + "?" + urllib.parse.urlencode(params)

# # Initialize the Display
# display = Adafruit_SSD1675(
#     122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=None, rst_pin=rst, busy_pin=busy,
# )

# display.rotation = 1

# gfx = Weather_Graphics(display, am_pm=True, celsius=False)
# weather_refresh = None

# while True:
#     # only query the weather every 10 minutes (and on first run)
#     if (not weather_refresh) or (time.monotonic() - weather_refresh) > 600:
#         response = urllib.request.urlopen(data_source)
#         if response.getcode() == 200:
#             value = response.read()
#             print("Response is", value)
#             gfx.display_weather(value)
#             weather_refresh = time.monotonic()
#         else:
#             print("Unable to retrieve data at {}".format(url))

#     gfx.update_time()
#     time.sleep(300)  # wait 5 minutes before updating anything again
