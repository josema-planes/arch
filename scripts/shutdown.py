#! /usr/bin/python

from tkinter import messagebox
import subprocess

def shutdown():
    MsgBox = messagebox.askquestion('Shutdown','Shutdown now?',icon = 'warning')
    if MsgBox == 'yes':
        subprocess.call("/home/josema/scripts/shutdown.sh")
    else:
        exit

shutdown()