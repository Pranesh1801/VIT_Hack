from tkinter import *
from PIL import  Image,ImageTk
import os
import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import os 

root = Tk()
root.geometry('700x400')
#root.configure(bg='#c1f7f7')
#root.attributes('-topmost', True)
#root.attributes('-fullscreen', True)
#root.state("zoomed")
root.resizable(width=False, height=False)
path=os.path.dirname(os.path.abspath(__file__))
bg = PhotoImage(file = (path+"/1167.png"))
bg1 = PhotoImage(file = (path+"/1167987.png"))


label1 = Label( root, image = bg, width=1362, height=764)
label1.place(x = 0, y = 0)
#Label(root, text = 'Click Any One ', font = 'arial 15 bold').place(x=620, y=320)

canvas1 = Canvas( root, highlightthickness=0, width = 400, height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.create_text( 450, 100, fill='White', font = 'chiller 30 bold', text = "Click Start:")
num = 1
a=50
def printf(output, a):
    add()
#    canvas2.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( 100, a, fill='White', font = 'chiller 30 bold', text = output)
    #label1 = Label( root, text="asp")
    #label1.place(x = 150, y = 100)
def add():
    global a
    a+=18   
def assistant_speaks(output, a):
    global num
    num += 1
    printf(output, a)
 
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    file = str(num)+".mp3"

    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)
 
def process_text(input):
    f=open('pass.txt','r')
    lines = f.read()
    print(lines)
    try:
        if lines in input or lines.lower() in input:
           print("login")
           file=(path+"/main.py")
           os.system('"' + file + '"')
           return

 
        else:   
 
            assistant_speaks("wrong credential", a)
            tryagain(a)
    except :
 
        assistant_speaks("I don't understand", a)
        tryagain(a)
 
def get_audio(a):
 
    rObject = sr.Recognizer()
    audio = '' 
    with sr.Microphone() as source:
        print("Speak...")
        audio = rObject.listen(source, phrase_time_limit = 5)
    print("Stop.") # limit 5 secs
        
    try:
 
        text = rObject.recognize_google(audio, language ='en-US')
        print(text)
        return text
 
    except:
 
        assistant_speaks("Could not understand your audio, PLease try again !", a)
        return 0
def tryagain(a):
    assistant_speaks("try again", a)
    password = get_audio(a)
    if password!=0:
        password=password.lower()
        process_text(password)
    else:
        tryagain(a)
    
def thephotographer(a):
    assistant_speaks("Password", a)
    password = get_audio(a)
    if password!=0:
        password=password.lower()
        process_text(password)
    else:
        tryagain(a)


def ch1(e):
    button_1.config(width=190, height=110, borderwidth=2)
def chb1(e):
    button_1.config(width=180, height=100, borderwidth=0)

    
button_1=Button(root, image=bg1, width=180, height=100, command=lambda:[thephotographer(a)], borderwidth=0)
button_1.place(x=260,y=280)


button_1.bind("<Enter>",ch1)
button_1.bind("<Leave>",chb1)


root.mainloop()
