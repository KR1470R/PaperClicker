# -*- coding: utf-8 -*-

# from tkinter import Canvas
import pyautogui
import time
# import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageDraw
import os
import re
import signal

root = Tk()
root.title('Paper Clicker')
#oot.resizable(False, False)
root.geometry('500x500')
#root.wm_attributes('-alpha', 0.1)
root.configure(bg='#181915')

FONT = 'Ubuntu'
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
myScreenshot = pyautogui.screenshot()
try:
    myScreenshot.save('screenshots/screen.png')
except:
    os.mkdir('screenshots')
    myScreenshot.save('screenshots/screen.png')
img = os.path.abspath('screenshots/screen.png')
background_img = PhotoImage(file=img)
image_ = Image.open(img)
real_image = image_.resize((497,300))
real_image.save('screenshots/screen_view_for_interface.png',"PNG")
real_image = PhotoImage(file='screenshots/screen_view_for_interface.png')
img2 = os.path.abspath('screenshots/screen_view_for_interface.png')
background_img2 = PhotoImage(file=img2)
text_btn1 = 'Get'
text_btn2 = 'Get'
try:
    start_ico = os.path.abspath('menuicons/start.png')
    start_image = PhotoImage(file=start_ico)

    ico_add_path = os.path.abspath('menuicons/add_point.png')
    ico_add_btn = PhotoImage(file=ico_add_path)
except:
    messagebox.showerror('Error!','Main files not found! Please reinstall the app and try run it again! Er:0x12')
    root.destroy()
    os.kill(os.getpid(), signal.SIGKILL)
    sys.exit()
    
#lbl1 = Label(text='Point 1', font=FONT,fg='white',bg='#181915')
#lbl2 = Label(text='Point 2',font=FONT,fg='white',bg='#181915')
#lbl1.place(x=10, y=50)
#lbl2.place(x=10, y=100)

textfbtn1 = StringVar()
textfbtn1.set(text_btn1)

textfbtn2 = StringVar()
textfbtn2.set(text_btn2)
def on_closing():
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
		os.kill(os.getpid(), signal.SIGKILL)
		sys.exit()

class HoverInfo(Menu):
    def __init__(self, parent, text, command=None):
       self._com = command
       Menu.__init__(self,parent, tearoff=0)
       if not isinstance(text, str):
          raise TypeError('Trying to initialise a Hover Menu with a non string type: ' + text.__class__.__name__)
       toktext=re.split('\n', text)
       for t in toktext:
            self.add_command(label = t)
            self._displayed=False
            self.master.bind("<Enter>",self.Display )
            self.master.bind("<Leave>",self.Remove )

    def __del__(self):
        try:
            self.master.unbind("<Enter>")
            self.master.unbind("<Leave>")
        except:
            return
    def Display(self,event):
       if not self._displayed:
          self._displayed=True
          self.post(event.x_root, event.y_root)
       if self._com != None:
          self.master.unbind_all("<Return>")
          self.master.bind_all("<Return>", self.Click)

    def Remove(self, event):
     if self._displayed:
       self._displayed=False
       self.unpost()
     if self._com != None:
       self.unbind_all("<Return>")

    def Click(self, event):
       self._com()

def start():
    global btn, btn1, btn2,lbl1,lbl2,time_interval,counter,careful_checkbtn,label_time_interva,how_much_times,image_cvs,ico_btn

    lbl1 = Label(text='Point 1', font=FONT,fg='white',bg='#181915')
    lbl2 = Label(text='Point 2',font=FONT,fg='white',bg='#181915')
    lbl1.place(x=10, y=50)
    lbl2.place(x=10, y=100)

    btn = Label(text='Start',image=start_image,borderwidth=0,cursor="hand2",bg='#181915')
    btn1 = Label(textvariable=textfbtn1,font=(FONT,10),bg='#181915',fg='white',cursor="hand2",relief="groove",borderwidth=2)
    btn2 = Label(textvariable=textfbtn2,font=(FONT,10),bg='#181915',fg='white',cursor="hand2",relief="groove",borderwidth=2)
    btn1.place(x=70, y=50)
    btn2.place(x=70, y=100)
    btn.pack(side='bottom')

    label_time_interva = Label(text='Time Interval',font=FONT, fg='white',bg='#181915')
    time_interval = Spinbox(from_=1,to=30,width=5,bd=0,insertborderwidth=0,bg='#23251E',fg='white',state='disabled')
    time_interval.place(x=285,y=50)
    label_time_interva.place(x=180,y=49)

    how_much_times = Label(text='How much',font=FONT, fg='white',bg='#181915')
    counter = Spinbox(from_=1,to=9999,width=5,bd=0,insertborderwidth=0,bg='#23251E',fg='white',state='disabled')
    counter.place(x=285,y=100)
    how_much_times.place(x=180,y=100)

    careful_checkbtn = Checkbutton(text='Careful mode',selectcolor="#2C2C2C",underline=0,bg="#181915",overrelief='flat',
        offrelief='flat',highlightbackground='#181915',fg='white',activebackground='#181915',activeforeground='white',font='Ubuntu')
    careful_checkbtn.place(x=350,y=49)

    image_cvs = Canvas(width=497,height=300,bg='#313131')
    image_cvs.place(x=0,y=155)

    image_cvs.create_image(0, 0, image=background_img2, anchor=NW)

    ico_btn = Label(text='add',image=ico_add_btn,borderwidth=0,cursor="hand2",bg='#181915')
    ico_btn.place(x=0,y=10)

    hover_add_point = HoverInfo(ico_btn, 'Add point')
    hover_start = HoverInfo(btn, 'Start Clicker')

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
        a = int(time_interval.get())
        end = int(counter.get())
        print(text_btn2,end)
        start_chepoints = re.findall(r'\d+', str(text_btn1))
        start_chepoints = list(map(int, start_chepoints))
        end_checkpoints = re.findall(r'\d+', str(text_btn2))
        end_checkpoints = list(map(int, end_checkpoints))
        print(end_checkpoints)
        def clear_a():
            if careful_checkbtn:
                if start == 102 or start % 102 == 0:
                    a = int(time_interval.get())
            else:
                pass
        while start < end:
            start += 1
            print(start)
            time.sleep(a)
            a += 0.01
            clear_a()
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
    label_time_interva.destroy()
    time_interval.destroy()
    how_much_times.destroy()
    counter.destroy()
    careful_checkbtn.destroy()
    image_cvs.destroy()
    ico_btn.destroy()

def get_pos(event, to):
    global text_btn1,text_btn2,textfbtn1,textfbtn2,time_interval,counter
    if to == 'first':
        text_btn1 = pyautogui.position()
        textfbtn1.set('x: '+re.findall(r'\d+', str(text_btn1))[0]+'; '+'y: '+re.findall(r'\d+', str(text_btn1))[1])

    elif to == 'second':
        text_btn2 = pyautogui.position()
        textfbtn2.set('x: '+re.findall(r'\d+', str(text_btn2))[0]+'; '+'y: '+re.findall(r'\d+', str(text_btn2))[1])

def quit_from_screen(event):
    root.attributes('-fullscreen', False)
    canvas.destroy()
    root.unbind('<Escape>')
    root.unbind('<ButtonRelease-1>')
    create_all()

def get_pos_btn1(event):
    get_pos('event', 'first')
    quit_from_screen('quit')
    if textfbtn1.get() != 'Get' and textfbtn2.get() != 'Get':
        time_interval.config(state='normal')
        counter.config(state='normal')
def get_pos_btn2(event):
    get_pos('event', 'second')
    quit_from_screen('quit')
    if textfbtn1.get() != 'Get' and textfbtn2.get() != 'Get':
        time_interval.config(state='normal')
        counter.config(state='normal')

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
    start()
    btn.bind("<ButtonRelease-1>", clicker)
    btn1.bind("<ButtonRelease-1>", get_start_checkpoint)
    btn2.bind("<ButtonRelease-1>", get_end_checkpoint)

start()
btn.bind("<ButtonRelease-1>", clicker)
btn1.bind("<ButtonRelease-1>", get_start_checkpoint)
btn2.bind("<ButtonRelease-1>", get_end_checkpoint)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
