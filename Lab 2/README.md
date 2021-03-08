# The Clock of Pi

Does it feel like time is moving strangely during the pandemic?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Wednesday.

### Get your kit
If you are overseas, you should have already ordered your parts.

If you are remote but in the US, the teaching team mailed parts last week.

If you are in New York, you can pick up your parts. If you have not picked up your parts by class you should come to Tata 351.

### Set up your Lab 2

1. [Pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Spring/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub. (This may have to be done again at the start of lab on Wednesday.)

In terminal cd into your Interactive-Lab-Hub folder and run 

```
Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
Interactive-Lab-Hub $ git pull upstream Spring2021
Interactive-Lab-Hub $ git add .
Interactive-Lab-Hub $ git commit -m'merge'
Interactive-Lab-Hub $ git push
```

Your local and remote should now be up to date with the most recent files.

2. Go to the [lab prep page](prep.md) to inventory your parts and set up your Pi.


## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
## Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once there create a Python environment.

```
ssh pi@ixe00
pi@ixe00:~ $ virtualenv circuitpython
pi@ixe00:~ $ source circuitpython/bin/activate
(circuitpython) pi@ixe00:~ $ 

```

## Part B. 
### Try out the Command Line Clock
Clone the repo for this assignment

```
(circuitpython) pi@ixe00:~$ git clone https://github.com/YOURGITID/Interactive-Lab-Hub.git
(circuitpython) pi@ixe00:~$ cd Interactive-Lab-Hub/Lab\ 2/
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub $ 
```

Install the packages from the requirements.txt and run the example

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub $ pip install -r requirements.txt
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```
you can press `ctrl-c` to exit.
If you're unfamiliar with the Python code in `cli_clock.py` have a look at [this Python refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you're still concerned, please reach out to the teaching staff!


## Part C. 
## Set up your RGB Display
We will introduce you to the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) and Python on the Pi.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware

From your kit take out the display and the [Raspberry Pi 4](https://www.adafruit.com/product/4296 | width=200)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

#### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

We can test it by typing 
```
python screen_test.py
```

You can type the name of a color then press either of the buttons to see what happens on the display. Take a look at the code with
```
cat screen_test.py
```

#### Displaying Info
You can look in `stats.py` for how to display text on the screen

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?

I modified `image.py` and saved it as `image-new.py` in this folder to make it switch to another image `pikachu.png` when push either one of the buttons. The demo is as below:

![image-switch-vid.GIF](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%202/image-switch-vid.GIF)


## Part D. 
## Set up the Display Clock Demo

In `screen_clock.py`. Show the time by filling in the while loop. You can use the code in `cli_clock.py` and `stats.py` to figure this out.

Please check `screen_clock.py` for the code. The demo is as below:

![screen-clock-setup.GIF](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%202/screen-clock-setup.GIF)

## Part E.
## Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

**A copy of your code should be in your Lab 2 Github repo.**

Time in seconds is centered on the screen. Information of weather, location, temperature, and time in minutes are shown in the screen when push the top button. If the top button is released, this information page will still be showing on the screen for 3 seconds before the "Time in seconds" page is shown again.

I referred to the tutorial [Raspberry Pi E-Ink Weather Station using Python](https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python) By [M. LeBlanc-Williams](https://learn.adafruit.com/users/MakerMelissa) for acquiring and showing information of weather, location and temperature, and referred to `screen_test.py` for using the buttons.

Codes are in files `modified_clock.py`, `weather_graphics.py`, and `meteocons.ttf`.

Run the following command in terminal to get my clock working:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab\ 2 $ python modified_clock.py 
```


you can push to your personal github repo by adding the files here, commiting and pushing.

```
git add .
git commit -m'your message here'
git push
```

After that, git will ask you to login to your github account to upload.

## Part F. 
## Make a short video of your modified barebones PiClock

**Take a video of your PiClock.**
[![Video of PiClock](https://img.youtube.com/vi/Qh0kQEShWUY/maxresdefault.jpg)](https://youtu.be/Qh0kQEShWUY)

(click the pic above to watch the video)

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

For Part 2, I'm thinking to add two features by using the bottom button solely and by using both bottom and top buttons. One of the feature may be a stopwatch or world clock. The other feature may be a torch (flashlight) for use in emergency.

## Prep for Part 2

1. Pick up remaining parts for kit.

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 

**Documentation**

In this part of the lab, the clock is modified to an astrology clock that give one's horoscope of the day based on user input of his/her birthday. Time in seconds is centered on the main screen when no buttons are pressed, with one's Zodiac sign decided from user input. 

*Press top button*: Information of weather, location, temperature, and time in minutes are shown in the screen. If the top button is released, this information page will still be showing on the screen for 3 seconds before the "Time in seconds" page is shown again.

*Press bottom button:* Horoscope of the day is shown for this Zodiac sign, with lucky number, lucky time, lucky color, mood, and compatible sign listed. The main screen is shown when bottom button is released.

*Press both buttons:* Description of the day for this Zodiac sign, with the color of text changing in seconds. 

I referred to the tutorial [Raspberry Pi E-Ink Weather Station using Python](https://learn.adafruit.com/raspberry-pi-e-ink-weather-station-using-python) by [M. LeBlanc-Williams](https://learn.adafruit.com/users/MakerMelissa) for acquiring and showing information of weather, location and temperature, and referred to `screen_test.py` for using the buttons. The horoscope and description of the day is acquired from [PyAztro](https://github.com/sameerkumar18/pyaztro), a client library of [aztro - The astrology API](https://github.com/sameerkumar18/aztro) by [Sameer Kumar](https://sameerkumar.website/). The background images for the horoscope screen are in the folder `zodiac_sign` and made by myself modifying [this picture](https://dribbble.com/shots/7307789-Zodiac-Signs).

Codes are in files `modified_clock_part2.py`, `weather_graphics.py`, and `meteocons.ttf`, and images are in the folder `zodiac_sign`.

If you haven't downloaded the [PyAztro API](https://github.com/sameerkumar18/pyaztro), please run the following command in terminal:
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab\ 2 $ pip install pyaztro
```

Run the following command in terminal to get my clock working:
```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab\ 2 $ python modified_clock_part2.py 
```

[![Video of PiClock for Part 2](https://img.youtube.com/vi/eMoMnk90PgU/maxresdefault.jpg)](https://youtu.be/eMoMnk90PgU)

(click the pic above to watch the video)
