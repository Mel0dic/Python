import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from viginere import *

class MyWindow(Gtk.Window):

	def __init__(self):
		self.keyword = ""
		self.ctext = ""
		Gtk.Window.__init__(self, title="Window")
		self.set_border_width(10)
		self.set_size_request(350, 100)

		self.timeout_id = None

		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(vbox)

		self.entry = Gtk.Entry()
		self.entry.set_text("Enter Cipher Text")
		vbox.pack_start(self.entry, True, True, 0)

		hbox = Gtk.Box(spacing=6)
		vbox.pack_start(hbox, True, True, 0)

		button = Gtk.Button.new_with_label(label="Accept Text")
		button.connect("clicked", self.textAccepted)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_label(label="Accept Key")
		button.connect("clicked", self.keyAccepted)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_label(label="Enter")
		button.connect("clicked", self.returnWord)
		hbox.pack_start(button, True, True, 0)

	def textAccepted(self, widget):
		widget.set_label("Button Pressed")
		self.ctext = self.entry.get_text()

	def keyAccepted(self, widget):
		widget.set_label("Button Pressed")
		self.keyword = self.entry.get_text()

	def returnWord(self, widget):
		viginere(self.keyword, self.ctext)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()