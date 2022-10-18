import pyautogui as pg
import time as t

import tkinter as tk

root = tk.Tk()
root.attributes('-topmost', True)
root.update()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

key = True


def hello():
    key = True
    for i in range(5):
        pg.press('home')
        t.sleep(1.25)


def key_change(key):
    key = False


button1 = tk.Button(text='Auto Home', command=hello, bg='brown', fg='white')
button2 = tk.Button(text='Turn off', command=key_change(key), bg='brown', fg='white')
canvas1.create_window(150, 170, window=button1)
canvas1.create_window(150, 200, window=button2)

root.mainloop()
