#!/usr/bin/env python

import gi

import os
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class myApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(800, 600)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        # header bar ----------------------------
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        self.set_titlebar(hb)

        # stack ----------------------------------
        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        grid.attach(stack, 1, 0, 1, 1)

        myApp = Gtk.StackSidebar()
        myApp.set_stack(stack)
        grid.attach(myApp, 0, 0, 1, 1)
        
        # wifi ----------------------------------------------------------------
        gridWifi = Gtk.Grid(column_homogeneous=True)

        gridWifi.set_margin_top(60)
                
        labelWifi = Gtk.Label()
        labelWifi.set_markup("<span size='x-large'>Wi-Fi</span>")

        switchWifi = Gtk.Switch()
        switchWifi.set_margin_right(100)
        switchWifi.connect("notify::active", self.on_switch_activated)

        if(os.system("nmcli n | grep 'enable'")==0):
            switchWifi.set_active(True)
        else:
            switchWifi.set_active(False)
        
        labelCon = Gtk.Label()
        labelCon.set_markup("<span size='x-large'>Status</span>")
        labelCon.set_margin_top(30)

        labelStat = Gtk.Label()
        if(os.system("ping google.com -c 1")==0):
            markup1 = "<span foreground='green' size='x-large'>connected</span>"
        else:
            markup1 = "<span foreground='red' size='x-large'>disconnected</span>"
        labelStat.set_markup(markup1)
        labelStat.set_margin_top(30)

        labelSsid = Gtk.Label()
        labelSsid.set_markup("<span size='x-large'>SSID</span>")
        labelSsid.set_margin_top(30)

        labelConName = Gtk.Label()
        try:
            datassid = subprocess.run(['nmcli', '-g', 'CONNECTION', 'device'], capture_output=True, text=True)
            ssid = datassid.stdout.split()[0]
        except:
            ssid = "none"
        labelConName.set_markup("<span size='x-large'>" + ssid + "</span>")
        labelConName.set_margin_top(30)

        gridWifi.attach(labelWifi, 0,0,1,1)
        gridWifi.attach(switchWifi, 1,0,1,1)
        gridWifi.attach(labelCon, 0,1,1,1)
        gridWifi.attach(labelStat, 1,1,1,1)
        gridWifi.attach(labelSsid, 0,2,1,1)
        gridWifi.attach(labelConName, 1,2,1,1)

        nameWifi = "Wi-Fi"
        titleWifi = "Wi-Fi"
        stack.add_titled(gridWifi, nameWifi, titleWifi)

        # sound ----------------------------------------------------------------

        gridSound = Gtk.Grid(column_homogeneous=True)

        gridSound.set_margin_top(60)
        gridSound.set_margin_right(100)
                
        labelSound = Gtk.Label()
        labelSound.set_markup("<span size='x-large'>Volume level</span>")

        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)
        self.scaleSound = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        self.scaleSound.set_digits(0)
        self.scaleSound.connect("value-changed", self.scale_moved)

        vol = subprocess.run(["amixer","get","Master"], capture_output=True, text=True)
        fvol = vol.stdout
        volLevel = fvol.split()[25]
        fVolLevel = volLevel.replace("[", "").replace("%]", "")
        self.scaleSound.set_value(int(fVolLevel))

        gridSound.attach(labelSound, 0,0,1,1)
        gridSound.attach(self.scaleSound, 1,0,1,1)

        nameSound = "Sound"
        titleSound = "Sound"
        stack.add_titled(gridSound, nameSound, titleSound)

        # appearance ---------------------------------------------------------
        gridAp = Gtk.Grid(column_homogeneous=True)

        gridAp.set_margin_top(60)
        gridAp.set_margin_right(100)

        # qtile theme ---------
        labelQtile = Gtk.Label()
        labelQtile.set_markup("<span size='x-large'>Qtile theme</span>")

        comBoxQ = Gtk.ComboBoxText()

        qtile_themes = ["dracula", "material-ocean", "nord", "one-dark"]
        for theme in qtile_themes:
            comBoxQ.append_text(theme)
        
        with open("/home/josema/.config/qtile/config.json") as f:
            dataTh = f.readlines()[0]
            rawTh = dataTh.split()[1]
        actual_theme = rawTh.replace("}", "").replace('''"''', "")

        if actual_theme == "dracula":
            comBoxQ.set_active(0)
        elif actual_theme == "material-ocean":
            comBoxQ.set_active(1)
        elif actual_theme == "nord":
            comBoxQ.set_active(2)
        elif actual_theme == "one-dark":
            comBoxQ.set_active(3)
        
        comBoxQ.connect("changed", self.on_comBoxQ_changed)

        # path variables ---------
        self.config_file = "/home/josema/.config/gtk-3.0/settings.ini"
        themes_file = "/usr/share/themes"
        icons_file = "/usr/share/icons"
        self.cursor_file = "/usr/share/icons/default/index.theme"

        g = open(self.config_file, "r")
        lineas = g.readlines()

        ic = lineas[1].replace("gtk-icon-theme-name=", "")
        th = lineas[2].replace("gtk-theme-name=", "")
        cu = lineas[3].replace("gtk-cursor-theme-name=", "")

        g.close()

        # icon theme ---------
        labelIcon = Gtk.Label()
        labelIcon.set_markup("<span size='x-large'>Icon theme</span>")
        labelIcon.set_margin_top(30)

        comBoxI = Gtk.ComboBoxText()
        comBoxI.set_margin_top(30)

        iconThemes = os.listdir(icons_file)

        for icTheme in iconThemes:
            comBoxI.append_text(icTheme)
        
        actual_icon_theme_index = iconThemes.index(ic.replace("\n", ""))
        comBoxI.set_active(actual_icon_theme_index)

        comBoxI.connect("changed", self.on_comBoxI_changed)

        # global theme ---------
        labelGlobal = Gtk.Label()
        labelGlobal.set_markup("<span size='x-large'>Global theme</span>")
        labelGlobal.set_margin_top(30)

        comBoxG = Gtk.ComboBoxText()
        comBoxG.set_margin_top(30)

        globalThemes = os.listdir(themes_file)

        for icTheme in globalThemes:
            comBoxG.append_text(icTheme)
        
        actual_global_theme_index = globalThemes.index(th.replace("\n", ""))
        comBoxG.set_active(actual_global_theme_index)

        comBoxG.connect("changed", self.on_comBoxG_changed)

        # cursor theme ---------
        labelCur = Gtk.Label()
        labelCur.set_markup("<span size='x-large'>Cursor theme</span>")
        labelCur.set_margin_top(30)

        comBoxC = Gtk.ComboBoxText()
        comBoxC.set_margin_top(30)

        cursorThemes = os.listdir(icons_file)

        for cuTheme in cursorThemes:
            comBoxC.append_text(cuTheme)
        
        actual_cursor_theme_index = cursorThemes.index(cu.replace("\n", ""))
        comBoxC.set_active(actual_cursor_theme_index)

        comBoxC.connect("changed", self.on_comBoxC_changed)

        # ----------------------
        gridAp.attach(labelQtile, 0,0,1,1)
        gridAp.attach(comBoxQ, 1,0,1,1)
        gridAp.attach(labelIcon, 0,1,1,1)
        gridAp.attach(comBoxI, 1,1,1,1)
        gridAp.attach(labelGlobal, 0,2,1,1)
        gridAp.attach(comBoxG, 1,2,1,1)
        gridAp.attach(labelCur, 0,3,1,1)
        gridAp.attach(comBoxC, 1,3,1,1)

        nameAp = "Appearance"
        titleAp = "Appearance"
        stack.add_titled(gridAp, nameAp, titleAp)

    # switch wifi ----------------------
    def on_switch_activated(self, mySwitch, gparam):
        if mySwitch.get_active():
            os.system("nmcli n on")
        else:
            os.system("nmcli n off")
    
    # scale sound ----------------------
    def scale_moved(self, event):
        vol = (int(self.scaleSound.get_value()))

        cmd = "amixer set Master " + str(vol) + "%"
        os.system(cmd)
    
    # combo box qtile theme ----------
    def on_comBoxQ_changed(self, combo):
        myIter = combo.get_active_iter()
        model = combo.get_model()
        theme = model[myIter][0]
        
        with open("/home/josema/.config/qtile/config.json", "w") as f:
            newTheme = '''{"theme": "''' + theme + '''"}'''
            f.write(newTheme)
        
        os.system("xdotool key Super_L+shift+r") # restart qtile
        os.system("notify-send 'Theme has changed'")
    
    # combo box icon theme -----------
    def on_comBoxI_changed(self, combo):
        myIter = combo.get_active_iter()
        model = combo.get_model()
        theme = model[myIter][0]
        
        f = open(self.config_file, "r")
        lines = f.readlines()
        lines[1] = "gtk-icon-theme-name=" + theme + "\n"

        f = open(self.config_file, "w")
        f.writelines(lines)
        f.close()
    
    # combo box icon theme -----------
    def on_comBoxG_changed(self, combo):
        myIter = combo.get_active_iter()
        model = combo.get_model()
        theme = model[myIter][0]
        
        f = open(self.config_file, "r")
        lines = f.readlines()
        lines[2] = "gtk-theme-name=" + theme + "\n"

        f = open(self.config_file, "w")
        f.writelines(lines)
        f.close()
    
    # combo box cursor theme ---------
    def on_comBoxC_changed(self, combo):
        myIter = combo.get_active_iter()
        model = combo.get_model()
        theme = model[myIter][0]
        
        f = open(self.config_file, "r")
        lines = f.readlines()
        lines[3] = "gtk-cursor-theme-name=" + theme + "\n"

        g = open(self.config_file, "w")
        g.writelines(lines)
        g.close()

        g = open(self.cursor_file, "r")
        lines = g.readlines()
        lines[1] = "Inherits=" + theme + "\n"

        g = open(self.cursor_file, "w")
        g.writelines(lines)
        g.close()

        os.system("xdotool key Super_L+shift+r") # restart qtile





if __name__ == "__main__":
    window = myApp()
    window.show_all()
    window.set_title("settings")
    Gtk.main()