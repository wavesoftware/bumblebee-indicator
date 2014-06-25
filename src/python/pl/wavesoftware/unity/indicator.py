
import sys
import gtk
import appindicator

class BumblebeeIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator("new-gmail-indicator",
                                           "indicator-messages",
                                           appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")

        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()
        
        self.dual_item = gtk.MenuItem("Dual screen: on")
        self.dual_item.show()
        self.menu.append(self.dual_item)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        gtk.main()

    def quit(self, widget):
        sys.exit(0)
