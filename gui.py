# import all the required modules
from tkinter import *
from tkinter import font
from tkinter import ttk


# GUI class for the db app
class GUI:
	# constructor method
	def __init__(self):
	
		# window which is currently hidden
		self.Window = Tk()
		self.Window.withdraw()
		self.Window.deiconify()
		# set the title
		self.Window.title("DB Search")
		self.Window.resizable(width = False,
							height = False)
		self.Window.configure(width = 800,
							height = 600)
		# create a Label
		self.pls = Label(self.Window,
					text = "Welcome to the DB search Application.",
					justify = CENTER,
					font = "Helvetica 14 bold")
		
		self.pls.place(relheight = 0.15, relx = 0.3,
					rely = 0.01)
		# create a Label
		self.labelInput = Label(self.Window,
							text = "Input: ",
							font = "Helvetica 12")
		
		self.labelInput.place(relheight = 0.05,
							relx = 0.2,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText.place(relwidth = 0.4,
							relheight = 0.05,
							relx = 0.3,
							rely = 0.15)


		# create a Label
		self.labelcombo = Label(self.Window,
							text = "Search by: ",
							font = "Helvetica 12")

		self.labelcombo.place(relheight = 0.05,
							relx = 0.2,
							rely = 0.2)

		self.combo = ttk.Combobox(self.Window,
			state="readonly",
			values=["Developer name", "Genre name", "Store name", "Platform name", "Game title", "Playtime", "System family", "ESRB rating", "Metacritic rating", "User rating", "Release date"]
		)

		self.combo.place(relwidth = 0.4,
                                                        relheight = 0.05,
                                                        relx = 0.3,
                                                        rely = 0.2)
		# create a Label
		self.labelcombo2 = Label(self.Window,
							text = "Update Method: ",
							font = "Helvetica 12")

		self.labelcombo2.place(relheight = 0.05,
							relx = 0.18,
							rely = 0.25)

		self.combo2 = ttk.Combobox(self.Window,
			state="readonly",
			values=["Proceedure", "Direct"]
		)

		self.combo2.place(relwidth = 0.4,
							relheight = 0.05,
							relx = 0.3,
							rely = 0.25)


		# set the focus of the cursor
		self.InputText.focus()
		
		# create a Search Button
		# along with action
		self.go = Button(self.Window,
						text = "SEARCH",
						font = "Helvetica 14 bold",
						command = lambda: self.goAhead(self.InputText.get(), self.combo.get()))
		
		self.go.place(relx = 0.1,
					rely = 0.3)
		# create a Search Button
		# along with action
		self.loadw = Button(self.Window,
						text = "Load Wishlist",
						font = "Helvetica 14 bold",
						command = lambda: self.loadWishlist(self.InputText.get()))

		self.loadw.place(relx = 0.25,
					rely = 0.3)


		# create a Search Button
		# along with action
		self.addw = Button(self.Window,
						text = "Add to wishlist",
						font = "Helvetica 14 bold",
						command = lambda: self.addToWishlist(self.InputText.get()))

		self.addw.place(relx = 0.45,
					rely = 0.3)

		# create a Search Button
		# along with action
		self.updateb = Button(self.Window,
						text = "Update",
						font = "Helvetica 14 bold",
						command = lambda: self.update(self.InputText.get(), self.combo2.get()))

		self.updateb.place(relx = 0.65,
					rely = 0.3)

		self.InputText.bind('<Return>', self.callback1)

		# create a Label
		self.labelResults = Label(self.Window,
							text = "Results",
							font = "Helvetica 12")
		
		self.labelResults.place(relheight = 0.05,
							relx = 0.25,
							rely = 0.35)

		# create a Label
		self.labelWishlist = Label(self.Window,
							text = "Wishlist",
							font = "Helvetica 12")
		
		self.labelWishlist.place(relheight = 0.05,
							relx = 0.65,
							rely = 0.35)

		self.results = Text(self.Window,
							width = 20,
							height = 2,
							font = "Helvetica 14",
							padx = 5,
							pady = 5)
		
		self.results.place(relheight = 0.6,
							relwidth = 0.35,
							rely = 0.4, relx = 0.1)

		self.wishlist = Text(self.Window,
							width = 20,
							height = 2,
							font = "Helvetica 14",
							padx = 5,
							pady = 5)
		
		self.wishlist.place(relheight = 0.6,
							relwidth = 0.35,
							rely = 0.4, relx = 0.5)

		# create a scroll bar
		scrollbar = Scrollbar(self.results)
		
		# place the scroll bar
		# into the gui window
		scrollbar.place(relheight = 1,
						relx = 0.974)

		# create a scroll bar
		scrollbar2 = Scrollbar(self.wishlist)
		
		# place the scroll bar
		# into the gui window
		scrollbar2.place(relheight = 1,
						relx = 0.974)

		scrollbar.config(command = self.results.yview)
		scrollbar2.config(command = self.wishlist.yview)

		self.Window.mainloop()

	def callback1(self, event):
		self.goAhead(self.InputText.get(), self.combo.get())


	# def goAhead(self, input, searchby):
        # the stuff to do when searching

	# def loadWishlst(self, input):
	# the stuff to do when loading a wishlist

	# def addToWishlist(self, input):
	# the stuff to do adding an entry to the wishlist

	# def update(self, input, umethod):
	# the stuff to do when performing updates

# create a GUI class object
g = GUI()
