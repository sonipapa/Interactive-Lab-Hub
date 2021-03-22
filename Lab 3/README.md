# You're a wizard, [Student Name Here]

<img src="https://pbs.twimg.com/media/Cen7qkHWIAAdKsB.jpg" height="400">

In this lab, we want you to practice wizarding an interactive device as discussed in class. We will focus on audio as the main modality for interaction but there is no reason these general techniques can't extend to video, haptics or other interactive mechanisms. In fact, you are welcome to add those to your project if they enhance your design.


## Text to Speech and Speech to Text

In the home directory of your Pi there is a folder called `text2speech` containing some shell scripts.

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav

```

you can run these examples by typing 
`./espeakdeom.sh`. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts

```

You can also play audio files directly with `aplay filename`.

After looking through this folder do the same for the `speech2text` folder. In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

## Serving Pages

In Lab 1 we served a webpage with flask. In this lab you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/$ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to [http://ixe00.local:5000]()


## Demo

In the [demo directory](./demo), you will find an example wizard of oz project you may use as a template. **You do not have to** feel free to get creative. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser. You can control what system says from the controller as well.

## Optional

There is an included [dspeech](.dspeech) demo that uses [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) for speech to text. If you're interested in trying it out we suggest you create a seperarate virutalenv. 



# Lab 3 Part 2

Create a system that runs on the Raspberry Pi that takes in one or more sensors and requires participants to speak to it. Document how the system works and include videos of both the system and the controller.

## Prep for Part 2

1. Sketch ideas for what you'll work on in lab on Wednesday.

My idea is a **Not So Accurate Lie Detector**. When the participant presses the button sensor and says something/answers a question, audio would be streamed from the Pi to my browser. I will then tell the Pi whether it's a lie by my wish, so that the Pi would give the feedback from me the wizard to the participant.

## Share your idea sketches with Zoom Room mates and get feedback

*what was the feedback? Who did it come from?*

My zoom roommates are Yimeng Sun, Renzhi Hu, Zhonghao Zhan, Panda Xu, Yuanhao Chu, and Yanjun Zhou. They all agreed that my idea is a feasible system and I could start working on it.
Yimeng Sun: It's not "Not So Accurate." Still have 50% chance to be acccurate.
Renzhi Hu: Maybe let the Pi speak to the participant for giving feedback.
Zhonghao Zhan: Maybe could try to use a pulse sensor to actually detect if it's a lie.
Panda Xu: Or maybe give red light for lies, green light for truth.
Yuanhao Chu: Sounds cool. It should be working.
Yanjun Zhou: Sounds feasible.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

The system is a lie detector, consisting of a Raspberry Pi, a speaker, a USB mic, a PiTFT screen, and a button, which are connected as shwon below. Text "*Don't you dare lie to me!*" is shown in the main screen of the TFT when no action is made.

![system-setup.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%203/system-setup.JPG)


The lie detector requires the partcipants to press the button and speak to the USB mic, and the wizard can eavesdrop, get the status of the button, and control the system remotely using webserver. When the button is pressed by the participant, the webserver will show the wizard the text "*Button is pressed!*" in red, as shown in the screenshots for the **controller**:

![controller.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%203/controller.JPG)

On this controller, when the wizard clicks `Eavesdrop`, audio would be streamed from the Pi to my browser. When `Truth` is pressed, the participant could hear "*Truth. You are honest*" from the speaker and see the TFT screen lighted green with text "*You are honest :) Applause for you...*". When `Lie` is pressed, the participant could hear "*Lie. Electric shock loading*" from the speaker and see the TFT screen lighted red with text "*You are lying! Electric shock...*". Shown in this picture:

![screen_lie_truth.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%203/screen_lie_truth.JPG)

When the wizard types in some texts to the input field under "Speak" and clicks `send`, the participant could hear the typed texts from the speaker and see the TFT screen lighted white with these texts:

![screen_speak_question.JPG](https://github.com/sonipapa/Interactive-Lab-Hub/blob/Spring2021/Lab%203/screen_speak_question.JPG)

The setup is demonstrated in this video:

[![Video of lie detector setup](https://img.youtube.com/vi/VV2UhvGg2yQ/maxresdefault.jpg)](https://youtu.be/VV2UhvGg2yQ)


The system allows the following two kinds of interaction:

**1. Let the participant speak freely & detect a lie**

The participant presses the button before speaking, and presses it again after done speaking. When the participant presses the button for the first time, the wizard sees the red text on the browser and clicks `Eavesdrop` to start audio streaming from the Pi. When the participant is done speaking with button pressing, the wizard sees the red text on the browser again and clicks `Truth` or `Lie` to give participant the result of lie detection.

**2. Let the participant answer a question & detect a lie**
The wizard clicks `Eavesdrop` to start audio streaming from the Pi before the participant is ready. When the wizard hears the participant is ready from the browser, he/she types in the question and clicks `send`. The participant listens & reads the question, presses the button before speaking, and presses it again after done speaking. When the participant is done speaking with button pressing, the wizard sees the red text on the browser again and clicks `Truth` or `Lie` to give participant the result of lie detection.


## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

A demo of testing the lie detector system is in this video:

[![Video of lie detector demo](https://img.youtube.com/vi/aomxX3Do4NY/maxresdefault.jpg)](https://youtu.be/aomxX3Do4NY)

Answer the following:

### What worked well about the system and what didn't?

*What worked well*: 

* The participant could not only hear the result, but also see it from the tft screen.
* The button is extremely useful for signaling the start/end of participant's voice input. It alleviated the delay in the whole system caused by the delay in audio streaming.
* The USB microphone is quite a smart idea when the AUX port is occupied by the speaker output.

*What didn't work well*: 

* The speaker sometimes outputs with a delay, and thus omits a few words in the beginning of the output speech.

### What worked well about the controller and what didn't?

*What worked well*: 

* Audio streaming was of good quality.
* It was quite simple for the wizard to controll the system from the webserver, because he/she only has to click buttons except for typing questions.
* Monitoring the participant's actions with the button helps the wizard to better control the system (i.e. knowing when to click `Eavesdrop`, when to give results, etc.).

*What didn't work well*: 

* If the participant does not pause for a second after clicks the button for the first time, the wizard may not be able to eavesdrop the whole content due to delay in audio streaming.
* It happened once when the participant has pressed the button but the browser didn't catch it.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

The WoZ interactions provided me with a detailed blueprint for designing a more autonomous version of the system. It worths a lot because it helps us find the right track first and avoid wasting time. It happens a lot that people waste so much time in a wrong direction when they just start desining the system with getting the system work autonomously. The WoZ simplfies the technology requirements and saves time for prototyping a such system by temporarily having human to "fake" the autonomous parts.

### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

My system right now does not actually detect lies due to the simple sensor it's using, and it does not give electric shock when someone is lying. Upon adding camera to the system, the facial expression of the participants can be captured for lie detection. Heartrate sensor would also be a logical choice, as lying in nature is related to one's psychological movement which increases one's heartrate. I could also try to add a component to give the participant electric shock when he/she is detected lying (thought this sounds evil LOL). 

