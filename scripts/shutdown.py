#!/usr/bin/env python

import os
from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, root):

        # Theme-------
        s=ttk.Style()
        s.theme_use('clam')
        s.configure("TButton", font=("UbuntuMono Nerd Font Bold", 12), width = 25)
        s.map('TButton', background=[('active','grey')])
        # ------------

        self.rt = root
        self.rt.title("Shutdown")
        self.rt.geometry("+1670+905")
        self.rt.configure(bg="white")

        frame = Frame(root, bg="white")
        frame.pack(pady=5,padx=5)

        ttk.Button(frame, text="Log out",command=self._logout, style="TButton").grid(row=0, column=0)

        ttk.Button(frame, text="Reboot",command=self._reboot, style="TButton").grid(row=1, column=0)

        ttk.Button(frame, text="Shutdown",command=self._shutdown,style="TButton").grid(row=2, column=0)

        ttk.Separator(frame).grid(row=3,column=0,pady=5,padx=5,sticky="ew")

        ttk.Button(frame, text="Exit",command=self._exit,style="TButton").grid(row=4, column=0)
    
    def _logout(self):
        os.system("xdotool key Super_L+Shift+Escape")

    def _reboot(self):
        os.system("reboot")
    
    def _shutdown(self):
        os.system("shutdown now")
    
    def _exit(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    program = app(root)
    root.mainloop()