import speech_recognition as sr 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
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
from PyQt5.QtWidgets import QDialog,QApplication ,QMessageBox, QListWidget, QCheckBox ,QComboBox, QGroupBox ,QDialogButtonBox , QVBoxLayout , QFrame,QTabWidget, QWidget, QLabel, QLineEdit, QPushButton
import sys
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

image = []

#Cac ham su dung voi UI (PyQt5)
class TabDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speech Processing")
        self.setWindowIcon(QIcon("myicon.png"))

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "Change")
        tabwidget.addTab(TabTwo(), "Add")

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(tabwidget)
        
        vboxLayout.addWidget(buttonbox)
        self.setLayout(vboxLayout)

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Test Tab1'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        self.button = QPushButton('Change to sign language', self)
        self.button.move(20, 80)

        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print("tab1, clicked")
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Messsage ", textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        print(textboxValue)
        press_c(textboxValue)

class TabTwo(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Test Tab1'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        self.button = QPushButton('Add to sign language dictionary', self)
        self.button.move(20, 80)
        self.button.clicked.connect(self.on_click)
        """
        self.button2 = QPushButton('Capture', self)
        self.button2.move(20, 100)
        self.button2.clicked.connect(self.on_click2)
        """

        self.show()
    @pyqtSlot()
    def on_click(self):
        print('tab2 clicked')
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message ", textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        print(textboxValue)
        press_a(textboxValue)

    #def on_click2(self):



#Cac ham su dung voi terminal
def speech2text():
    r = sr.Recognizer()
    read_audio("Enter.mp3")
    input("Press Enter to record...")
    with sr.Microphone() as source:
        print('Say something')
        read_audio("something.mp3")
        read_audio("beep.mp3")
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

def read_audio(file):
    os.system("mpg321 " + os.path.join("audio", file))

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
"""
def input_keyboard():
    inputK = input()
    if inputK == 'a':
        read_audio("add.mp3")
        print("What word do you want to add to sign language dictionary? ")
        text = input()
        capture_image(text)

    elif inputK  == 'c':
        work_with_string(input_text(), image)
        read_audio("change.mp3")
        display_gif()
        """

def press_c(text):
    work_with_string(text, image)
    read_audio("change.mp3")
    display_gif()
    
def press_a(text):
    read_audio('add.mp3')
    print("What word do you want to add to sign language dictionary?")
    capture_image(text)



def capture_image(text):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("webcam")
    img_counter = 0
    #text2speech("Press Space to capture")
    #text2speech("Press Esc to close webcam")
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
            read_audio("capture.mp3")
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

"""
def main():
    print("Press \"c\" to change text to sign language")
    print("Press \"a\" to add more sign language")
    input_keyboard()
    """


app = QApplication(sys.argv)
tabdialog = TabDialog()
tabdialog.show()
app.exec()