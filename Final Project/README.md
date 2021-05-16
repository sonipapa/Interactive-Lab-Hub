# Final Project

Using the tools and techniques you learned in this class, design, prototype and test an interactive device.

Project Github page set up - May 3

Functional check-off - May 10
 
Final Project Presentations (video watch party) - May 12

Final Project Documentation due - May 19



## Objective

The goal of this final project is for you to have a fully functioning and well-designed interactive device of your own design.
 
## Description

Project: **AC Gesture Control in a Car**

## Deliverables

### Documentation of design process

As someone who drives nearly everyday, the countless buttons that all look the same on the central control panel really make my daily driving an adventure. I (also almost anyone I know who drives) always need to switch attention from driving to look for the right button to control the AC or the radio, and this is dangerous especially when driving at night or high speed. If drivers were able to control the AC using hand gestures, they then wouldn't need to look at the control buttons to use the desired function. Voice control is widely used in modern-day cars (i.e. Tesla), but it is actually not convenient enough to use non-mechatronic controls while driving, and voice control is also not friendly to people with hearing loss.

Hence, I proposed this AC Gesture Control System for Cars in which the users (drivers) could control the AC with hand gestures and get both visual and audio feedback of users' actions.

The system was determined to use a raspberry pi, an APDS9960 proximity/gesture/color sensor, a speaker, and a pi tft screen. The proximity/gesture/color sensor was chosen because it could sense at least 4 hand gestures (waving up, down, left, and right). The speaker was needed for audio output and the screen for visual output considering people with hearing loss. They were connected as below for the inital design.

![connenction](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/connection.jpg)

I first tested the APDS9960 sensor's gesture sensing feature using [this instruction](https://learn.adafruit.com/adafruit-apds9960-breakout/circuitpython) and the sensing of 4 gestures generally worked great.

The functions controlled by the gestures were determined to be as follows:

* Left: the fan
 
* Right: AC mode
 
* Up: windshield vent
 
* Down: floor vent
 
Everytime a certain gesture is sensed, the corresponding funtion will be turned on or off. For example, if currently the fan is on, waving left would turn the fan off. It was also designed that if the fan is off, other functions will not be controllable, in line with how a real car AC works.

Afterwards, I added the audio output announcing which function is turned on or off for each gesture. 

The visual output was designed lastly:

* Background color:
 
  * Red - Fan on, AC off
  * Blue - Fan on, AC on
  * Black - Fan off
  
* Icons:
  * ![wind](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/wind.png) - windshield vent on
  * ![floor](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/floor.png) - floor vent on
  * ![front](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/front.png) - front vent on (always on)

![wind](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/wind.png) Icons made by [Freepik](https://www.freepik.com) from [www.flaticon.com](https://www.flaticon.com/)

![floor](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/floor.png) ![floor](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/front.png) Icons made by [Those Icons](https://www.flaticon.com/authors/those-icons) from [www.flaticon.com](https://www.flaticon.com/)


### Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

**Prototype**:

The final prototype consist a raspberry pi, an APDS9960 sensor, a speaker, a pi tft screen and a Dyson electric fan that is remotely controllable. A wizard controls the electric fan as the AC in car, because I could not demo this in a car (no internet connection in my car).

The raspberry pi, the APDS9960 sensor, the speaker and the pi tft screen are connected as shown in the picture earlier. 

The prototype was made of cardboard and is of the shape of a triangular prism. The length of the final prototype is about 50 cm and the edge length of the trangle side is about 15 cm. I cut the cardboard as so and folded along the yellow dotted line as shown in the picture below. Holes were cutted at where circled red. The buttom part was taped onto the top part to fix the folded cardboard.

![cardboard.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/cardboard.jpg)

The two "ears" on each triangle were inserted into the holes. This allows me to make adjustment to the electronics hidden inside the box easily, by opening the triangular side from pulling the ears out.

![cardboard_insert.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/cardboard_insert.jpg)

The Pi, speaker and wires were hiddent inside of this cardboard prism, while the pi tft screen sticked out from the rectangular hole and the gesture sensor was fixed on the outside of the prototype.

![prototype_dashboard](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/prototype_dashboard.png)

The inside looks like this:

![inner.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/inner.jpg)

The sensor was mounted by a twist tie going through the two holes and twisted in the back.

![sensor_mounting](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/sensor_mounting.jpg)

The entire setup for user interaction is as below:

![driver](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/driver.png)

The wizard should be in another room. A `Dyson Link` app needs to be downloaded on the wizard's phone and it has to connect the Dyson electric fan. The terminal window of running `gesture.py`should be on and monitored by the wizard. Everytime the user performs a hand gesture, his/her action and the corresponding action that wizard is supposed to do would be printed in the terminal window. The wizard should perform the printed action (press certain buttons in the Dyson Link app) everytime he/she sees a change in the terminal window.

Dyson link app UI:

<img src="https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/wizard_app.jpg" width="300">

Sample terminal prints:

<img src="https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/terminal.png">

Wizard setup:
![wizard](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/wizard.png)


**Interaction**:

The interaction design didn't change much from the initial design. Only the electric fan was added to mimic real AC output.

Functions controlled by the gestures:

* Left: the fan
 
* Right: AC mode
 
* Up: windshield vent
 
* Down: floor vent
 
Everytime a certain gesture is sensed, the corresponding funtion will be turned on or off. If the fan is off, other functions will not be controllable.

Audio output announces which function is turned on or off for each gesture:

* Left:
  * "Turning on the fan"
  * "Shutting down the fan"
 
* Right:
  * "AC mode is on"
  * "AC mode is off"
 
* Up:
  * "Turning on windshield vent"
  * "Shutting down windshield vent"
 
* Down:
  * "Turning on floor vent"
  * "Shutting down floor vent"

Tft screen display:

* Background color:
 
  * Red - Fan on, AC off
  * Blue - Fan on, AC on
  * Black - Fan off
  
* Icons:
  * ![wind](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/wind.png) - windshield vent on
  * ![floor](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/floor.png) - floor vent on
  * ![front](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/front.png) - front vent on (always on)

Example display:

<img src="https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/red.jpg" width="150"> AC off, windshield vent off, floor vent off

<img src="https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/blue.jpg" width="150"> AC on, windshield vent off, floor vent off

<img src="https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Final%20Project/imgs/icon.jpg" width="150"> AC on, windshield vent on, floor vent on

Wizard control the fan:

* Left:
  * "Turning on the fan" -> Wizard: turn switch on
  * "Shutting down the fan" -> Wizard: turn switch off
 
* Right:
  * "AC mode is on" -> Wizard: turn switch on
  * "AC mode is off" -> Wizard: turn switch off
 
* Up:
  * "Turning on windshield vent" -> Wizard: press 'Airflow direction' button to switch to back
  * "Shutting down windshield vent" -> Wizard: press 'Airflow direction' button to switch to front
 
* Down:
  * "Turning on floor vent" -> Wizard: switch on 'Humidify' button
  * "Shutting down floor vent" -> Wizard: switch off 'Humidify' button

**Coding**:

The system is ready to use by running the file `gesture.py`. I changed the rotation angle of the sensor to be 90 degrees because of the way I mounted it. I also change the rotation angle of the tft screen display to be 270, because I put the pi with the pins side being down.

`car_indicator.ttf` is the font book for the icons displayed on the screen.

### Video of someone using your project (or as safe a version of that as can be managed given social distancing)

[![Video demo](https://img.youtube.com/vi/IOoE608VBzU/maxresdefault.jpg)](https://youtu.be/IOoE608VBzU)
(click to view the vid)

### Reflections on process (What have you learned or wish you knew at the start?)

* The gesture sensor was hard to use. Sometimes it's not sensitive, but sometimes it's oversensitive. I invited my mom to use this system but she couldn't let the sensor sense her desired gesture at the beginning. When she wanted to turn the fan on by waving left, the sensor didn't sense anything. When she wanted to turn the AC on by waving right, the system turn the windshield vent on because it sensed her gesture as waving up. In the end, my mom managed to control the system and she told me the trick. The user has to wave slowly and cannot start his/her hand motion right on top of the sensor, because the sensor tracks the change of light to distinguish gestures. I think a better sensor would have made the system much more user-friendly.
* It's impossible to display an vector image with background colors using pi tft screen. I tried to display the icons by displaying their vector images. However, no matter what I've tried, I could not display a background color under the vector image as I could do under text. In lab 2 when I was making a clock showing weather, I was able to display icons as text by importing a font file of icons. Therefore, I made a font file of the icons I downloaded from [www.flaticon.com](https://www.flaticon.com/) and imported it so that I could display icons as text. It made my life much easier upon designing the screen display with changing background colors.
* Since my sensor is not stemma qt compatible, I soldered the pins onto the sensor by myself. The pins were soldered on the front side for the sensing unit, which means the female tips of the jumper wires had to be inserted on the front of the sensor for connection. This made the propotype have wires shown on the surface. If I knew at the start, I would have soldered the pins on the back, so that the wires could be hidden inside.

## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)
This version of the class is very different, but it may be useful to see these.
