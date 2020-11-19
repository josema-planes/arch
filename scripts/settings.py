#!/usr/bin/env python

import os
import subprocess
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
        self.frames["general"] = General(parent=container)
        self.frames["general"].grid(row=0, column=1, sticky="nsew")

        self.frames["wifi"] = Wifi(parent=container)
        self.frames["wifi"].grid(row=0, column=1, sticky="nsew")

        self.frames["themes"] = Themes(parent=container)
        self.frames["themes"].grid(row=0, column=1, sticky="nsew")

        self.frames["icons"] = Icons(parent=container)
        self.frames["icons"].grid(row=0, column=1, sticky="nsew")

        self.frames["volume"] = Volume(parent=container)
        self.frames["volume"].grid(row=0, column=1, sticky="nsew")

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
    def __init__(self, parent):

        Frame.__init__(self, parent)

        ttk.Label(self, text="Welcome to settings", style="TLabel").grid(row=0, column=0, padx=100, pady=100)

# Wifi------------------------------------------------------
class Wifi(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)


        ttk.Label(self,text="Wifi status:", style="TLabel").grid(row=0,column=0,sticky="w",pady=5,padx=5)

        self.e = Scale(self, from_=0, to=1, orient=HORIZONTAL, command=self.scale_value,)

        if(os.system("nmcli n | grep 'enable'")==0):
            self.e.set(1)
        else:
            self.e.set(0)

        self.e.grid(row=0,column=1,sticky="e",pady=5,padx=5)

        ttk.Separator(self).grid(row=1,columnspan=2,padx=5,pady=10,sticky="ew")
        # List box -----------------------------------------

        ttk.Label(self, text="Conection status:", style="TLabel").grid(row=2,column=0,padx=5,sticky="w")

        self.stat = StringVar()
        self.statfg= StringVar()
        if(os.system("ping google.com -c 1")==0):
            self.stat.set("connected")
            self.statfg.set("green")
        else:
            self.stat.set("disconnected")
            self.statfg.set("red")

        Label(self, text=self.stat.get(), font=("sans", 16), fg=self.statfg.get()).grid(row=2,column=1,padx=5,sticky="e")

        ttk.Label(self, text="SSID:", style="TLabel").grid(row=3,column=0,padx=5,sticky="w")

        try:
            datassid = subprocess.run(['nmcli', '-g', 'CONNECTION', 'device'], capture_output=True, text=True)
            ssid = datassid.stdout.split()[0]
        except:
            ssid = "none"

        Label(self, text=ssid, font=("sans", 16)).grid(row=3,column=1,padx=5,sticky="e")
    
    def scale_value(self, val):
        if (val == "1"):
            self.enable()
        else:
            self.disable()

    def disable(self):
        os.system("nmcli n off")
    
    def enable(self):
        os.system("nmcli n on")

# Themes----------------------------------------------------
class Themes(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)

        ttk.Label(self, text="Set qtile theme:", style="TLabel").grid(row=0, column=0, pady=10)

        self.dracula = ttk.Button(self, text="dracula", style="TButton", command=self.dracula_theme)
        self.dracula.grid(row=1,column=0, padx=30, pady=2)

        self.material_ocean = ttk.Button(self, text="material ocean", style="TButton", command=self.material_ocean_theme)
        self.material_ocean.grid(row=2,column=0, padx=30, pady=2)

        self.nord = ttk.Button(self, text="nord", style="TButton", command=self.nord_theme)
        self.nord.grid(row=3,column=0, padx=30, pady=2)

        self.one_darck = ttk.Button(self, text="one darck", style="TButton", command=self.one_darck_theme)
        self.one_darck.grid(row=4,column=0, padx=30, pady=2)

        ttk.Separator(self).grid(row=5,column=0,padx=5,pady=10,sticky="ew")

        # Actual theme -----
        self.theme_path = "/home/josema/.config/qtile/config.json"

        with open(self.theme_path) as f:
            data = f.readlines()[0]
            raw = data.split()[1]

        # Remuve quotation marks
        actual_theme = raw.replace("}", "").replace('''"''', "")

        text = "Actual theme: " + actual_theme
        ttk.Label(self, text=text, style="TLabel").grid(row=6, column=0, pady=2, padx=10, sticky="w")
        # ----------------
    
    def config_file(self, newTheme):
        with open(self.theme_path, "w") as f:
            theme = '''{"theme": "''' + newTheme + '''"}'''
            f.write(theme)
    
    def restart_qtile(self):
        os.system("xdotool key Super_L+shift+r")

    def dracula_theme(self):
        self.config_file("dracula")
        self.restart_qtile()
        root.destroy()
    
    def material_ocean_theme(self):
        self.config_file("material-ocean")
        self.restart_qtile()
        root.destroy()
    
    def nord_theme(self):
        self.config_file("nord")
        self.restart_qtile()
        root.destroy()
    
    def one_darck_theme(self):
        self.config_file("one-dark")
        self.restart_qtile()
        root.destroy()

# Icons-----------------------------------------------------
class Icons(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)

        # collect data --------------
        config_file = "/home/josema/.config/gtk-3.0/settings.ini"
        themes_file = "/usr/share/themes"
        icons_file = "/usr/share/icons"
        cursor_file = "/usr/share/icons/default/index.theme"

        f = open(config_file, "r")
        lineas = f.readlines()

        th = lineas[1].replace("gtk-icon-theme-name = ", "")
        ic = lineas[2].replace("gtk-theme-name = ", "")
        cu = lineas[3].replace("gtk-cursor-theme-name = ", "")

        f.close()

        ttk.Label(self, text="Global theme:", style="TLabel").grid(row=0,column=0,padx=10,pady=20,sticky="w")
        ttk.Label(self, text="Icon theme:", style="TLabel").grid(row=1,column=0,padx=10,sticky="w")
        ttk.Label(self, text="Cursor theme:", style="TLabel").grid(row=2,column=0,padx=10,pady=20,sticky="w")

        # Gobal theme---------------------------------------
        data1 = os.listdir(themes_file)

        default1 = StringVar()
        myTh = th.strip() # Remove blanck spaces
        default1.set(myTh)
        
        menubutton = OptionMenu(self, default1, *data1)
        menubutton.configure(font=("sans", 14),width=20, heigh=1)
        menubutton["menu"].config(font=('sans',14),bg='white')
        menubutton.grid(row=0, column=1, sticky="e", padx=10)

        # Icon theme---------------------------------------
        data2 = os.listdir(icons_file)

        default2 = StringVar()
        myIc = ic.strip() # Remove blanck spaces
        default2.set(myIc)
        
        menubutton = OptionMenu(self, default2, *data2)
        menubutton.configure(font=("sans", 14),width=20, heigh=1)
        menubutton["menu"].config(font=('sans',14),bg='white')
        menubutton.grid(row=1, column=1, sticky="e", padx=10)

        # Cursor theme---------------------------------------
        data3 = os.listdir(icons_file)

        default3 = StringVar()
        myCu = cu.strip() # Remove blanck spaces
        default3.set(myCu)
        
        menubutton = OptionMenu(self, default3, *data3)
        menubutton.configure(font=("sans", 14),width=20, heigh=1)
        menubutton["menu"].config(font=('sans',14),bg='white')
        menubutton.grid(row=2, column=1, sticky="e", padx=10)

        # Advice----------------------------------------------
        Label(self, text="Warning! Changes need reboot", foreground="red").grid(row=3,columnspan=2,sticky="sew",pady=5)

# Volume----------------------------------------------------
class Volume(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent)

        self.new_volume = IntVar()

        ttk.Label(self, text="Volume level:", style="TLabel").grid(row=0, column=0, padx=5, pady=10,sticky="w")

        self.e = Scale(self, from_=0, to=100, orient=HORIZONTAL, length=250, command=self.set_volume)
        self.get_volume()
        self.e.grid(row=1,column=0,sticky="w",pady=5,padx=5)

        ttk.Button(self, text="Applay", style="bar.TButton", command=lambda:self.bvol(self.new_volume)).grid(row=1, column=1,sticky="w",padx=20)
    
    def get_volume(self):
        vol = subprocess.run(["amixer","get","Master"], capture_output=True, text=True)
        e = vol.stdout.replace("\n", "").replace("Simple mixer control 'Master',0  Capabilities: pvolume pvolume-joined pswitch pswitch-joined  Playback channels: Mono  Limits: Playback 0 - 87  Mono: Playback ", "")

        finalvol = e.split()[1].replace("[", "").replace("%]", "")

        self.e.set(int(finalvol))
    
    def set_volume(self, var):
        self.new_volume.set(var)
    
    def bvol(self, vol):
        cmd = "amixer set Master " + str(vol.get()) + "%"
        os.system(cmd)

        notification = "notify-send 'Volume set to " + str(vol.get()) + "%'"
        os.system(notification)



if __name__ == "__main__":
    root = Tk()
    program = app(root)
    root.mainloop()