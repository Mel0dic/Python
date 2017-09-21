import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from viginere import viginere

class MyWindow(Gtk.ApplicationWindow):

	def __init__(self, app):

		Gtk.Window.__init__(self, title="Window", application=app)
		self.set_border_width(10)
		self.set_size_request(400, 100)

		self.keyword = ""
		self.ctext = ""

		self.timeout_id = None

		# a button
		button1 = Gtk.Button(label="Enter Text")
		button1.connect("clicked", self.textAccepted)
		button2 = Gtk.Button(label="Enter Key")
		button2.connect("clicked", self.keyAccepted)
		button3 = Gtk.Button(label="Encode")
		button3.connect("clicked", self.returnWord)

		self.statusbar = Gtk.Statusbar()
		self.context_id = self.statusbar.get_context_id("example")
		self.statusbar.push(self.context_id, "               Waiting for you to do something...")

		self.entry = Gtk.Entry()
		self.entry.set_text("Enter Cipher Text")

		# a grid to attach the widgets
		grid = Gtk.Grid()
		grid.set_row_spacing(5)
		grid.set_column_spacing(5)
		grid.set_column_homogeneous(True)
		grid.set_row_homogeneous(True)
		grid.attach(self.entry, 0, 0, 3, 1)
		grid.attach(button1, 0, 1, 1, 1)
		grid.attach(button2, 1, 1, 1, 1)
		grid.attach(button3, 2, 1, 1, 1)
		grid.attach(self.statusbar, 0, 2, 3, 1)

		# add the grid to the window
		self.add(grid)

	def textAccepted(self, widget):
		widget.set_label("Button Pressed")
		self.ctext = self.entry.get_text()

	def keyAccepted(self, widget):
		widget.set_label("Button Pressed")
		self.keyword = self.entry.get_text()

	def returnWord(self, widget):
		ciph = viginere(self.keyword, self.ctext)
		print(ciph)
		self.statusbar.push(self.context_id, ciph)

class MyApplication(Gtk.Application):
	def __init__(self):
		Gtk.Application.__init__(self)

	def do_activate(self):
		win = MyWindow(self)
		win.show_all()

	def do_startup(self):
		Gtk.Application.do_startup(self)


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)