import speech_recognition as sr 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import sys
import imageio
import PIL.Image
import cv2
import numpy as np 
import pygame
import pyglet
import os
import time
import ffmpy
from pynput import keyboard
from moviepy.editor import *
from gtts import gTTS 

image = []

def speech2text():
    r = sr.Recognizer()
    text2speech("Press Enter to record")
    input("Press Enter to record...")
    with sr.Microphone() as source:
        print('Say something')
        text2speech('Say something')
        audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        print ('Google thinks you said:\n' + text)
        text2speech('Google thinks you said ' +text)
    except:
        pass
    return text

def text2speech(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("test.mp3") 
    os.system("mpg321 test.mp3") 

def input_text():
    s = speech2text()
    s = s.lower()
    return s

def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'test.gif'
    imageio.mimsave(output_file, images, loop = 1,  duration=duration)


def work_with_string(s, image):
    array_string = s.split()
    array_char = []
    for i in range(0, len(array_string)):
        if os.path.exists(os.path.join("image", array_string[i] + '.png')) == True:
            array_char.append(array_string[i])

        else:
            for j in range(0, len(get_char(array_string[i]))):
                array_char.append(get_char(array_string[i])[j])
    
    for k in range(0, len(array_char)):
        image.append(os.path.join("image", array_char[k]+ '.png'))
        create_gif(image, 5)
def get_char(s):
    array = []
    for i in range(0, len(s)):
        array.append(s[i])
    return array

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('output_gif', type= str, help= 'Directory of gif image')

    return parser.parse_args(argv)
def convert_gif2mp4(gif_path, mp4_path):
    if os.path.exists(mp4_path):
        os.remove(mp4_path)
        ff = ffmpy.FFmpeg(inputs = {gif_path : None }, outputs = {mp4_path: None})
        ff.run()

def display_gif():
    convert_gif2mp4('test.gif', 'test.mp4')
    cam = cv2.VideoCapture('test.mp4')
    while (cam.isOpened()):
        ret,frame = cam.read()
        if ret == True:
            cv2.imshow('gif', frame)
            cv2.waitKey(100)
        else:
        	break;
    cam.release()
    cv2.destroyAllWindows()
    while True:
        print("Press q to exit")
        print("Press c to continue")
        j = input()
        if j == 'q':
            break;
        elif j == 'c':
            main()

def input_keyboard():
    inputK = input()
    if inputK == 'a':
        text2speech("What word do you want to add to sign language dictionary?")
        print("What word do you want to add to sign language dictionary? ")
        text = input()
        capture_image(text)

    elif inputK  == 'c':
        work_with_string(input_text(), image)
        text2speech("Changing text to sign language")
        display_gif()
def capture_image(text):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("webcam")
    img_counter = 0
    text2speech("Press Space to capture")
    text2speech("Press Esc to close webcam")
    print("Press Space to capture, Esc to close webcam")
    while True:
        ret, frame =cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break;
        k = cv2.waitKey(1)
        if k % 256 ==27:
            break;
        elif k % 256 ==32:
            img_name = os.path.join("image", text +".png")
            cv2.imwrite(img_name, frame)
            img = cv2.imread(os.path.join('image', text+ ".png"), 1)
            cv2.imshow("image", img)
            cv2.waitKey(2000)
            cv2.destroyAllWindows()
            print("Captured")
            text2speech("Captured")
    cam.release()
    cv2.destroyAllWindows()
    while True:
        print("Press q to exit")
        print("Press c to continue")
        j = input()
        if j == 'q':
            break;
        elif j == 'c':
            main()


def main():
    print("Press \"c\" to change text to sign language")
    print("Press \"a\" to add more sign language")
    input_keyboard()

