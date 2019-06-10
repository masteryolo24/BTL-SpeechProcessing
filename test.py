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
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
def text2speech(mytext, save_dir):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save(os.path.join("audio", save_dir)) 
    os.system("mpg321 " + os.path.join("audio", save_dir)) 

text2speech("Changing text to sign language", "changetext.mp3")