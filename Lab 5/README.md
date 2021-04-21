# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

In Lab 5 part 1, we focus on detecting and sense-making.

In Lab 5 part 2, we'll incorporate interactive responses.


## Prep

1.  Pull the new Github Repo.
2.  Read about [OpenCV](https://opencv.org/about/).
3.  Read Belloti, et al's [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf)

### For the lab, you will need:

1. Raspberry Pi
1. Raspberry Pi Camera (2.1)
1. Microphone (if you want speech or sound input)
1. Webcam (if you want to be able to locate the camera more flexibly than the Pi Camera)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.


## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

Befor you get started connect the RaspberryPi Camera V2. [The Pi hut has a great explanation on how to do that](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera).  

#### OpenCV
A more traditional to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python.

Additionally, we also included 4 standard OpenCV examples. These examples include contour(blob) detection, face detection with the ``Haarcascade``, flow detection(a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (I.e. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example.

```shell
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

**contours-detection**
![contour-pic](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/contour-pic.png)

**face-detection**
![face-pic](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/face-pic.png)

**flow-detection**
![flow-face](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/flow-face.png)

![flow-traffic](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/flow-traffic.png)

**object-detection**
![object-pic](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/object-pic.png)

#### Filtering, FFTs, and Time Series data. (beta, optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the set up from the [Lab 3 demo](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Spring2021/Lab%203/demo) and the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

Include links to your code here, and put the code for these in your repo--they will come in handy later.

#### Teachable Machines (beta, optional)
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple.  However, its simplicity is very useful for experimenting with the capabilities of this technology.

You can train a Model on your browser, experiment with its performance, and then port it to the Raspberry Pi to do even its task on the device.

Here is Adafruit's directions on using Raspberry Pi and the Pi camera with Teachable Machines:

1. [Setup](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/raspberry-pi-setup)
2. Install Tensorflow: Like [this](https://learn.adafruit.com/running-tensorflow-lite-on-the-raspberry-pi-4/tensorflow-lite-2-setup), but use this [pre-built binary](https://github.com/bitsy-ai/tensorflow-arm-bin/) [the file](https://github.com/bitsy-ai/tensorflow-arm-bin/releases/download/v2.4.0/tensorflow-2.4.0-cp37-none-linux_armv7l.whl) for Tensorflow, it will speed things up a lot.
3. [Collect data and train models using the PiCam](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/training)
4. [Export and run trained models on the Pi](https://learn.adafruit.com/teachable-machine-raspberry-pi-tensorflow-camera/transferring-to-the-pi)

Alternative less steps option is [here](https://github.com/FAR-Lab/TensorflowonThePi).

#### PyTorch  
As a note, the global Python install contains also a PyTorch installation. That can be experimented with as well if you are so inclined.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interactions outputs and inputs.
**Describe and detail the interaction, as well as your experimentation.**

I chose openCV face detection model to detect whether the detected person is sleeping (eyes closed/open). A Pi camera was connected to the Raspberry Pi and taped on my iPad, so that it could live stream what's going on of the user at a correct angle. Both `facefrontal` and `eye_tree_eyeglasses` cascades were used to detect whether one's eyes are closed.

The video below shows a simple interaction that prints "eyes!!!" when the detected person's eyes are open and "no eyes!!!" when closed.

[![Video of simple interaction](https://img.youtube.com/vi/MNyLFcdi1h4/maxresdefault.jpg)](https://youtu.be/MNyLFcdi1h4)

(click to view the vid)

I improved the interaction so that it tells whether detected person is sleeping (eyes kept closed for a few seconds). A line of text "WARNING! She's sleeping!" in red was shown on the live video when the person is sleeping, shown in the pictures below.

When not sleeping:
![not-sleeping](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/eye-open.png)

When sleeping detected:
![sleep-detected](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/sleep-detected.png)

The video shows this improved interaction.

[![Video of sleeping interaction](https://img.youtube.com/vi/0oVudXbT3Vk/maxresdefault.jpg)](https://youtu.be/0oVudXbT3Vk)

(click to view the vid)

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note your observations**:
For example:
1. When does it what it is supposed to do?
    
    It works with good lightings when someone is facing towards the camera and is not too far away for the camera to detect his/her face and eyes. The camera also has to be fixed for the sleeping detection system to work.
    
3. When does it fail?

    It fails when the envrionment is dark, when the camera is in big motion (however this could be acutally caused by the low fps of the camera), when the person is far from the camera, when the person is not properly facing towards the camera, or when the person's eyes are covered. It also fails sometimes when the person looks downwards for a long time, but this rarely happened.

5. When it fails, why does it fail?

    It fails because it couldn't detect a face or the eyes properly (when the face is far, the lighting is bad, the face is not frontal, or the eyes are covered) so it stops counting how long the eyes' been closed. Sometimes also because the pi camera I used has a relatively low frame rate, so there are glitches in the captured video.

7. Based on the behavior you have seen, what other scenarios could cause problems?

    If there are multiple users (hence faces/eyes), it might be impossible for the system to accurately detect if someone is sleeping. For example, if A is sleeping, but B is not, the counter would not count how long A's eyes' been closed because it will be initialized when B's eyes' are open, hence the counter would never reach the threshold of sleeping and never give warning output.

**Think about someone using the system. Describe how you think this will work.**
1. Are they aware of the uncertainties in the system?

    Yes because they know the system is vision based so they should be aware that lighting is a crucial factor.
    
3. How bad would they be impacted by a miss classification?
    
    It could happen though super rarely that the system mistakenly classifies that the user as sleeping while he/she is actually not. In this case, the warning message would keep showing the screen. It happens more often that the system doesn't catch when one's sleeping. In this case, the warning is not shown hence the system would lose its main purpose.
    
5. How could change your interactive system to address this?
    I could give users intructions for the correct conditions to use the system when the system is running. I could also use a better camera with high frame rate to reduce glitches.

7. Are there optimizations you can try to do on your sense-making algorithm.
    I could lower the threshold for determining if one's sleeping, so that the system is less likely to be messed up by the environmental factors and more sensitve in catching if one's sleeping.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?

    The system can be used for alarming drowsy/fatigued drivers, or alarming students sleeping in class.

* What is a good environment for X?

    Environment with suffient lighting, with the camera fixed and facing towards the user's frontal face.

* What is a bad environment for X?

    Environment without suffient lighting, camera is not fixed and not facing towards the user's frontal face.

* When will X break?

    It breaks when face is not detected.

* When it breaks how will X break?

    The system could not recognize if one's sleeping and would give no warnings at all.

* What are other properties/behaviors of X?

    The system works better with people with large eyes.

* How does X feel?

    The system is light in weight and small in size.

**Include a short video demonstrating the answers to these questions.**

[![Video of part D](https://img.youtube.com/vi/WFVzAiSVVAs/maxresdefault.jpg)](https://youtu.be/WFVzAiSVVAs)
(click to view the vid)

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**Include a short video demonstrating the finished result.**

I added a speaker that played alarm when the detected person is sleeping. The finished prototype is a device that looks like a dash cam (but facing the inside of the car) and should be fixed either behind the steering wheel or on top of the windshield (both should be facing towards the driver). It could be connected to the car stereo using AUX cable. The images below shows the cardboard prototype.

![prototype.png](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/prototype.png)

![prototype2.png](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%205/img/prototype2.png)

This video below demonstrates it in use. Since I need WIFI to connect to the Pi, I just pretended I was driving.

[![Video of Part 2](https://img.youtube.com/vi/4JlA3ctKK5Y/maxresdefault.jpg)](https://youtu.be/4JlA3ctKK5Y)
(click to view the vid)
