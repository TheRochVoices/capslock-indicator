import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator
import signal
import sys
import os

APPINDICATOR_ID = 'myappindicator'

def build_menu():
   	menu = gtk.Menu()
	item_quit = gtk.MenuItem('Quit')
    	item_quit.connect('activate', quit)
    	menu.append(item_quit)
    	menu.show_all()
    	return menu
 
def quit(source):
    	gtk.main_quit()

def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID, gtk.STOCK_INFO, appindicator.IndicatorCategory.SYSTEM_SERVICES)
        indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    	indicator.set_menu(build_menu())
    	gtk.main()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)
    	main() 	
