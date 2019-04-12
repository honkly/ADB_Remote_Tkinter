#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
import os

def on_click():  
    os.system('adb shell input keyevent KEYCODE_DPAD_DOWN')

top=tkinter.Tk(className=' ADB_Remote')
#定义窗体的大小，是400X200像素 
top.geometry('300x600') 

#加上标签
label = tkinter.Label(top)  
label['text'] = 'be on your own'  
label.pack() 

#加上按钮
button = tkinter.Button(top)
button['text'] = 'Ok'  
button.pack()

#添加按钮操作 
button['command'] = on_click 
button.pack()

# #添加可编辑文本框
# text = tkinter.StringVar()  
# text.set('ADB_Remote Debug')  
# entry = tkinter.Entry(top) 
# entry['textvariable'] = text  
# entry.pack() 

#进入消息循环体
top.mainloop() 