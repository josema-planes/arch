#!/usr/bin/env python

import gi

import os
import subprocess

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class myApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(350, 150)
        self.connect("destroy", Gtk.main_quit)
        #self.set_border_width(20)

        grid = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        self.add(grid)

        # header bar ----------------------------
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        self.set_titlebar(hb)

        # -------------

        label1 = Gtk.Label()
        label1.set_markup("<span size='x-large'>What do you want to do?</span>")
        label1.set_justify(Gtk.Justification.FILL)
        label1.set_margin_bottom(30)
        label1.set_margin_left(240)

        logout = Gtk.Button()
        logout.set_label("Log out")
        logout.set_hexpand(True)
        logout.set_vexpand(False)
        logout.connect("clicked", self.on_logout_clicked)

        reboot = Gtk.Button()
        reboot.set_label("Reboot")
        reboot.set_hexpand(True)
        reboot.set_vexpand(False)
        reboot.connect("clicked", self.on_reboot_clicked)

        shutdown = Gtk.Button()
        shutdown.set_label("Shutdown")
        shutdown.set_hexpand(True)
        shutdown.set_vexpand(False)
        shutdown.connect("clicked", self.on_shutdown_clicked)

        grid.attach(label1, 0,0,2,3)
        grid.attach(logout, 0,2,1,1)
        grid.attach(reboot, 1,2,1,1)
        grid.attach(shutdown, 2,2,1,1)

    def on_shutdown_clicked(self, button):
        os.system("shutdown now")
    
    def on_reboot_clicked(self, button):
        os.system("reboot")
    
    def on_logout_clicked(self, button):
        os.system("xdotool key Super_L+Shift+Escape")



if __name__ == "__main__":
    window = myApp()
    window.show_all()
    window.set_title("settings")
    Gtk.main()