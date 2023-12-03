# import all the required modules
from tkinter import *
from tkinter import font
from tkinter import ttk
import json


# GUI Classes

class SearchPage:
	# constructor method
	def __init__(self):
	
		# Declare tkinter window and configure
		self.Window = Tk()
		self.Window.title("DB Search")
		self.Window.minsize(1280, 720)

		# Place spacer before category label so category label covers it
		self.Spacer1 = Label(self.Window).grid(row=0, column=0, padx=2, pady=10)


		# Create category name to inform user what kind of input they should have
		self.MultivaluedLabel = Label(self.Window,
									  text="Multivalued Parameters: Input either a signle value or multiple values "
										  + "seperated by commas (e.g. value1,value2,value3)",
									  font = "Helvetica 16").place(x=0, y=0)

		# create a Label
		self.labelInput1 = Label(self.Window,
							text = "Developer Name(s): ",
							font = "Helvetica 12").grid(row=1, column=0, padx=2, pady=2)
		
		# create a entry box for typing the input
		self.InputText1 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText1.grid(row=1, column=1, padx=2, pady=2)

		# create a Label
		self.labelInput2 = Label(self.Window,
							text = "Genre Name(s): ",
							font = "Helvetica 12").grid(row=1, column=2, padx=2, pady=2)
		
		# create a entry box for typing the input
		self.InputText2 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText2.grid(row=1, column=3, padx=2, pady=2)

		# create a Label
		self.labelInput3 = Label(self.Window,
							text = "Store Name(s): ",
							font = "Helvetica 12").grid(row=1, column=4, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText3 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText3.grid(row=1, column=5, padx=2, pady=2)


		# create a Label
		self.labelInput4 = Label(self.Window,
							text = "Platform Name(s): ",
							font = "Helvetica 12").grid(row=2, column=0, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText4 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText4.grid(row=2, column=1, padx=2, pady=2)

		# create a Label
		self.labelInput5 = Label(self.Window,
								 text="Parent Platform(s): ",
								 font="Helvetica 12").grid(row=2, column=2, padx=2, pady=2)

		# create a entry box for
		# typing the input
		self.InputText5 = Entry(self.Window,
								font="Helvetica 14")

		self.InputText5.grid(row=2, column=3, padx=2, pady=2)

		# Place spacer before category label so category label covers it
		self.Spacer1 = Label(self.Window).grid(row=3, column=0, padx=2, pady=10)


		# Create category name to inform user what kind of input they should have
		self.SingleValuedLabel = Label(self.Window,
									  text="Single Valued Parameters: Input either a signle value only",
									  font = "Helvetica 16").place(x=0, y=100)

		# create a Label
		self.labelInput6 = Label(self.Window,
							text = "Game Title: ",
							font = "Helvetica 12").grid(row=4, column=0, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText6 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText6.grid(row=4, column=1, padx=2, pady=2)


		# create a Label
		self.labelInput7 = Label(self.Window,
							text = "Playtime: ",
							font = "Helvetica 12").grid(row=4, column=2, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText7 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText7.grid(row=4, column=3, padx=2, pady=2)

		# create a Label
		self.labelInput8 = Label(self.Window,
							text = "ESRB Rating: ",
							font = "Helvetica 12").grid(row=4, column=4, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText8 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText8.grid(row=4, column=5, padx=2, pady=2)


		# create a Label
		self.labelInput9 = Label(self.Window,
							text = "Metacritic Rating: ",
							font = "Helvetica 12").grid(row=5, column=0, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText9 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText9.grid(row=5, column=1, padx=2, pady=2)


		# create a Label
		self.labelInput10 = Label(self.Window,
							text = "User Rating: ",
							font = "Helvetica 12").grid(row=5, column=2, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText10 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText10.grid(row=5, column=3, padx=2, pady=2)


		# create a Label
		self.labelInput11 = Label(self.Window,
							text = "Release Date: ",
							font = "Helvetica 12").grid(row=5, column=4, padx=2, pady=2)
		
		# create a entry box for
		# typing the input
		self.InputText11 = Entry(self.Window,
							font = "Helvetica 14")

		self.InputText11.grid(row=5, column=5, padx=2, pady=2)
		
		# create a Search Button along with action
		self.go = Button(self.Window,
						text = "Search",
						font = "Helvetica 20 bold",
						command = lambda: Search(self, self.InputText1.get(), self.InputText2.get(), self.InputText3.get(), self.InputText4.get(), self.InputText5.get(), self.InputText6.get(), self.InputText7.get(), self.InputText8.get(), self.InputText9.get(), self.InputText10.get(), self.InputText11.get()))
		
		self.go.grid(row=6, column=0, padx=2, pady=2)

		self.Window.mainloop()

class SearchResultsPage():

	# Constructor
	def __init__(self, results):

		# Declare tkinter window and configure
		self.window = Tk()
		self.window.title("DB Search Results")
		self.window.minsize(1280, 720)

		self.HorizontalScroll = Scrollbar(self.window, orient='horizontal')
		self.VerticalScroll = Scrollbar(self.window)

		self.ResultsBox = Listbox(self.window,
								  font="Helvetica 14",
								  height=len(results),
								  selectmode=MULTIPLE,
								  width=100,
								  xscrollcommand = self.HorizontalScroll.set,
								  yscrollcommand = self.VerticalScroll.set)

		self.HorizontalScroll.config(command = self.ResultsBox.xview())
		self.VerticalScroll.config(command=self.ResultsBox.yview())

		i=1
		for item in results:
			self.ResultsBox.insert(i, item)
			i += 1

		self.HorizontalScroll.pack(side=BOTTOM, fill=X)
		self.VerticalScroll.pack(side=RIGHT, fill=Y)
		self.ResultsBox.pack()

		self.Instructions = Label(self.window,
								  text="Select all records you want to store in your wishlist.",
								  font= "Helvetica 16").pack()

		self.WishlistButton = Button(self.window,
									 text="Add to wishlist",
									 font="Helvetica 20 bold",
									 command= lambda: AddToWishlist(self, self.ResultsBox.curselection()),
									 width=20,
									 height=5).pack()

		self.window.mainloop()

class WishlistPage():

	# Constructor
	def __init__(self, results):
		# Declare tkinter window and configure
		self.window = Tk()
		self.window.title("DB Wishlist")
		self.window.minsize(1280, 720)

		self.HorizontalScroll = Scrollbar(self.window, orient='horizontal')
		self.VerticalScroll = Scrollbar(self.window)

		self.WishlistBox = Listbox(self.window,
								  font="Helvetica 14",
								  height=len(results),
								  selectmode=MULTIPLE,
								  width=100,
								  xscrollcommand=self.HorizontalScroll.set,
								  yscrollcommand=self.VerticalScroll.set)

		self.HorizontalScroll.config(command=self.WishlistBox.xview())
		self.VerticalScroll.config(command=self.WishlistBox.yview())

		i = 1
		for item in results:
			self.WishlistBox.insert(i, item)
			i += 1

		self.HorizontalScroll.pack(side=BOTTOM, fill=X)
		self.VerticalScroll.pack(side=RIGHT, fill=Y)
		self.WishlistBox.pack()

		self.Instructions = Label(self.window,
								  text="Select all records you want remove from your wishlist.",
								  font="Helvetica 16").pack()

		self.WishlistButton = Button(self.window,
									 text="Remove from wishlist",
									 font="Helvetica 20 bold",
									 command=lambda: RemoveFromWishlist(self, results, self.WishlistBox.curselection()),
									 width=20,
									 height=5).pack()

		self.CloseButton = Button(self.window,
									 text="Close wishlist",
									 font="Helvetica 20 bold",
									 command=lambda: self.window.destroy(),
									 width=20,
									 height=5).pack()

		self.window.mainloop()

class HomePage():

	# Constructor
	def __init__(self):

		# Declare tkinter window and configure
		self.window = Tk()
		self.window.title("DB Home Page")
		self.window.minsize(1280,720)

		# Create Links to our functionalities
		self.SearchButton = Button(self.window, text="Search", font="Helvetica 20 bold", command=SearchPage, width=80, height=7).pack()
		self.WishlistButton = Button(self.window, text="Wishlist", font="Helvetica 20 bold", command=StartWishlist, width=80, height=7).pack()
		self.UpdateButton = Button(self.window, text="Update", font="Helvetica 20 bold", command=SearchPage, width=80, height=7).pack()

		self.window.mainloop()

# Functions for buttons

def Search(self, devname, genname, stoname, platname, parentplat, gamtitl, playtime, esrbrate, metacritrate, userrate, reldate):
	# Placeholder until we get actual logic
	print(devname)
	print(genname)
	print(stoname)
	print(platname)
	print(parentplat)
	print(gamtitl)
	print(playtime)
	print(esrbrate)
	print(metacritrate)
	print(userrate)
	print(reldate)
	g = SearchResultsPage([[devname, genname, stoname, platname]])

def AddToWishlist(self, records):

	# Open wishlist JSON if exists otherwise start fresh and dump to directory
	try:
		with open('wishlist.json', 'r') as file:
			writeDict = json.load(file)
	except:
		writeDict = {'stored':[]}

	for record in records:
		writeDict['stored'].append(self.ResultsBox.get(record))

	json.dump(writeDict, open("wishlist.json", "w"))

	self.window.destroy()

def StartWishlist():
	# We load the JSON here and then grab all keys (game_ids) and then search them in database and output to form for listbox
	try:
		with open('wishlist.json', 'r') as file:
			wishlist = json.load(file)
			listpassthrough = wishlist['stored']
	except:
		listpassthrough = []
    
	g = WishlistPage(listpassthrough)

def RemoveFromWishlist(self, totalrecords, removalrecords):
  
	recordsToBeRemoved = []
	recordsToBeKept = []
	writeDict = {}
  
	for record in removalrecords:
		recordsToBeRemoved.append(self.WishlistBox.get(record)[0])
	for record in totalrecords:
		if record[0] not in recordsToBeRemoved:
			recordsToBeKept.append(record[0])
      
	writeDict['stored'] = recordsToBeKept
	print(writeDict)
	json.dump(writeDict, open("wishlist.json", "w"))
  
	self.window.destroy()

# create a GUI class object
g = HomePage()
