import board
import busio
import adafruit_apds9960.apds9960
import time

import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

from subprocess import Popen, call

# proximity/color/gesture sensor setup
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_proximity = True
sensor.enable_gesture = True

# Uncomment and set the rotation if depending on how your sensor is mounted.
sensor.rotation = 90 # 270 for CLUE


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    rotation=270, # need this for landscape
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
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

def disp_img(img_path):
    image2 = Image.open(img_path)
    image_ratio = image2.width / image2.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image2.width * height // image2.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image2.height * width // image2.width
    image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image2 = image2.crop((x, y, x + width, y + height))
    disp.image(image2)


# import icon font of car indicators
icon_font = ImageFont.truetype("car_indicator.ttf", 100)
# icons
windshield_icon = chr(59392)
(wind_width, wind_height) = icon_font.getsize(windshield_icon)
floor_icon = chr(59393)
(floor_width, floor_height) = icon_font.getsize(floor_icon)
front_icon = chr(59395)
(front_width, front_height) = icon_font.getsize(front_icon)


# Fan is initally off
ON = False

# AC is initially off
AC = False

# windshield vent is initially off
WIND = False

# floor vent is initially off
FLOOR = False


# draw icon on tft screen
def disp_front():
    draw.text(
            (width // 4 * 3- front_width // 2,
                height // 2 - front_height // 2
            ),
            front_icon,
            font=icon_font,
            fill=(255, 255, 255))
def disp_floor():
    draw.text(
            (width // 4 * 3- floor_width // 2,
                height // 2 - floor_height // 2
            ),
            floor_icon,
            font=icon_font,
            fill=(255, 255, 255))
def disp_wind():
    draw.text(
            (width // 4 - wind_width // 2,
                height // 2 - wind_height // 2
            ),
            windshield_icon,
            font=icon_font,
            fill=(255, 255, 255))

# display background color
def disp_red():
    draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
def disp_blue():
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 255))
def disp_black():
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

while True:
    # gesture detection
    gesture = sensor.gesture()
    if gesture == 1:
        print("up")
        if ON: # only change windshield vent when fan is on
            if WIND:
                WIND = False
                disp_blue() if AC else disp_red()
                disp_floor() if FLOOR else disp_front()
                disp.image(image)
                print("\tWizard: press 'Airflow direction' button to switch to front\n")
                call(f"espeak -s125 'Shutting down windshield vent'", shell=True)
            else:
                WIND = True
                disp_wind()
                disp.image(image)
                print("\tWizard: press 'Airflow direction' button to switch to back\n")
                call(f"espeak -s125 'Turning on windshield vent'", shell=True)
    elif gesture == 2:
        print("down")
        if ON: # only change floor vent when fan is on
            if FLOOR:
                FLOOR = False
                disp_blue() if AC else disp_red()
                disp_front()
                if WIND:
                    disp_wind()
                disp.image(image)
                print("\tWizard: switch off 'Purify' button\n")
                call(f"espeak -s125 'Shutting down floor vent'", shell=True)
            else:
                FLOOR = True
                disp_blue() if AC else disp_red()
                disp_floor()
                if WIND:
                    disp_wind()
                disp.image(image)
                print("\tWizard: switch on 'Purify' button\n")
                call(f"espeak -s125 'Turning on floor vent'", shell=True)
    elif gesture == 3:
        print("left")
        # call(f"espeak -s125 'waving left'", shell=True)
        if ON:
            ON = False;
            disp_black()
            disp.image(image)
            print("\tWizard: turn switch off\n")
            call(f"espeak -s125 'Shutting down the fan'", shell=True)
        else:
            ON = True;
            disp_blue() if AC else disp_red()
            disp_floor() if FLOOR else disp_front()
            if WIND:
                disp_wind()
            disp.image(image)
            print("\tWizard: turn switch on\n")
            call(f"espeak -s125 'Turning on the fan'", shell=True)
    elif gesture == 4:
        print("right")
        # call(f"espeak -s125 'waving right'", shell=True)
        if ON: # only change AC when fan is on
            if AC:
                AC = False;
                disp_red()
                disp_floor() if FLOOR else disp_front()
                if WIND:
                    disp_wind()
                disp.image(image)
                print("\tWizard: switch off 'Humidify' button\n")
                call(f"espeak -s125 'AC mode is off'", shell=True)
            else:
                AC = True;
                disp_blue()
                disp_floor() if FLOOR else disp_front()
                if WIND:
                    disp_wind()
                disp.image(image)
                print("\tWizard: switch on 'Humidify' button\n")
                call(f"espeak -s125 'AC mode is on'", shell=True)
    # time.sleep(0.5)