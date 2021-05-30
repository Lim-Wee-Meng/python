from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog, simpledialog
import tkinter as tk
from gtts import gTTS
import playsound
import os
import sys




global text,file
main=tk.Tk()
main.title('Text to Speech')
main.geometry('820x280')

lang_list=['English-Female(US)','English-Female(Canada)','English-Female(UK)','English-Female(GB)','English-Female(Australia)','English-Female(Ghana)',
           'English-Female(India)','English-Female(Ireland)','English-Female(New Zealand)','English-Female(Nigeria)','English-Female(Philippines)',
           'English-Female(South Africa)','English-Female(Tanzania)','Chinese-Female(Mandarin/China)','Chinese-Female(Mandarin/Taiwan)','Japanese-Female','Korean-Male','Thai-Female',
           'French-Female(Canada)','French-Female(France)','Portuguese-Female(Brazil)','Portuguese-Female(Portugal)','Spanish-Female(Spain)','Spanish-Female(United States)']
lang_func=['en-us','en-ca','en-uk','en-gb','en-au','en-gh',
           'en-in','en-ie','en-nz','en-ng','en-ph',
           'en-za','en-tz' ,'zh-cn','zh-tw','ja','ko','th',
           'fr-ca','fr-fr','pt-br','pt-pt','es-es','es-us']

langVar = StringVar(main)
langVar.set(lang_list[0])


langsel = OptionMenu(main,langVar, *lang_list)
langsel.grid(row=0,column=0,sticky=tk.W)

icon_img="/Users/remylim/Documents/program_pic/tts.png"
img1 = Image.open(icon_img)
img1 = img1.resize((100, 100), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)

label1= Label(main,text="Enter Text Here  >>",width=27).grid(row=1,column=0,sticky=W)

text_input=Text(main,width=69,height=10,borderwidth=3,relief='sunken')
text_input.grid(row=1,column=1,rowspan=5,columnspan=4,sticky=W)

main_logo=Label(main, image=img1)
main_logo.grid(row=2,column=0,rowspan=4)

label2= Label(main,text="Output Filename  >>",width=27).grid(row=6,column=0,sticky=W)
Outfilename=tk.Entry(main,width=54,borderwidth=3,relief="sunken")
Outfilename.grid(row=6,column=1,columnspan=4,sticky=W)

label3= Label(main,text="Output Directory >>",width=27).grid(row=7,column=0,sticky=W)
OutDir=tk.Entry(main,width=54,borderwidth=3,relief="sunken")
OutDir.grid(row=7,column=1,columnspan=4,sticky=W)

def select():
    folder_selected = filedialog.askdirectory()
    OutDir.delete(0,tk.END)
    OutDir.insert(tk.END,folder_selected)


    
def gfetch():
    global tts
    # define variables
    text = text_input.get("1.0","end-1c")
    OD = OutDir.get()
    OF = Outfilename.get()
    file = OD + OF + ".mp3"
    language =lang_func[int(lang_list.index(langVar.get()))]
    # initialize tts, create mp3 and play
    if var1.get()==1:
        tts = gTTS(text = text, lang = language, slow = True)
    else:
        tts = gTTS(text = text, lang = language, slow = False)
        
    tts.save("temp.mp3")
    #tts.save("/Users/remylim/Downloads/audio.wav")
    os.system("start " + file)
    

def save_file():
    gfetch()
    OD = OutDir.get()
    OF = Outfilename.get()
    file = OD + OF + ".mp3"
    tts.save(file)
    os.system("start " + file)
    
def read_text():
    gfetch()
    playsound.playsound("temp.mp3", True)
    
    
def clear():
    text = text_input.get("1.0","end-1c")
    if len(text)>0:
        text_input.delete("1.0","end")
    
def quit():
    main.destroy()
    raise SystemExit()
    rootquit()
    

    
var1 = IntVar()
var1.set(0)
varbox1=tk.Checkbutton(main, text="Slow",width=10,anchor='w', variable=var1).grid(row=0, column=1,sticky=W)

button1= tk.Button(main,text="Read",fg='blue',width=15,borderwidth=3,relief='raised',command=read_text).grid(row=8,column=0,sticky=tk.W, 
                                                            pady=4)

button2= tk.Button(main,text="Save",fg='green',width=15,borderwidth=3,relief='raised',command=save_file).grid(row=8,column=1,sticky=tk.W, 
                                                            pady=4)

button3= tk.Button(main,text="Clear",fg='orange',width=8,borderwidth=3,relief='raised',command=clear).grid(row=8,column=2,sticky=tk.W, 
                                                            pady=4)

button4= tk.Button(main,text="Quit",fg='red',width=15,borderwidth=3,relief='raised',command=quit).grid(row=8,column=3,sticky=tk.W, 
                                                            pady=4)

button5= tk.Button(main,text="Select",fg='blue',width=7,borderwidth=3,relief='raised',command=select).grid(row=7,column=6,sticky=tk.W, 
                                                            pady=4)


