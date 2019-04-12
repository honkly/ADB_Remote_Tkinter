#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
import os

def click_up():  
    os.system('adb shell input keyevent KEYCODE_DPAD_UP')
def click_down(): 
    os.system('adb shell input keyevent KEYCODE_DPAD_DOWN')

top=tkinter.Tk(className=' ADB_Remote')
#定义窗体的大小，是400X200像素 
top.geometry('300x600') 

#加上按钮
button1 = tkinter.Button(top,text="上",command=click_up,width=5,height=2)
button1.place(x=40, y=0)
button1.pack()

button2=tkinter.Button(top,text="下",command=click_down,width=5,height=2) 
button2.place(x=40, y=500)
button2.pack()

button3=tkinter.Button(top,text="左",command=click_down,width=5,height=2)
button3.place(x=10, y=30) 
button3.pack()

button4=tkinter.Button(top,text="右",command=click_down,width=5,height=2) 
button4.place(x=60, y=30) 
button4.pack()


#进入消息循环体
top.mainloop() 