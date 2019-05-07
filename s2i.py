import speech_recognition as sr 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import sys
import imageio
import PIL.Image
from tkinter import *
import cv2
import numpy as np 
import pygame
import pyglet
import os
import argparse
import time
import ffmpy
from pynput import keyboard
from moviepy.editor import *
image = []


"""r = sr.Recognizer()

input("Press Enter to record...")
with sr.Microphone() as source:
    print('Say Hello')
    audio = r.listen(source)
text = r.recognize_google(audio)
try:
    print ('Google thinks you said:\n' + text)
except:
    pass"""



VALID_EXTENSIONS = ('png', 'jpg') 

def input_text():
	s = input()
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
        print(array_string[i])
        if os.path.exists(os.path.join("image", array_string[i] + '.png')) == True:
            array_char.append(array_string[i])

        else:
            for j in range(0, len(get_char(array_string[i]))):
                array_char.append(get_char(array_string[i])[j])
    
    for k in range(0, len(array_char)):
        image.append(os.path.join("image", array_char[k]+ '.png'))
    
    print(array_char)
    create_gif(image, 5)
def get_char(s):
    array = []
    for i in range(0, len(s)):
        array.append(s[i])
    return array

def display_gif(ag_file, width, height):
    # pick an animated gif file you have in the working directory
    ag_file
    animation = pyglet.resource.animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)
    # create a window and set it to the image size
    win = pyglet.window.Window(width, height)
    # set window background color = r, g, b, alpha
    # each value goes from 0.0 to 1.0
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)
    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()

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
    while cam.isOpened():
        ret,frame = cam.read()
        cv2.imshow('webcam', frame)
        cv2.waitKey(100)
    cam.release()
    cv2.destroyAllWindows()

def input_keyboard():
	inputK = input()
	if inputK == 's':
		print("Nhap chuoi muon them vao ngon ngu ki hieu: ")
		text = input()
		capture_image(text)

	elif inputK  == 'c':
		print("Nhap tu muon chuyen thanh ngon ngu ki hieu: ")
		work_with_string(input_text(), image)
		display_gif()
def capture_image(text):
	cam = cv2.VideoCapture(0)
	cv2.namedWindow("webcam")
	img_counter = 0
	while True:
		ret, frame =cam.read()
		cv2.imshow("test", frame)
		if not ret:
			break
		k = cv2.waitKey(1)
		if k % 256 ==27:
			break;
		elif k % 256 ==32:
			print("Press Space to capture: ")
            print("Press Esc to exit")
			img_name = os.path.join("image", text +".png")
			cv2.imwrite(img_name, frame)
	cam.release()
	cv2.destroyAllWindows()

def main():
	print("Press \"c\" to change text to sign language")
	print("Press \"s\" to add more sign language")
	input_keyboard()

