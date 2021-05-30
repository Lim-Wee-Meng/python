from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch

from PIL import ImageTk,Image
import seaborn as sns
import datetime
import requests
from bs4 import BeautifulSoup


global mrt_line
'''reading csv.file into dataframe using pandas'''
NSL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/North_South_Line.csv")
NEL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/North_East_Line.csv")
EWL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/East_West_Line.csv")
CL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Circle_Line.csv")
DTL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Downtown_Line.csv")

CLEL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Circle_Line_Ext_Line.csv")
CABL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Changi_Airport_Branch_Line.csv")
SKL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Seng_Kang_LRT.csv")
BPL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Bukit_Panjang_LRT.csv")
PL_df = pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Punggol_LRT.csv")
ALL_df= pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/all_lines.csv")
L2L_df= pd.read_csv("/Users/remylim/Desktop/Singapore_MRT_Network/Line2Line.csv")

L2L_df=L2L_df.set_index('Lines')
MRT_Lines=['Bukit Panjang LRT','Changi Airport Branch Line','Circle Line','Circle Line Ext','Downtown Line','East West Line','North East Line','North South Line','Punggol Line','Seng Kang Line']
dat_files={'Bukit Panjang LRT':'BPL_df',
           'Changi Airport Branch Line':'CABL_df',
           'Circle Line':'CL_df',
           'Circle Line Ext':'CLEL_df',
           'Downtown Line':'DTL_df',
           'East West Line':'EWL_df',
           'North East Line':'NEL_df',
           'North South Line':'NSL_df',
           'Punggol Line':'PL_df',
           'Seng Kang Line':'SKL_df'}
sline=""
eline=""
s_station=""
e_station=""

def sel_sline():
    global mrt_line,sline,variable_sL,s_station
    sline=variable_sline.get()
    s_station=""
    blank_start()
    
    if sline==MRT_Lines[0]:
        
        variable_sL.set(BPL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *BPL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

    elif sline==MRT_Lines[1]:
        variable_sL = StringVar(root)
        variable_sL.set(CABL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *CABL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

    elif sline==MRT_Lines[2]:
        
        variable_sL.set(CL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *CL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)
        
    elif sline==MRT_Lines[3]:
        
        variable_sL.set(CLEL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *CLEL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

    elif sline==MRT_Lines[4]:
        
        variable_sL.set(DTL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *DTL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

    elif sline==MRT_Lines[5]:
        
        variable_sL.set(EWL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *EWL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)
        
    elif sline==MRT_Lines[6]:
        
        variable_sL.set(NEL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *NEL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

    elif sline==MRT_Lines[7]:
        
        variable_sL.set(NSL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *NSL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

    elif sline==MRT_Lines[8]:
        
        variable_sL.set(PL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *PL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)
        
    else:
        
        variable_sL.set(SKL_df.English[0]) # default value
        mrt_sline = OptionMenu(root, variable_sL, *SKL_df.English)
        mrt_sline.config(width=20)
        mrt_sline.grid(row=1,column=1,sticky=W)

def sel_eline():
    global mrt_line,eline,variable_eL,e_station
    eline=variable_eline.get()
    e_station=""
    blank_end()
    
    if eline==MRT_Lines[0]:
        
        variable_eL.set(BPL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *BPL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)

    elif eline==MRT_Lines[1]:
        
        variable_eL.set(CABL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *CABL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)

    elif eline==MRT_Lines[2]:
        
        variable_eL.set(CL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *CL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)
        
    elif eline==MRT_Lines[3]:
        
        variable_eL.set(CLEL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *CLEL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)

    elif eline==MRT_Lines[4]:
        
        variable_eL.set(DTL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *DTL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)

    elif eline==MRT_Lines[5]:
        
        variable_eL.set(EWL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *EWL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)
        
    elif eline==MRT_Lines[6]:
        
        variable_eL.set(NEL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *NEL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)

    elif eline==MRT_Lines[7]:
        
        variable_eL.set(NSL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *NSL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)

    elif eline==MRT_Lines[8]:
        
        variable_eL.set(PL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *PL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)
        
    else:
        
        variable_eL.set(SKL_df.English[0]) # default value
        mrt_eline = OptionMenu(root, variable_eL, *SKL_df.English)
        mrt_eline.config(width=20)
        mrt_eline.grid(row=5,column=1,sticky=W)


def cfm_sline():
    global mrt_line,s_station,sline
    sL=variable_sL.get()
    

    if sL=="" :
        return
    
    if sline==MRT_Lines[0]:
        x=BPL_df.English[BPL_df.English == sL].index[0]
        Label(root,text=BPL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=BPL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=BPL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=BPL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=BPL_df.Station_Code[x]
        
    elif sline==MRT_Lines[1]:
        x=CABL_df.English[CABL_df.English == sL].index[0]
        Label(root,text=CABL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=CABL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=CABL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=CABL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=CABL_df.Station_Code[x]
        
    elif sline==MRT_Lines[2]:
        x=CL_df.English[CL_df.English == sL].index[0]
        Label(root,text=CL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=CL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=CL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=CL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=CL_df.Station_Code[x]

    elif sline==MRT_Lines[3]:
        x=CLEL_df.English[CLEL_df.English == sL].index[0]
        Label(root,text=CLEL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=CLEL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=CLEL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=CLEL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=CLEL_df.Station_Code[x]
        
    elif sline==MRT_Lines[4]:
        x=DTL_df.English[DTL_df.English == sL].index[0]
        Label(root,text=DTL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=DTL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=DTL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=DTL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=DTL_df.Station_Code[x]

    elif sline==MRT_Lines[5]:
        x=EWL_df.English[EWL_df.English == sL].index[0]
        Label(root,text=EWL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=EWL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=EWL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=EWL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=EWL_df.Station_Code[x]
        
    elif sline==MRT_Lines[6]:
        x=NEL_df.English[NEL_df.English == sL].index[0]
        Label(root,text=NEL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=NEL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=NEL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=NEL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=NEL_df.Station_Code[x]
        
    elif sline==MRT_Lines[7]:
        x=NSL_df.English[NSL_df.English == sL].index[0]
        Label(root,text=NSL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=NSL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=NSL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=NSL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=NSL_df.Station_Code[x]
        
    elif sline==MRT_Lines[8]:
        x=PL_df.English[PL_df.English == sL].index[0]
        Label(root,text=PL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=PL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=PL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=PL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=PL_df.Station_Code[x]
        
    elif sline==MRT_Lines[9]:
        x=SKL_df.English[SKL_df.English == sL].index[0]
        Label(root,text=SKL_df.Station_Code[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
        Label(root,text=SKL_df.Malay[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
        Label(root,text=SKL_df.Chinese[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
        Label(root,text=SKL_df.Tamil[x],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)
        s_station=SKL_df.Station_Code[x]
   






    
def cfm_eline():
    global mrt_line,e_station,eline,final_station
    eL=variable_eL.get()

    
    if eL=="":
        return
    if eline==MRT_Lines[0]:
        y=BPL_df.English[BPL_df.English == eL].index[0]
        Label(root,text=BPL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=BPL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=BPL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=BPL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=BPL_df.Station_Code[y]
        
    elif eline==MRT_Lines[1]:
        y=CABL_df.English[CABL_df.English == eL].index[0]
        Label(root,text=CABL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=CABL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=CABL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=CABL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=CABL_df.Station_Code[y]
        
    elif eline==MRT_Lines[2]:
        y=CL_df.English[CL_df.English == eL].index[0]
        Label(root,text=CL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=CL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=CL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=CL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=CL_df.Station_Code[y]
        

    elif eline==MRT_Lines[3]:
        y=CLEL_df.English[CLEL_df.English == eL].index[0]
        Label(root,text=CLEL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=CLEL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=CLEL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=CLEL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=CLEL_df.Station_Code[y]
        
    elif eline==MRT_Lines[4]:
        y=DTL_df.English[DTL_df.English == eL].index[0]
        Label(root,text=DTL_df.Station_Code[y],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=DTL_df.Malay[y],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=DTL_df.Chinese[y],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=DTL_df.Tamil[y],fg="green",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=DTL_df.Station_Code[y]
        

    elif eline==MRT_Lines[5]:
        y=EWL_df.English[EWL_df.English == eL].index[0]
        Label(root,text=EWL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=EWL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=EWL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=EWL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=EWL_df.Station_Code[y]
        
    elif eline==MRT_Lines[6]:
        y=NEL_df.English[NEL_df.English == eL].index[0]
        Label(root,text=NEL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=NEL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=NEL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=NEL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=NEL_df.Station_Code[y]
        
    elif eline==MRT_Lines[7]:
        y=NSL_df.English[NSL_df.English == eL].index[0]
        Label(root,text=NSL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=NSL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=NSL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=NSL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=NSL_df.Station_Code[y]
        
    elif eline==MRT_Lines[8]:
        y=PL_df.English[PL_df.English == eL].index[0]
        Label(root,text=PL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=PL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=PL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=PL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=PL_df.Station_Code[y]
        
    elif eline==MRT_Lines[9]:
        y=SKL_df.English[SKL_df.English == eL].index[0]
        Label(root,text=SKL_df.Station_Code[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
        Label(root,text=SKL_df.Malay[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
        Label(root,text=SKL_df.Chinese[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
        Label(root,text=SKL_df.Tamil[y],fg="red",relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
        e_station=SKL_df.Station_Code[y]

    final_station=e_station   

def sameline(eline,s_station,e_station):
    route=[]
    if eline==MRT_Lines[0]:
        a=BPL_df.Station_Code[BPL_df.Station_Code == s_station].index[0]
        b=BPL_df.Station_Code[BPL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1
        for s in range(a,b,step):
            route.append(BPL_df.Station_Code[s])

        
    elif eline==MRT_Lines[1]:
        a=CABL_df.Station_Code[CABL_df.Station_Code == s_station].index[0]
        b=CABL_df.Station_Code[CABL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1
        for s in range(a,b,step):
            route.append(CABL_df.Station_Code[s])
            
    elif eline==MRT_Lines[2]:
        a=CL_df.Station_Code[CL_df.Station_Code == s_station].index[0]
        b=CL_df.Station_Code[CL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(CL_df.Station_Code[s])

    elif eline==MRT_Lines[3]:
        a=CLEL_df.Station_Code[CLEL_df.Station_Code == s_station].index[0]
        b=CLEL_df.Station_Code[CLEL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(CLEL_df.Station_Code[s])
            
    elif eline==MRT_Lines[4]:
        a=DTL_df.Station_Code[DTL_df.Station_Code == s_station].index[0]
        b=DTL_df.Station_Code[DTL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(DTL_df.Station_Code[s])

    elif eline==MRT_Lines[5]:
        a=EWL_df.Station_Code[EWL_df.Station_Code == s_station].index[0]
        b=EWL_df.Station_Code[EWL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(EWL_df.Station_Code[s])
            
    elif eline==MRT_Lines[6]:
        a=NEL_df.Station_Code[NEL_df.Station_Code == s_station].index[0]
        b=NEL_df.Station_Code[NEL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(NEL_df.Station_Code[s])
            
    elif eline==MRT_Lines[7]:
        a=NSL_df.Station_Code[NSL_df.Station_Code == s_station].index[0]
        b=NSL_df.Station_Code[NSL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(NSL_df.Station_Code[s])
            
    elif eline==MRT_Lines[8]:
        a=PL_df.Station_Code[PL_df.Station_Code == s_station].index[0]
        b=PL_df.Station_Code[PL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(PL_df.Station_Code[s])
            
    elif eline==MRT_Lines[9]:
        a=SKL_df.Station_Code[SKL_df.Station_Code == s_station].index[0]
        b=SKL_df.Station_Code[SKL_df.Station_Code == e_station].index[0]
        if a>b:
            step=-1
        else:
            step=1

        for s in range(a,b,step):
            route.append(SKL_df.Station_Code[s])
    route.append(e_station)
    return route
  
def check():
    global mrt_line,s_station,e_station,eline,sline,eroute,troute,route
    route=[]
    eroute=[]         
    troute=[]
    tselect={}
    #Same Line
    if sline=="" or eline=="" or s_station=="" or e_station=="":
        messagebox.showerror("Incomplete Entry","Direction Not Completed")
        return
    if sline==eline:
            route=sameline(eline,s_station,e_station)
            show_route(route)
    else:
        head=[]
        tail=[]
        if sline==MRT_Lines[0] or sline==MRT_Lines[1] or sline==MRT_Lines[3] or sline==MRT_Lines[8] or sline==MRT_Lines[9]:
            head,sline,s_station=startline(sline,s_station)
        if eline==MRT_Lines[0] or eline==MRT_Lines[1] or eline==MRT_Lines[3] or eline==MRT_Lines[8] or eline==MRT_Lines[9]:
            tail,eline,e_station=endline(eline,e_station)
        if sline==eline:
            route=sameline(eline,s_station,e_station)
        else:
            
            route=diffline(sline,eline,s_station,e_station)
    
        route=head+route+tail
        show_route(route)
            
def startline(sline,s_station):
    hroute=[]
    if sline==MRT_Lines[0]:  
        if eline==MRT_Lines[7]:
            a=BPL_df.Station_Code[BPL_df.Station_Code == s_station].index[0]
            b=BPL_df.Station_Code[BPL_df.Station_Code == 'NS4/BP1'].index[0]
            if a>b:
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(BPL_df.Station_Code[s])
            sline=MRT_Lines[7]
            s_station='NS4/BP1'

        else:
            a=BPL_df.Station_Code[BPL_df.Station_Code == s_station].index[0]
            b=BPL_df.Station_Code[BPL_df.Station_Code == 'DT1/BP6'].index[0]
            if a>b: 
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(BPL_df.Station_Code[s])
            sline=MRT_Lines[4]
            s_station='DT1/BP6'  


    elif sline==MRT_Lines[1]:
        if eline==MRT_Lines[4]:
            a=CABL_df.Station_Code[CABL_df.Station_Code == s_station].index[0]
            b=CABL_df.Station_Code[CABL_df.Station_Code == 'CG1/DT35'].index[0]
            if a>b:
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(CABL_df.Station_Code[s])
            sline=MRT_Lines[4]
            s_station='CG1/DT35'
         
        else:
            a=CABL_df.Station_Code[CABL_df.Station_Code == s_station].index[0]
            b=CABL_df.Station_Code[CABL_df.Station_Code == 'EW4/CG'].index[0]
            if a>b:
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(CABL_df.Station_Code[s])
            sline=MRT_Lines[5]
            s_station='EW4/CG'
             
    elif sline==MRT_Lines[3]:
        if eline==MRT_Lines[4]:
            a=CLEL_df.Station_Code[CLEL_df.Station_Code == s_station].index[0]
            b=CLEL_df.Station_Code[CLEL_df.Station_Code == 'CC4/DT15'].index[0]
            if a>b: 
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(CLEL_df.Station_Code[s])
            sline=MRT_Lines[4]
            s_station='CC4/DT15'
        elif eline==MRT_Lines[7]:
            a=CLEL_df.Station_Code[CLEL_df.Station_Code == s_station].index[0]
            b=CLEL_df.Station_Code[CLEL_df.Station_Code == 'NS27/CE2'].index[0]
            if a>b:
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(CLEL_df.Station_Code[s])
            sline=MRT_Lines[7]
            s_station='NS27/CE2'
        else:
            a=CLEL_df.Station_Code[CLEL_df.Station_Code == s_station].index[0]
            b=CLEL_df.Station_Code[CLEL_df.Station_Code == 'CC4/DT15'].index[0]
            if a>b:
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                hroute.append(CLEL_df.Station_Code[s])
            sline=MRT_Lines[3]
            s_station='CC4/DT15'

         
    elif sline==MRT_Lines[8]:
        a=PL_df.Station_Code[PL_df.Station_Code == s_station].index[0]
        b=PL_df.Station_Code[PL_df.Station_Code == 'NE17/PTC'].index[0]
        if a>b:
            step=-1
        else:
            step=1
        for s in range(a,b,step):
            hroute.append(PL_df.Station_Code[s])
        sline=MRT_Lines[8]
        s_station='NE17/PTC'
         
    elif sline==MRT_Lines[9]:
        a=SKL_df.Station_Code[SKL_df.Station_Code == s_station].index[0]
        b=SKL_df.Station_Code[SKL_df.Station_Code == 'NE16/STC'].index[0]
        if a>b:
            step=-1
        else:
            step=1
        for s in range(a,b,step):
            hroute.append(SKL_df.Station_Code[s])
        sline=MRT_Lines[9]
        s_station='NE16/STC'
    hroute.append(s_station)
    return hroute,sline,s_station
    
def endline(eline,e_station):
    eroute=[]
    if eline==MRT_Lines[0]:
        if eline==MRT_Lines[7]:
            a=BPL_df.Station_Code[BPL_df.Station_Code == 'NS4/BP1'].index[0]
            b=BPL_df.Station_Code[BPL_df.Station_Code == e_station].index[0]
            if a>b:
                step=-1
            else:
                step=1
            for s in range(a,b,step):
                eroute.append(BPL_df.Station_Code[s])
            eline=MRT_Lines[7]
            e_station='NS4/BP1'

        else:
            a=BPL_df.Station_Code[BPL_df.Station_Code == 'DT1/BP6'].index[0]
            b=BPL_df.Station_Code[BPL_df.Station_Code == e_station].index[0]
            if a>b: 
             step=-1
            else:
             step=1
            for s in range(a,b,step):
             eroute.append(BPL_df.Station_Code[s])
            eline=MRT_Lines[4]
            e_station='DT1/BP6'  


    elif eline==MRT_Lines[1]:   
        if eline==MRT_Lines[4]:
            a=CABL_df.Station_Code[CABL_df.Station_Code == 'CG1/DT35'].index[0]
            b=CABL_df.Station_Code[CABL_df.Station_Code == e_station].index[0]
            if a>b: 
             step=-1
            else:
             step=1
            for s in range(a,b,step):
             eroute.append(CABL_df.Station_Code[s])
            eline=MRT_Lines[4]
            e_station='CG1/DT35'

        else:
            a=CABL_df.Station_Code[CABL_df.Station_Code =='EW4/CG'].index[0]
            b=CABL_df.Station_Code[CABL_df.Station_Code == e_station].index[0]
            if a>b:
             step=-1
            else:
             step=1
            for s in range(a,b,step):
             eroute.append(CABL_df.Station_Code[s])
            eline=MRT_Lines[5]
            e_station='EW4/CG'

    elif eline==MRT_Lines[3]:
        if eline==MRT_Lines[4]:
            a=CLEL_df.Station_Code[CLEL_df.Station_Code == 'CC4/DT15'].index[0]
            b=CLEL_df.Station_Code[CLEL_df.Station_Code == e_station].index[0]
            if a>b: 
             step=-1
            else:
             step=1
            for s in range(a,b,step):
             eroute.append(CLEL_df.Station_Code[s])
            eline=MRT_Lines[4]
            e_station='CC4/DT15'

        elif eline==MRT_Lines[7]:
            a=CLEL_df.Station_Code[CLEL_df.Station_Code == 'NS27/CE2'].index[0]
            b=CLEL_df.Station_Code[CLEL_df.Station_Code == e_station].index[0]
            if a>b:
             step=-1
            else:
             step=1
            for s in range(a,b,step):
             eroute.append(CLEL_df.Station_Code[s])
            eline=MRT_Lines[7]
            e_station='NS27/CE2'

    elif eline==MRT_Lines[8]:
        a=PL_df.Station_Code[PL_df.Station_Code == 'NE17/PTC'].index[0]
        b=PL_df.Station_Code[PL_df.Station_Code == e_station].index[0]
        if a>b:
         step=-1
        else:
         step=1
        for s in range(a,b,step):
         eroute.append(PL_df.Station_Code[s])
        eline=MRT_Lines[8]
        e_station='NE17/PTC'
     
    elif eline==MRT_Lines[9]:
        a=SKL_df.Station_Code[SKL_df.Station_Code == 'NE16/STC'].index[0]
        b=SKL_df.Station_Code[SKL_df.Station_Code == e_station].index[0]
        if a>b:
         step=-1
        else:
         step=1
        for s in range(a,b,step):
         eroute.append(SKL_df.Station_Code[s])
        eline=MRT_Lines[9]
        e_station='NE16/STC'

    eroute.append(final_station)
    return eroute,eline,e_station        

def diffline(sline,eline,s_station,e_station):
    troute=[]
    tselect={}
    if pd.isnull(L2L_df.loc[sline,eline])==False:
        if "," in L2L_df.loc[sline,eline]:
            l2l=L2L_df.loc[sline,eline].split(",")
        
            for rte in range(len(l2l)):
                
                if sline==MRT_Lines[2]:
                        a=CL_df.Station_Code[CL_df.Station_Code == s_station].index[0]
                        b=CL_df.Station_Code[CL_df.Station_Code == l2l[rte]].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(CL_df.Station_Code[s])            
                           
                elif sline==MRT_Lines[4]:
                        a=DTL_df.Station_Code[DTL_df.Station_Code == s_station].index[0]
                        b=DTL_df.Station_Code[DTL_df.Station_Code == l2l[rte]].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(DTL_df.Station_Code[s])

                elif sline==MRT_Lines[5]:
                        a=EWL_df.Station_Code[EWL_df.Station_Code == s_station].index[0]
                        b=EWL_df.Station_Code[EWL_df.Station_Code == l2l[rte]].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(EWL_df.Station_Code[s])

                elif sline==MRT_Lines[6]:
                        a=NEL_df.Station_Code[NEL_df.Station_Code == s_station].index[0]
                        b=NEL_df.Station_Code[NEL_df.Station_Code == l2l[rte]].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(NEL_df.Station_Code[s])

                elif sline==MRT_Lines[7]:
                        a=NSL_df.Station_Code[NSL_df.Station_Code == s_station].index[0]
                        b=NSL_df.Station_Code[NSL_df.Station_Code == l2l[rte]].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(NSL_df.Station_Code[s])
                troute.append(l2l[rte])
                if eline==MRT_Lines[2]:
                        a=CL_df.Station_Code[CL_df.Station_Code == l2l[rte]].index[0]
                        b=CL_df.Station_Code[CL_df.Station_Code == e_station].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(CL_df.Station_Code[s])            
                           
                elif eline==MRT_Lines[4]:
                        a=DTL_df.Station_Code[DTL_df.Station_Code == l2l[rte]].index[0]
                        b=DTL_df.Station_Code[DTL_df.Station_Code == e_station].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(DTL_df.Station_Code[s])

                elif eline==MRT_Lines[5]:
                        a=EWL_df.Station_Code[EWL_df.Station_Code == l2l[rte]].index[0]
                        b=EWL_df.Station_Code[EWL_df.Station_Code == e_station].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(EWL_df.Station_Code[s])

                elif eline==MRT_Lines[6]:
                        a=NEL_df.Station_Code[NEL_df.Station_Code == l2l[rte]].index[0]
                        b=NEL_df.Station_Code[NEL_df.Station_Code == e_station].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(NEL_df.Station_Code[s])

                elif eline==MRT_Lines[7]:
                        a=NSL_df.Station_Code[NSL_df.Station_Code == l2l[rte]].index[0]
                        b=NSL_df.Station_Code[NSL_df.Station_Code == e_station].index[0]
                        if a>b:
                            step=-1
                        else:
                            step=1
                        for s in range(a,b,step):
                            troute.append(NSL_df.Station_Code[s])
                
                tselect[rte]=troute
                troute=[]
            k=sorted(tselect, key=lambda k: len(tselect[k]), reverse=False)
            route=tselect[k[0]]
            
        else:
            l2l=L2L_df.loc[sline,eline]
            if sline==MRT_Lines[2]:
                a=CL_df.Station_Code[CL_df.Station_Code == s_station].index[0]
                b=CL_df.Station_Code[CL_df.Station_Code == l2l].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(CL_df.Station_Code[s])            
                   
            elif sline==MRT_Lines[4]:
                a=DTL_df.Station_Code[DTL_df.Station_Code == s_station].index[0]
                b=DTL_df.Station_Code[DTL_df.Station_Code == l2l].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(DTL_df.Station_Code[s])

            elif sline==MRT_Lines[5]:
                a=EWL_df.Station_Code[EWL_df.Station_Code == s_station].index[0]
                b=EWL_df.Station_Code[EWL_df.Station_Code == l2l].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(EWL_df.Station_Code[s])

            elif sline==MRT_Lines[6]:
                a=NEL_df.Station_Code[NEL_df.Station_Code == s_station].index[0]
                b=NEL_df.Station_Code[NEL_df.Station_Code == l2l].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(NEL_df.Station_Code[s])

            elif sline==MRT_Lines[7]:
                a=NSL_df.Station_Code[NSL_df.Station_Code == s_station].index[0]
                b=NSL_df.Station_Code[NSL_df.Station_Code == l2l[rte]].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(NSL_df.Station_Code[s])
            troute.append(l2l)
            if eline==MRT_Lines[2]:
                a=CL_df.Station_Code[CL_df.Station_Code == l2l].index[0]
                b=CL_df.Station_Code[CL_df.Station_Code == e_station].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(CL_df.Station_Code[s])            
                   
            elif eline==MRT_Lines[4]:
                a=DTL_df.Station_Code[DTL_df.Station_Code == l2l].index[0]
                b=DTL_df.Station_Code[DTL_df.Station_Code == e_station].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(DTL_df.Station_Code[s])

            elif eline==MRT_Lines[5]:
                a=EWL_df.Station_Code[EWL_df.Station_Code == l2l].index[0]
                b=EWL_df.Station_Code[EWL_df.Station_Code == e_station].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(EWL_df.Station_Code[s])

            elif eline==MRT_Lines[6]:
                a=NEL_df.Station_Code[NEL_df.Station_Code == l2l].index[0]
                b=NEL_df.Station_Code[NEL_df.Station_Code == e_station].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(NEL_df.Station_Code[s])

            elif eline==MRT_Lines[7]:
                a=NSL_df.Station_Code[NSL_df.Station_Code == l2l].index[0]
                b=NSL_df.Station_Code[NSL_df.Station_Code == e_station].index[0]
                if a>b:
                    step=-1
                else:
                    step=1
                for s in range(a,b,step):
                    troute.append(NSL_df.Station_Code[s])
            
            route=troute
                   
        route.append(e_station)
        return route
    else:
        if eline==MRT_Lines[0]:
            eline=MRT_Lines[7]
        elif eline==MRT_Lines[1]:
            eline=MRT_Lines[5]
        elif eline==MRT_Lines[3]:
            eline=MRT_Lines[2]
        elif eline==MRT_Lines[8]:
            eline=MRT_Lines[6]
        elif eline==MRT_Lines[9]:
            eline=MRT_Lines[6]
        route=diffline(sline,eline,s_station,e_station)
        return route
    
def show_plot():
    mplot_df=pd.DataFrame()
    mplot_df['Longtitude']=(map_route['lng'].astype(float)-103.5435)*3740
    mplot_df['Latitude']=-(map_route['lat'].astype(float)-1.4785)*3725
    si=len(mplot_df.Latitude)-1
    
    
    usetex = plt.rcParams["text.usetex"]
    plt.figure(figsize=(10,6))
    im = plt.imread("/Users/remylim/Desktop/Singapore_MRT_Network/Singapore_Mrt_Map.png")
    implot = plt.imshow(im)
    
    plt.scatter(mplot_df.Longtitude,mplot_df.Latitude,zorder=2,s=30,color='b', marker='o',label='Suggest Route')
    plt.scatter(mplot_df.Longtitude[0],mplot_df.Latitude[0],zorder=3,s=50,color='g', marker='o',label='Start')
    plt.scatter(mplot_df.Longtitude[si],mplot_df.Latitude[si],zorder=4,s=50,color='r', marker='o',label='Stop') 
    for mrta in range(len(map_route.station)):
        Name=map_route.station[mrta]
        mplot_lat=mplot_df.Latitude[mrta]+5
        mplot_lng=mplot_df.Longtitude[mrta]+5
        
        fs= 8
        plt.text(mplot_lng,mplot_lat,Name,color='m',fontsize=fs)
               
        #tp = TextPath((mplot_lng,mplot_lat),Name, size=12)
        #plt.gca().add_patch(PathPatch(tp, color="red"))
        

    plt.title('MRT Travel Recommendation')
    plt.savefig("MRT_Route.png", dpi="figure")
    plt.legend()
    plt.show()
    
def show_route(route_list):
    global main,map_route
    main=tk.Tk()
    main.title("Route")
    main.geometry("640x500")
    listboxB_row=0

    scrollbarBy = tk.Scrollbar(main,bg="green",orient=VERTICAL)
    scrollbarBy.grid(row=0,column=1,padx=5,pady=5,sticky=N+S+W,)
    scrollbarBx = tk.Scrollbar(main,bg="green",orient=HORIZONTAL)
    scrollbarBx.grid(row=1,column=0,padx=5,pady=5,sticky=E+W)

    listboxB = tk.Listbox(main,width=64,height=20,bg="cyan",xscrollcommand=scrollbarBx.set, yscrollcommand=scrollbarBy.set,selectmode=EXTENDED)
    listboxB.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
    scrollbarBx.config(command=listboxB.xview)
    scrollbarBy.config(command=listboxB.yview)
    
    ln=1
    map_station=[]
    map_name=[]
    map_lat=[]
    map_lng=[]
    p_text=""
    for r in route_list:
         z=ALL_df.Station_Code[ALL_df.Station_Code == r].index[0]
         r_text=f"{ALL_df.Station_Code[z]} {ALL_df.Name[z]} Lat: {'%.6f' %(ALL_df.lat[z])} Long:{'%.6f' %(ALL_df.lng[z])}"
         listboxB.insert(tk.END,r_text)
         if ln==1:
             listboxB.itemconfig(tk.END, bg='light green')    
         if r_text==p_text:
             listboxB.itemconfig(tk.END, bg='yellow')
         map_station.append(ALL_df.Station_Code[z])
         map_name.append(ALL_df.Name[z])
         map_lat.append(ALL_df.lat[z])
         map_lng.append(ALL_df.lng[z])
         ln +=1
         p_text=r_text
    listboxB.itemconfig(tk.END, bg='magenta')
    if (ln-2)*3.46875>60:
        time_travel= str(int(((ln-2)*3.46875)/60))+'hr ' + str(int(((ln-2)*3.46875)%60)) +'min'
    else:
        time_travel= str(int(((ln-2)*3.46875)%60))+'min'        

    
    map_route=pd.DataFrame({'station':map_station,'name':map_name,'lat':map_lat,'lng':map_lng})
        
    
    summary=f" Total Stations:{ln-2}     Estimated Travel Time:{time_travel}"
    listboxB.insert(tk.END,summary)
    listboxB.itemconfig(tk.END, bg='#f5beb8')
    


    button9= tk.Button(main,text="View Route (Map)",fg="blue",width=15,borderwidth=3,relief="raised",command=show_plot)
    button9.grid(row=2,column=0,padx=5,pady=5,sticky=E+W)
    
    button12= tk.Button(main,text="Quit",fg="red",width=15,borderwidth=3,relief="raised",command=quit_main)
    button12.grid(row=3,column=0,padx=5,pady=5,sticky=E+W)

    



def quit_main():
    main.destroy()
   
def show_CL():
    pass
def show_DTL():
    pass
def show_EWL():
    pass
def show_NEL():
    pass
def show_NSL():
    pass


    
def quit():
    root.destroy()
    raise SystemExit()
    rootquit()

root = tk.Tk()
root.title("MRT NETWORK")

variable_sL = StringVar(root)
variable_eL = StringVar(root)


Label(root,text="Starting Point",fg="green",anchor='w',width=23).grid(row=0,column=0,sticky=W)
Label(root,text="MRT Stations",fg="green",anchor='w',width=23).grid(row=0,column=1,sticky=W) 
variable_sline = StringVar(root)
variable_sline.set(MRT_Lines[0]) # default value

mrt_sline = OptionMenu(root, variable_sline, *MRT_Lines)
mrt_sline.config(width=20)
mrt_sline.grid(row=1,column=0,columnspan=2,sticky=W)

button1 =tk.Button(root,text="Select",fg="green",width=7,borderwidth=3,relief="raised",command=sel_sline)
button1.grid(row=2,column=0,sticky=W)
button1 =tk.Button(root,text="Confirm",fg="green",width=7,borderwidth=3,relief="raised",command=cfm_sline)
button1.grid(row=1,column=2,sticky=W)

Label(root,text="",bg='yellow',width=80,height=7).grid(row=4,rowspan=4,column=0,columnspan=4)
Label(root,text="End Point",fg="red",bg='yellow',anchor='w',width=23).grid(row=4,column=0,sticky=W)
Label(root,text="MRT Stations",fg="red",bg='yellow',anchor='w',width=23).grid(row=4,column=1,sticky=W) 
variable_eline = StringVar(root)
variable_eline.set(MRT_Lines[0]) # default value

def blank_start():
    Label(root,text="Station Code",fg="light grey",relief='sunken',anchor='w',width=20,padx=10).grid(row=2,column=1,sticky=W)
    Label(root,text="Malay",fg="light grey",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=0,sticky=W)
    Label(root,text="中文",fg="light grey",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=1,sticky=W)
    Label(root,text= "தமிழ்",fg="light grey",relief='sunken',anchor='w',width=20,padx=10).grid(row=3,column=2,sticky=W)

def blank_end():
    Label(root,text="Station Code",fg="light grey",bg='yellow',relief='sunken',anchor='w',width=20,padx=10).grid(row=6,column=1,sticky=W)
    Label(root,text="Malay",fg="light grey",bg='yellow',relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=0,sticky=W)
    Label(root,text="中文",fg="light grey",bg='yellow',relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=1,sticky=W)
    Label(root,text="தமிழ்",fg="light grey",bg='yellow',relief='sunken',anchor='w',width=20,padx=10).grid(row=7,column=2,sticky=W)
    
blank_start()
blank_end()

mrt_eline = OptionMenu(root, variable_eline, *MRT_Lines)
mrt_eline.config(width=20)
mrt_eline.grid(row=5,column=0,columnspan=2,sticky=W)



button2 =tk.Button(root,text="Select",bg='yellow',fg="red",width=7,borderwidth=3,relief="raised",command=sel_eline)
button2.grid(row=6,column=0,sticky=W)
button2 =tk.Button(root,text="Confirm",bg='yellow',fg="red",width=7,borderwidth=3,relief="raised",command=cfm_eline)
button2.grid(row=5,column=2,sticky=W)


button10= tk.Button(root,text="Check",fg="blue",width=7,borderwidth=3,relief="raised",command=check)
button10.grid(row=21,column=3,sticky=W)

button11= tk.Button(root,text="Quit",fg="red",width=7,borderwidth=3,relief="raised",command=quit)
button11.grid(row=22,column=3,sticky=W)
