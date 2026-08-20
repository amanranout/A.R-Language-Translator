from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator
from gtts import gTTS
import playsound
import os
import threading
from PIL import Image, ImageTk

# ----------------- WINDOW -----------------
root = Tk()
root.geometry("1200x700")
root.title("A.R Translator")
root.resizable(False, False)

# ----------------- BACKGROUND IMAGE -----------------
try:
    bg_image = Image.open("AR11.jpg")   # keep image in same folder
    bg_image = bg_image.resize((1200,700))
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(root,image=bg_photo)
    bg_label.place(x=0,y=0,relwidth=1,relheight=1)

except:
    root.configure(bg="lightblue")

# ----------------- LANGUAGE DICTIONARY -----------------
lang_dict = {v:k for k,v in LANGUAGES.items()}

# ----------------- TRANSLATE FUNCTION -----------------
def translator():

    text = input_box.get(1.0,END).strip()

    if text == "":
        output_box.delete(1.0,END)
        output_box.insert(END,"Please enter text")
        return

    try:
        trans = Translator()

        src = lang_dict[input_lang.get()]
        dest = lang_dict[output_lang.get()]

        result = trans.translate(text,src=src,dest=dest)

        output_box.delete(1.0,END)
        output_box.insert(END,result.text)

    except Exception as e:
        output_box.delete(1.0,END)
        output_box.insert(END,"Translation Error")

# ----------------- SPEAK INPUT -----------------
def speak():

    text = input_box.get(1.0,END).strip()

    if text == "":
        return

    try:
        lang = lang_dict[input_lang.get()]

        tts = gTTS(text=text,lang=lang)

        file = "voice1.mp3"
        tts.save(file)

        threading.Thread(target=playsound.playsound,args=(file,),daemon=True).start()

    except:
        print("Voice error")

# ----------------- SPEAK OUTPUT -----------------
def speak2():

    text = output_box.get(1.0,END).strip()

    if text == "":
        return

    try:
        lang = lang_dict[output_lang.get()]

        tts = gTTS(text=text,lang=lang)

        file = "voice2.mp3"
        tts.save(file)

        threading.Thread(target=playsound.playsound,args=(file,),daemon=True).start()

    except:
        print("Voice error")

# ----------------- TITLE -----------------
title = Label(root,
text="Language Translator",
font=("Arial",22,"bold"),
bg="lightyellow")

title.pack(pady=15)

# ----------------- INPUT FRAME -----------------
frm_input = Frame(root,bg="lightblue",bd=5,relief=RIDGE)
frm_input.place(x=80,y=100,width=420,height=500)

Label(frm_input,text="Input Language",
font=("Arial",14,"bold"),bg="wheat").pack(pady=10)

languages = list(LANGUAGES.values())

input_lang = ttk.Combobox(frm_input,values=languages,state="readonly")
input_lang.set("english")
input_lang.pack()

input_box = Text(frm_input,height=15,width=45)
input_box.pack(pady=10)

Button(frm_input,
text="Speak",
font=("Arial",12,"bold"),
bg="peachpuff",
command=speak).pack()

# ----------------- OUTPUT FRAME -----------------
frm_output = Frame(root,bg="lightblue",bd=5,relief=RIDGE)
frm_output.place(x=700,y=100,width=420,height=500)

Label(frm_output,text="Output Language",
font=("Arial",14,"bold"),bg="wheat").pack(pady=10)

output_lang = ttk.Combobox(frm_output,values=languages,state="readonly")
output_lang.set("french")
output_lang.pack()

output_box = Text(frm_output,height=15,width=45)
output_box.pack(pady=10)

Button(frm_output,
text="Speak",
font=("Arial",12,"bold"),
bg="peachpuff",
command=speak2).pack()

# ----------------- TRANSLATE BUTTON -----------------
Button(root,
text="Translate",
font=("Arial",16,"bold"),
bg="gold",
command=translator).place(x=520,y=600,width=180,height=50)

root.mainloop()