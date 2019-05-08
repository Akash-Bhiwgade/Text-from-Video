# How to generate text from a video file using python

As per the trend, everyone is talking about Natural language processing, speech recognition, text generation etc. In this article, we will discuss on how can we get text from the video or audio files.

# Pre-requisites:

>> Python 3.7
>> ffmpeg
>> Libraries: os and speech_recognition

# Step 1: Prepare directory

Create a new folder and add some video files. For instance, I have created a folder 'SpeechConversion' and in this folder I have one video song (in .mp4 format).

# Step 2: Import libraries

Import the required libraries, refer below code:
import os
import speech_recognition as sr

# Step 3: Command for video conversion

I am using ffmpeg to convert the video file to audio. First, I will convert this to mp3 format and then will transform it to the wav format, as wav format allows you to extract better features. Here, my video file name is Bolna.mp4, I convert this to Bolna.mp3 then to Bolna.wav. Below are the commands for the conversion process. Let's save them in variables as below.

command2mp3 = "ffmpeg -i Bolna.mp4 Bolna.mp3"
command2wav = "ffmpeg -i Bolna.mp3 Bolna.wav"

# Step 4: Execute video conversion commands

Let us now execute these commands using the 'os' library as below

os.system(command2mp3)
os.system(command2wav)

# Step 5: Load the wav file

Now, let us load the wav file that was created in the above step. The below code can be used for the same.

r = sr.Recognizer()
audio = sr.AudioFile('Bolna.wav')

# Step 6: Process the wav file

Lastly, as per the required, set the duration of the audio you want for further processing. I am keeping this as 100 seconds duration for test purposes. You can change the same as per your convenience.

with audio as source:
	audio = r.record(source, duration=100)
print(r.recognize_google(audio))

Voila, you can get the text for the first 100 seconds of the video or audio file.

# Further enhancements:

The text generated can be later used for Natural language understanding and Natural language generation processes.

Hope this helps. Do share your comments below. Thank you..!!
