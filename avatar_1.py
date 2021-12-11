from tkinter import *
from tkinter import ttk
import tkinter as tk
import uuid
import datetime
import pytz
from tkinter import messagebox


m=Tk()
ttk.Label(m,text='ENTER YOUR NAME').grid(column=0,row=0)
name_var=tk.StringVar()
e=Entry(m,textvariable=name_var)
e.grid(row=0,column=1)


def final(name,current_time,user_id):

        thisfinals={
            "NAME = ": name,
            "TIME = ":current_time,
            "USER-ID = ":user_id
        }
        N="NAME : "+ thisfinals["NAME = "]
        D="DATE : "+ str(thisfinals["TIME = "])
        U="USER-ID : "+ str(thisfinals["USER-ID = "])
        return(N,D,U)
    

def result():

    name=name_var.get()
    current_time=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    user_id=uuid.uuid4()
    messagebox.showinfo("results",final(name,current_time,user_id))
    return()

ttk.Button(m,text="ok",width=25,command=result).grid(column=1,row=2)
m.mainloop()


















