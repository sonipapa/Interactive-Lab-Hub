# Ph-UI!!!

For lab this week, we focus on the prototyping the physical look and feel of the device. _Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

1. Pull the new Github Repo.
2. Readings: 

* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)

* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 

* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 

* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.

* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 

<img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > Dyson Vacuum cardboard prototypes


### For lab, you will need:

1. Cardboard (start collecting those shipping boxes!)
1. Cutting board
1. Cutting tools
1. Markers
1. Found objects and materials--like bananas--we're not saying that to be funny.


### Deliverables for this lab are: 
1. Sketches/photos of device designs
1. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.
3. "Works like" prototypes: show us what the device can do
4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device
5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


## Overview
Here are the parts of the assignment

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. 

Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

### Part A
### Capacitive Sensing, a.k.a. Human Banana Interaction

We wanted to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we were able to provide. At boot it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes it considers it a user touch. You can attach any conductive material. In your kit you have conductive fabric and copper tape that will work well, but don't limit yourself! In this lab we will use (go?) bananas!

<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
<img src="https://post.healthline.com/wp-content/uploads/2020/08/banana-pink-background-thumb-1-732x549.jpg" height="150">
</p>

Plug in the capacitive sensor board with the qwiic connector. Connect your banana's with either the copper tape or the alligator clips (the clips work better). make sure to install the requirements from `requirements.txt`

![](https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg?width=1518&height=1139)

I've connected my banana's* to pads 6 and 10. When you run the code and touch a banana the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Banana 10 touched!
Banana 6 touched!
```

*\*Some students have noted that their banana's look noticeably different from the ones presented in this demo. We firmly reject the accusation that these are not in fact banana's but Twizzlers™. Due to the challenges of remote teaching we cannot debug banana's at this time. We suggest you bring these issues up with the university or your local produce representative*

[![Video of part A](https://img.youtube.com/vi/Dysq62ehmmI/maxresdefault.jpg)](https://youtu.be/Dysq62ehmmI)
(click the pic above to watch the video)

### Part B
### OLED screen

We just received some of the small oled screens that we had coped to include in your kit. If you want one feel free to pop into the lab and get one. These don't have colors like the one on the pi but you can move it around on a cable making for more flexible interface design. The way you program this display is almost identical to the pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>

[![Video of part B](https://img.youtube.com/vi/lP0snvOK2e8/maxresdefault.jpg)](https://youtu.be/lP0snvOK2e8)
(click the pic above to watch the video)

### Part C
### Paper Display

Here is an Pi with a paper faceplate on it to turn it into a display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but it can be a bit difficult to lay out a great and user friendly display within the constraints of the Pi. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

It holds a pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>


Make a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**a. Document the design for your paper display.** (e.g. if you had to make it again from scratch, what information would you need?). Include interim iterations (or at least tell us about them).

I designed a portable paper piano when user touches a certain key, a certain tone is played. This is designed for the Lingling's who are so talented in playing instruments and wanted to practice their piano skill every where (as we all know you can't carry piano like a violin)! It's like a real piano but the keys are flatted and it is made of paper. A capacitive sensor, copper wires, a speaker, and a rapsberry pi were needed for the electronis. Masking tape, cardboards, paper, double-sided tape, insulating tape, cutting knife, and a cutting board were needed for physically propotyping the piano.

***(The images I uploaded somehow crashed for me. If it happens to you too, please check [this google drive folder](https://drive.google.com/drive/folders/1krwctjXZJhLVgY-BcdrsWGKO2w6qXC7N?usp=sharing) for the images below.)***

![prototype.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/prototype.JPG)

A huge cardboard was trimmed, folded and taped (using double-sided tape) as shown in the image below.

![partc_tape.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/partc_tape.JPG)

The dimension of the cardboard box was **300mm x 125mm x 100mm** (W x D x H).

![partc_dimension_w](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/partc_dimension_w.JPG)

![partc_dimension_d](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/partc_dimension_d.JPG)

![partc_dimension_h](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/partc_dimension_h.JPG)

The top board is not taped or glued, but instead fixed by inserting the side boards (attached to the top) to the two slits on the bottom. This way, I could make adjustment to the electronics hidden inside the box easily, by opening the top from unassembly the side boards.

![partc_slidein](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/partc_slidein.JPG)

The electronics are connected as below. Since I'm outside of US, so I used copper wire to connect to the capacitive sensor instead of copper tape.

![elements](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/elements.JPG)

Insulating tape was needed to wrap around the copper wires to prevent overlapping of the wires & hence shortening the circuit or interfering the actual interaction.

![insulating_tape.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/insulating_tape.JPG)

The 12 wires from 0 to 11 are taped using masking tape onto the keyboard indicating the 12 keys from C to B. The wires and the paper keyboard were mounted/fixed onto the top board using tapes.

![box_open_inner_taped.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/box_open_inner_taped.JPG)

The propotype is now ready to work on, by insert the side boards back into the slits.

![box_assembly.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/box_assembly.JPG)

**b. Make a video of your paper display in action.**

Here, I didn't actually use the speaker to play sound because this is just the initial design of the prototype appearance. Instead, I just have the screen showing which key is touched. Will update the sound functionality in part 2.

[![Video of part C](https://img.youtube.com/vi/ePudRjJ30OQ/maxresdefault.jpg)](https://youtu.be/ePudRjJ30OQ)
(click the pic above to watch the video)

**c. Explain the rationale for the design.** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

The design has to resemble a piano, at least for the keys, because it meant to be played by people like a real piano. However, the keyboard was design to be flat because it is a paper piano and meant to be portable. The dimension was set to be 300mm x 125mm x 100mm in order to hold all the electrical components (especially the speaker is quite big) with a minimized size.

### Part D
### Materiality

**Open Ended**: We are putting very few constraints on this part but we want you to get creative.

Design a system with the Pi and anything from your kit with a focus on form, and materiality. The "stuff" that enclose the system should be informed by the desired interaction. What would a computer made of rocks be like? How would an ipod made of grass behave? Would a roomba made of gold clean your floor any differently?

The system is my design in part C - the portable paper piano.

**a. document the material prototype.** Include candidates that were considered even if they were set aside later.

When trying to connect the capacitive sensor to the key, I first tried to use the alligator clips to have one side clip on the sensor and one on the key for the user to interact with. I then tried to fold aluminum foil to be a thin thread, having one side wrapping around the holes of the sensor and on side taped to the keys. In the end, the copper wire just worked perfect.

Cardboard and medium-hard plastics (like the plastic of a binder) were both considered as candidates for the outer box.

**b. explain the selection.**
The alligator clips didn't work out as the they are just way too huge in size. Aluminum foil is just too brittle that it breaks easily which does not fulfill the requirement of the durability of a portable piano. The copper wire, on the other hand, provided ideal durability and conductivity, but it just needed insulating tapes to prevent from short circuiting.

Cardboard wins out medium-hard plastics because cardboard is easier to cut, fold and taped, while plastics is sometimes too smooth to be taped.

### Part 2.

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design.

Reiterating:
### Deliverables for this lab are: 
1. Sketches/photos of device designs

**Prototype design:**

![prototype.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/prototype.JPG)

**Electronics:**

![box_open_inner_taped.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/box_open_inner_taped.JPG)

**Details of the keys:**

![detail.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/detail.JPG)

2. "Looks like" prototypes: show us what how the device should look, feel, sit, weigh, etc.

The device should look that it is made of cardboard because it's a paper piano. It would feel like paper when you touch the outer box & the keys. The size is relatively small (**300mm x 125mm x 100mm** - W x D x H) for it to be portable.

**width:**

![dimension_width.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/dimension_width.JPG)

**depth:**

![dimension_depth.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/dimension_depth.JPG)

**height:**

![dimension_height.jpg](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%204/dimension_height.JPG)

However, it shouldn't feel too light, because it needs hold some not-so-light electrical components like a speaker. The users could put it on a counter, on a desk, or even on their laps, so that they could practice piano everywhere they want.

3. "Works like" prototypes: show us what the device can do

The device incorporates a capacitive sensor and a speaker. When someone (an alive person who conducts electricity) touches a key, which is connected to one of the keys on the capacitive sensor, a pitch/sound corresponds to that key will be played by the speaker as if a real piano is played.

4. "Acts like" prototypes: videos/storyboards/other means of showing how a person would interact with the device

Please check the vid below for "Acts like".

[![Video of part 2](https://img.youtube.com/vi/bCh29VXPYm4/maxresdefault.jpg)](https://youtu.be/bCh29VXPYm4)
(click the pic above to watch the video)


5. Submit these in the lab 4 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same for each person in the group.


