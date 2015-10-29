#!/usr/bin/python
from gi.repository import Gtk

class Display(Gtk.Window):
    
    def __init(self):


disp = Display()
disp.connect("delete-event",Gtk.main_quit)
disp.show_all()
Gtk.main()
