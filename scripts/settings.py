#!/usr/bin/env python

import os
from tkinter import *
from tkinter import ttk
from functools import partial


class app:
    
    def __init__(self, root):
        self.rt = root
        self.rt.title("settings")
        self.rt.configure(bg="white")

        # Theme-------
        s=ttk.Style()
        s.theme_use('clam')

        s.configure("TButton", font=("UbuntuMono Nerd Font Bold", 22), width = 25)
        s.configure("bar.TButton", font=("UbuntuMono Nerd Font Bold", 14), width = 15)

        s.configure("TLabel", font=("UbuntuMono Nerd Font Bold", 22))

        s.map('TButton', background=[('active','grey')])
        # ------------

        container = Frame(root)
        container.grid(row=0,column=1)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.frames = {}
        self.frames["general"] = General(parent=container, controller=self)
        self.frames["general"].grid(row=0, column=1, sticky="nsew")

        self.frames["themes"] = Themes(parent=container, controller=self)
        self.frames["themes"].grid(row=0, column=1, sticky="nsew")

        self.frames["icons"] = Icons(parent=container, controller=self)
        self.frames["icons"].grid(row=0, column=1, sticky="nsew")

        self.frames["wifi"] = Wifi(parent=container, controller=self)
        self.frames["wifi"].grid(row=0, column=1, sticky="nsew")

        self.show_frame("general")


        # sidebar---------------------------------
        sidebar = Frame(root, bg="white")
        sidebar.grid(row=0,column=0)
        
        # Autocreate buttons with self.frames
        i=0
        for element in self.frames:
            ttk.Button(sidebar, text=element, style="bar.TButton", command=partial(self.show_frame, element)).grid(row=i, padx=5, pady=2)
            i += 1


        ttk.Separator(sidebar).grid(row=25,column=0,padx=5,pady=10,sticky="ew")

        ttk.Button(sidebar, text="exit", style="bar.TButton", command=self.exit).grid(row=26,column=0)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    
    def exit(self):
        root.destroy()


# General--------------------------------------------------
class General(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        self.controller = controller

        ttk.Label(self, text="Welcome to settings", style="TLabel").grid(row=0, column=0, padx=100, pady=100)

# Themes----------------------------------------------------
class Themes(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        self.controller = controller

        ttk.Label(self, text="Set qtile theme:", style="TLabel").grid(row=0, column=0, pady=10)

        self.dracula = ttk.Button(self, text="dracula", style="TButton", command=self.dracula_theme)
        self.dracula.grid(row=1,column=0, padx=30, pady=2)

        self.material_ocean = ttk.Button(self, text="material ocean", style="TButton", command=self.material_ocean_theme)
        self.material_ocean.grid(row=2,column=0, padx=30, pady=2)

        self.nord = ttk.Button(self, text="nord", style="TButton", command=self.nord_theme)
        self.nord.grid(row=3,column=0, padx=30, pady=2)

        self.one_darck = ttk.Button(self, text="one darck", style="TButton", command=self.one_darck_theme)
        self.one_darck.grid(row=4,column=0, padx=30, pady=2)

        Label(self, text="").grid(row=5, column=0, pady=2)
    
    def config_file(self):
        os.system("rm ~/.config/qtile/config.json")
        os.system("touch ~/.config/qtile/config.json")
    
    def restart_qtile(self):
        os.system("xdotool key Super_L+shift+r")

    def dracula_theme(self):
        self.config_file()
        os.system("""echo '{"theme": "dracula"}' >> ~/.config/qtile/config.json""")
        self.restart_qtile()
        root.destroy()
    
    def material_ocean_theme(self):
        self.config_file()
        os.system("""echo '{"theme": "material-ocean"}' >> ~/.config/qtile/config.json""")
        self.restart_qtile()
        root.destroy()
    
    def nord_theme(self):
        self.config_file()
        os.system("""echo '{"theme": "nord"}' >> ~/.config/qtile/config.json""")
        self.restart_qtile()
        root.destroy()
    
    def one_darck_theme(self):
        self.config_file()
        os.system("""echo '{"theme": "one-dark"}' >> ~/.config/qtile/config.json""")
        self.restart_qtile()
        root.destroy()

# Icons-----------------------------------------------------
class Icons(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        self.controller = controller

        ttk.Label(self, text="All icons themes:", style="TLabel").grid(row=0, column=0, padx=100, pady=30)

        ttk.Separator(self).grid(row=1,column=0,padx=5,pady=10,sticky="ew")

        # collect data --------------
        config_file = "/home/josema/.config/gtk-3.0/settings.ini"

        word = 'gtk'
        matches = []
        with open(config_file) as lines:
            for line in lines:
                if word in line:
                    matches.append(line)

        cont = 2
        for linea in matches:
            Label(self, text=linea, font=("sans",12)).grid(row=cont,column=0,sticky="w",padx=20)
            cont += 1

# Wifi------------------------------------------------------
class Wifi(Frame):
    def __init__(self, parent, controller):

        Frame.__init__(self, parent)

        self.controller = controller

        ttk.Label(self, text="Wifi status:", style="TLabel").grid(row=0, padx=20, pady=10, sticky="w")

        if (os.system("nmcli n | grep 'enabled'")==0):  # return 0 if ture
            status = "enabled"
        else:
            status = "disabled"

        Label(self, text=status, font=("sans", 14)).grid(row=1, column=0, sticky="w", padx=20)

        ttk.Separator(self).grid(row=2,column=0,padx=5,pady=10,sticky="ew")

        ttk.Label(self, text="Conection status:", style="TLabel").grid(row=3, padx=20, pady=10, sticky="w")

        self.connection = StringVar()

        if (os.system("ping google.com -c 1")==0):
            self.connection.set("connected")
        else:
            self.connection.set("disconnected")
        
        Label(self, text=self.connection.get(), font=("sans", 14)).grid(row=4, column=0, sticky="w", padx=20)



if __name__ == "__main__":
    root = Tk()
    program = app(root)
    root.mainloop()