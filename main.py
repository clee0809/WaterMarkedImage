# import required modules

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
from turtle import width
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import random

import click
NUM_OF_WATERMARK = 7

root = Tk()
root.title("Add Watermark")
root.geometry("800x600")

## functions

def remove_image():
    img_label.destroy()
    # input_text.insert(0, "Type your watermark here")

def load_image():
    global img_path, im, photo, img_label

    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    im = Image.open(img_path)
    im.thumbnail((450, 450))
    photo = ImageTk.PhotoImage(im)    
        
    img_label = Label(root, image=photo)
    # img_label.image = photo
    img_label.grid(row=2, column=0, columnspan=3)

def add_watermark():
    global wm_img_path
    img = Image.open(img_path)
    width, height = img.size
    font_size = int(height/30)
    text_font = ImageFont.truetype("C:\Windows\Fonts\COPRGTB.TTF", font_size)
    text_to_add = input_text.get()

    edit_photo = ImageDraw.Draw(img)

    ## one line watermark
    # x = im.size[0] - len(text_to_add)
    # y = im.size[1] - 15
    # edit_photo.text((x,y), text_to_add, fill=(255,255,255, 75), font=text_font)

    # Loop for Multiple Watermarks
    y=font_size
    # print(y)
    for i in range(NUM_OF_WATERMARK):
        x=random.randint(0, width-len(text_to_add))        
        edit_photo.text((x,y), text_to_add, fill=(255,255,255, 25), font=text_font)
        y+=random.randrange(0,int(height/8), 19)+font_size


    ## save watermarked file
    dot_pos = img_path.rfind('.')
    wm_img_path = img_path.replace(img_path[dot_pos], "_watermark.")
    img.save(wm_img_path)

    input_text.delete(0, END)
    input_text.insert(0, "Saving image...")

    img_label.after(2000, show_pic)

    

def show_pic():
    global wm_image
    wm_img = Image.open(wm_img_path)
    wm_img.thumbnail((450,450))
    wm_image = ImageTk.PhotoImage(wm_img)
    
    img_label.config(image=wm_image)

    input_text.delete(0, END)

    messagebox.showinfo(message=f"Successfully created watermarked image.\n as {wm_img_path}")

def click(event):
    input_text.configure(state=NORMAL)
    input_text.delete(0, END)
    input_text.unbind('<Button-1>', clicked)
    
select_btn = Button(root, text="Select Image", bg='#78938A', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=load_image)
select_btn.grid(row=0, column=0, pady=20)

refresh_btn = Button(root, text="Refresh", bg='#78938A', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=remove_image)
refresh_btn.grid(row=0, column=1, pady=20)

input_text = Entry(root, width=30, font=("Helvetica", 15))
input_text.insert(0, "Type your watermark here")
input_text.grid(row=1, column=0,  padx=5, ipady=10)
add_watermark_btn = Button(root, text="Add Watermark", width=12, bg='#78938A', fg='white', font=('ariel 15 bold'), relief=GROOVE, command=add_watermark)
add_watermark_btn.grid(row=1, column=1, padx=10, pady=20)

clicked = input_text.bind('<Button-1>', click)

root.mainloop()