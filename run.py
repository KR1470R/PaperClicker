# -*- coding: utf-8 -*-

# from tkinter import Canvas
import pyautogui
import time
# import random
from tkinter import *
# from PIL import Image, ImageTk
import os
import re

root = Tk()
root.title('Paper Clicker')
# root.resizable(False, False)
root.geometry('400x200')
root.wm_attributes('-alpha', 0.1)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
myScreenshot = pyautogui.screenshot()
myScreenshot.save('screenshots/screen.png')
img = os.path.abspath('screenshots/screen.png')
background_img = PhotoImage(file=img)

text_btn1 = 'Get'
text_btn2 = 'Get'

lbl1 = Label(text='Get start checkpoints')
lbl2 = Label(text='Get end checkpoints')
lbl1.place(x=10, y=50)
lbl2.place(x=10, y=100)

textfbtn1 = StringVar()
textfbtn1.set('Get')

textfbtn2 = StringVar()
textfbtn2.set('Get')


def start():
    global btn, btn1, btn2
    btn = Button(text='Start clicker')
    btn1 = Button(textvariable=textfbtn1)
    btn2 = Button(textvariable=textfbtn2)
    btn1.place(x=190, y=45)
    btn2.place(x=190, y=95)
    btn.pack(side='bottom')


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom


def clicker(event):
    if textfbtn1.get() == 'Get' and textfbtn2.get() == 'Get':
        return
    else:
        start = 0
        a = 0
        end = 1
        print(text_btn2)
        start_chepoints = re.findall(r'\d+', str(text_btn1))
        start_chepoints = list(map(int, start_chepoints))
        end_checkpoints = re.findall(r'\d+', str(text_btn2))
        end_checkpoints = list(map(int, end_checkpoints))
        print(end_checkpoints)
        while start < end:
            start += 1
            print(start)
            time.sleep(a)
            a += 0.01
            if start == 102 or start % 102 == 0:
                a = 0
            # pyautogui.moveTo(random.uniform(start_chepoints[0][0],start_chepoints[1][0]),random.uniform(start_chepoints[0][1],start_chepoints[1][1]))
            pyautogui.moveTo(start_chepoints[0], start_chepoints[1])
            pyautogui.mouseDown(button='left')
            # pyautogui.mouseUp(button='left', x=random.uniform(end_checkpoints[0][0],end_checkpoints[1][0]),\
            # y=random.uniform(end_checkpoints[0][1],end_checkpoints[1][1]))
            pyautogui.mouseUp(button='left', x=end_checkpoints[0], y=end_checkpoints[1])


def destroy_all():
    lbl1.destroy()
    lbl2.destroy()
    btn.destroy()
    btn1.destroy()
    btn2.destroy()


def get_pos(event, to):
    global text_btn1
    global text_btn2
    global textfbtn1
    global textfbtn2
    if to == 'first':
        text_btn1 = pyautogui.position()
        textfbtn1.set(str(text_btn1))
    elif to == 'second':
        text_btn2 = pyautogui.position()
        textfbtn2.set(str(text_btn2))


def quit_from_screen(event):
    root.attributes('-fullscreen', False)
    canvas.destroy()
    root.unbind('<Escape>')
    root.unbind('<ButtonRelease-1>')
    create_all()


def get_pos_btn1(event):
    get_pos('event', 'first')
    quit_from_screen('quit')


def get_pos_btn2(event):
    get_pos('event', 'second')
    quit_from_screen('quit')


def get_start_checkpoint(event):
    global canvas
    destroy_all()
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save('screenshots/screen.png')
    canvas = Canvas(root, width=width, height=height)
    canvas.create_image(0, 0, anchor=NW, image=background_img)
    canvas.pack(side='left')
    root.attributes('-fullscreen', True)
    root.bind('<ButtonRelease-1>', get_pos_btn1)
    root.bind('<Escape>', quit_from_screen)


def get_end_checkpoint(event):
    global canvas
    destroy_all()
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save('screenshots/screen.png')
    canvas = Canvas(root, width=width, height=height)
    canvas.create_image(0, 0, anchor=NW, image=background_img)
    canvas.pack(side='left')
    root.attributes('-fullscreen', True)
    root.bind('<ButtonRelease-1>', get_pos_btn2)
    root.bind('<Escape>', quit_from_screen)


def create_all():
    global lbl, lbl1, lbl2
    lbl1 = Label(text='Get start checkpoints')
    lbl2 = Label(text='Get end checkpoints')
    lbl1.place(x=10, y=50)
    lbl2.place(x=10, y=100)

    start()

    btn.bind("<ButtonRelease-1>", clicker)
    btn1.bind("<ButtonRelease-1>", get_start_checkpoint)
    btn2.bind("<ButtonRelease-1>", get_end_checkpoint)


btn.bind("<ButtonRelease-1>", clicker)
btn1.bind("<ButtonRelease-1>", get_start_checkpoint)
btn2.bind("<ButtonRelease-1>", get_end_checkpoint)

root.mainloop()
