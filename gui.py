# import all the required modules
from tkinter import *
from tkinter import font
from tkinter import ttk

import os
import mysql.connector
import json

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Setting up Database Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Change this to your directory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
path_to_games = "C:/Users/Nick/Desktop/Python/Project/gamedata/"

with open("connectorConfig.json", "r") as f:
    config = json.load(f)
connection_config = config["mysql"]
data_base = mysql.connector.connect(**connection_config)

# Preparing a cursor object to use throughout app
cursor_object = data_base.cursor()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Opening Wishlist/Creating it if it doesn't exist or is empty
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

wishlist = {}

try: 
	with open('wishlist.json', 'r') as file:
		# Reading from json file
		# Opened Wishlist
		wishlist = json.load(file)
except:
    with open('wishlist.json', 'w') as file:
        print("Created Wishlist")


"""
~~~~~~~~~~~~~~
Setting up App
~~~~~~~~~~~~~~
"""

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
		self.Window.configure(width = 1400,
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
							relx = 0.04,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.07,
							rely = 0.15)

		# create a Label
		self.labelInput1 = Label(self.Window,
							text = "Dev name: ",
							font = "Helvetica 12")
		
		self.labelInput1.place(relheight = 0.05,
							relx = 0.17,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText1 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText1.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.22,
							rely = 0.15)

		# create a Label
		self.labelInput2 = Label(self.Window,
							text = "Genre name: ",
							font = "Helvetica 12")
		
		self.labelInput2.place(relheight = 0.05,
							relx = 0.32,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText2 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText2.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.38,
							rely = 0.15)


		# create a Label
		self.labelInput3 = Label(self.Window,
							text = "Store name: ",
							font = "Helvetica 12")
		
		self.labelInput3.place(relheight = 0.05,
							relx = 0.48,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText3 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText3.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.54,
							rely = 0.15)


		# create a Label
		self.labelInput4 = Label(self.Window,
							text = "Platform name: ",
							font = "Helvetica 12")
		
		self.labelInput4.place(relheight = 0.05,
							relx = 0.64,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText4 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText4.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.71,
							rely = 0.15)


		# create a Label
		self.labelInput5 = Label(self.Window,
							text = "Game title: ",
							font = "Helvetica 12")
		
		self.labelInput5.place(relheight = 0.05,
							relx = 0.81,
							rely = 0.15)
		
		# create a entry box for
		# typing the input
		self.InputText5 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText5.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.86,
							rely = 0.15)


		# create a Label
		self.labelInput6 = Label(self.Window,
							text = "Playtime: ",
							font = "Helvetica 12")
		
		self.labelInput6.place(relheight = 0.05,
							relx = 0.04,
							rely = 0.2)
		
		# create a entry box for
		# typing the input
		self.InputText6 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText6.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.08,
							rely = 0.2)


		# create a Label
		self.labelInput7 = Label(self.Window,
							text = "System family: ",
							font = "Helvetica 12")
		
		self.labelInput7.place(relheight = 0.05,
							relx = 0.18,
							rely = 0.2)
		
		# create a entry box for
		# typing the input
		self.InputText7 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText7.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.24,
							rely = 0.2)


		# create a Label
		self.labelInput8 = Label(self.Window,
							text = "ESRB rating: ",
							font = "Helvetica 12")
		
		self.labelInput8.place(relheight = 0.05,
							relx = 0.34,
							rely = 0.2)
		
		# create a entry box for
		# typing the input
		self.InputText8 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText8.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.39,
							rely = 0.2)


		# create a Label
		self.labelInput9 = Label(self.Window,
							text = "Metacritic rating: ",
							font = "Helvetica 12")
		
		self.labelInput9.place(relheight = 0.05,
							relx = 0.49,
							rely = 0.2)
		
		# create a entry box for
		# typing the input
		self.InputText9 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText9.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.56,
							rely = 0.2)


		# create a Label
		self.labelInput10 = Label(self.Window,
							text = "User rating: ",
							font = "Helvetica 12")
		
		self.labelInput10.place(relheight = 0.05,
							relx = 0.66,
							rely = 0.2)
		
		# create a entry box for
		# typing the input
		self.InputText10 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText10.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.71,
							rely = 0.2)


		# create a Label
		self.labelInput11 = Label(self.Window,
							text = "Release date: ",
							font = "Helvetica 12")
		
		self.labelInput11.place(relheight = 0.05,
							relx = 0.81,
							rely = 0.2)
		
		# create a entry box for
		# typing the input
		self.InputText11 = Entry(self.Window,
							font = "Helvetica 14")
		
		self.InputText11.place(relwidth = 0.1,
							relheight = 0.05,
							relx = 0.87,
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
			values=["Procedure", "Direct"]
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
						command = lambda: self.goAhead(self.InputText1.get(), self.InputText2.get(), self.InputText3.get(), self.InputText4.get(), self.InputText5.get(), self.InputText6.get(), self.InputText7.get(), self.InputText8.get(), self.InputText9.get(), self.InputText10.get(), self.InputText11.get()))
		
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

		# The results list
		self.results = Listbox(self.Window,
							width = 20,
							height = 2,
							font = "Helvetica 14",
							)
		
		self.results.place(relheight = 0.6,
							relwidth = 0.35,
							rely = 0.4, relx = 0.1)

		
		# The wishlist list
		self.wishlist = Listbox(self.Window,
							width = 20,
							height = 2,
							font = "Helvetica 14",
							)
		
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

		# Loads the first 100 rows of the game table for users to look at and populates the wishlist if there is anything already in it upon startup
		initial_statement = """
							select title, playtime, first_release_date, ESRB_rating, metacritic_rating, user_rating, name AS Developer, genre
							from game g join gamedeveloper gd on g.game_id = gd.game_id
								join developer d on d.developer_id = gd.developer_id
								join gamegenre gg on g.game_id = gg.game_id
								join genre gen on gg.genre_id = gen.genre_id
							limit 100
							"""
		cursor_object.execute(initial_statement)
		initial_list = cursor_object.fetchall()
  
		for game in initial_list:
			self.results.insert(END, game)
  
		self.Window.mainloop()

	def callback1(self, event):
		self.goAhead(self.InputText1.get(), self.InputText2.get(), self.InputText3.get(), self.InputText4.get(), self.InputText5.get(), self.InputText6.get(), self.InputText7.get(), self.InputText8.get(), self.InputText9.get(), self.InputText10.get(), self.InputText11.get())

 
	# Function for searching
	def goAhead(self, devname, genrename, storename, platformname, gametitle, playtime, systemfamily, esrbrate, metacritrate, userrate, releasedate):
		
		return
    
	# Function for loading a wishlist (Not sure what the point of this is, it should autoload no?)
	def loadWishlist(self, input):
		print("Loaded")
		return

	# Function for adding an entry to a wishlist
	def addToWishlist(self, input):
		# Get the index of the selected item
		index = self.results.curselection()
		
		if index:  # Check if an item is selected
			# Get the tuple at the selected index
			selected_tuple = self.results.get(index)
			game = list(selected_tuple)
			
			print(f"Selected tuple: {selected_tuple}")
			with open ("wishlist.json", 'w') as file:
				json.dump(wishlist, file, indent = 4)

		else:
			print("No item selected")
		return
	
 	# Empty update function
	def update(self, input, umethod):
		# Get the index of the selected item
		index = self.results.curselection()
		
		if index:  # Check if an item is selected
			# Get the tuple at the selected index
			selected_tuple = self.results.get(index)
			print(f"Selected tuple: {selected_tuple}")
		else:
			print("No item selected")
			search_statement = ""
		return


# create a GUI class object
g = GUI()
