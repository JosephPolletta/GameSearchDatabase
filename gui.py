# Import all the required modules
import tkinter.messagebox
from tkinter import *
import json
import os
import mysql.connector
from tkinter import ttk


# GUI Classes
class SearchPage:

    # Constructor
    def __init__(self):
        # Declare tkinter window and configure
        self.Window = Tk()
        self.Window.title("DB Search")
        self.Window.minsize(1280, 720)

        # Place spacer before category label so category label covers it
        self.Spacer1 = Label(self.Window).grid(row=0, column=0, padx=2, pady=10)

        # Create category name to inform user what kind of input they should have
        self.MultivaluedLabel = Label(self.Window,
                                      text="Multivalued Parameters: Input either a single value or multiple values "
                                           + "seperated by commas (e.g. value1,value2,value3)",
                                      font="Helvetica 16").place(x=0, y=0)

        # create a Label
        self.labelInput1 = Label(self.Window,
                                 text="Developer Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=0, padx=2, pady=2)

        # create a entry box for typing the input
        self.InputText1 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText1.grid(row=1, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput2 = Label(self.Window,
                                 text="Genre Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=2, padx=2, pady=2)

        # create a entry box for typing the input
        self.InputText2 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText2.grid(row=1, column=3, padx=2, pady=2)

        # create a Label
        self.labelInput3 = Label(self.Window,
                                 text="Store Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=4, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText3 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText3.grid(row=1, column=5, padx=2, pady=2)

        # create a Label
        self.labelInput4 = Label(self.Window,
                                 text="Platform Name(s): ",
                                 font="Helvetica 12").grid(row=2, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText4 = Entry(self.Window,
                                font="Helvetica 14")

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
                                       text="Single Valued Parameters: Input a single value only",
                                       font="Helvetica 16").place(x=0, y=100)

        # create a Label
        self.labelInput6 = Label(self.Window,
                                 text="Game Title: ",
                                 font="Helvetica 12").grid(row=4, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText6 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText6.grid(row=4, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput7 = Label(self.Window,
                                 text="Playtime: ",
                                 font="Helvetica 12").grid(row=4, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText7 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText7.grid(row=4, column=3, padx=2, pady=2)

        # create a Label
        self.labelInput8 = Label(self.Window,
                                 text="ESRB Rating: ",
                                 font="Helvetica 12").grid(row=4, column=4, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText8 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText8.grid(row=4, column=5, padx=2, pady=2)

        self.InputText8.grid(row=4, column=5, padx=2, pady=2)

        # create a Label
        self.labelInput9 = Label(self.Window,
                                 text="Metacritic Rating: ",
                                 font="Helvetica 12").grid(row=5, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.MetaCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14")

        self.MetaCombo['values'] = ('Greater than or equal to',
                                    'Less than or equal to')

        self.MetaCombo.current(0)
        self.MetaCombo.grid(row=5, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText9 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText9.grid(row=5, column=2, padx=2, pady=2)

        # create a Label
        self.labelInput10 = Label(self.Window,
                                  text="User Rating: ",
                                  font="Helvetica 12").grid(row=6, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.UserCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14")

        self.UserCombo['values'] = ('Greater than or equal to',
                                    'Less than or equal to')

        self.UserCombo.current(0)
        self.UserCombo.grid(row=6, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText10 = Entry(self.Window,
                                 font="Helvetica 14")

        self.InputText10.grid(row=6, column=2, padx=2, pady=2)

        # create a Label
        self.labelInput11 = Label(self.Window,
                                  text="Release Date: ",
                                  font="Helvetica 12").grid(row=7, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText11 = Entry(self.Window,
                                 font="Helvetica 14")

        self.InputText11.grid(row=7, column=1, padx=2, pady=2)

        # create a Search Button along with action
        self.go = Button(self.Window,
                         text="Search",
                         font="Helvetica 20 bold",
                         command=lambda: Search(self, self.InputText1.get(), self.InputText2.get(),
                                                self.InputText3.get(), self.InputText4.get(), self.InputText5.get(),
                                                self.InputText6.get(), self.InputText7.get(), self.InputText8.get(),
                                                self.InputText9.get(), self.InputText10.get(), self.InputText11.get()))

        self.go.grid(row=8, column=0, padx=2, pady=2)

        self.Window.mainloop()


class SearchResultsPage:

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
                                  height=20,
                                  selectmode=MULTIPLE,
                                  width=100,
                                  xscrollcommand=self.HorizontalScroll.set,
                                  yscrollcommand=self.VerticalScroll.set)

        self.HorizontalScroll.config(command=self.ResultsBox.xview())
        self.VerticalScroll.config(command=self.ResultsBox.yview())

        self.ResultsBox.insert(1, ['Game ID', 'Title', 'Playtime', 'Release Date', 'ESRB Rating', 'Metacritic Rating',
                                   'User Rating', 'Developer'])

        i = 2
        for item in results:
            self.ResultsBox.insert(i, item)
            i += 1

        self.HorizontalScroll.pack(side=BOTTOM, fill=X)
        self.VerticalScroll.pack(side=RIGHT, fill=Y)
        self.ResultsBox.pack()

        self.Instructions = Label(self.window,
                                  text="Select all records you want to store in your wishlist.",
                                  font="Helvetica 16").pack()

        self.WishlistButton = Button(self.window,
                                     text="Add to wishlist",
                                     font="Helvetica 10 bold",
                                     command=lambda: AddToWishlist(self, self.ResultsBox.curselection()),
                                     width=20,
                                     height=2).pack()

        self.window.mainloop()


class WishlistPage:

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
                                   height=20,
                                   selectmode=MULTIPLE,
                                   width=100,
                                   xscrollcommand=self.HorizontalScroll.set,
                                   yscrollcommand=self.VerticalScroll.set)

        self.HorizontalScroll.config(command=self.WishlistBox.xview())
        self.VerticalScroll.config(command=self.WishlistBox.yview())

        self.WishlistBox.insert(1, ['Game ID', 'Title', 'Playtime', 'Release Date', 'ESRB Rating', 'Metacritic Rating',
                                    'User Rating', 'Developer'])

        i = 2
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
                                     font="Helvetica 10 bold",
                                     command=lambda: RemoveFromWishlist(self, results, self.WishlistBox.curselection()),
                                     width=20,
                                     height=2).pack()

        self.CloseButton = Button(self.window,
                                  text="Close wishlist",
                                  font="Helvetica 10 bold",
                                  command=lambda: self.window.destroy(),
                                  width=20,
                                  height=2).pack()

        self.window.mainloop()


class UpdateSearchPage:

    # Constructor
    def __init__(self):
        # Declare tkinter window and configure
        self.Window = Tk()
        self.Window.title("DB Search for Update")
        self.Window.minsize(1280, 720)

        # Place spacer before category label so category label covers it
        self.Spacer1 = Label(self.Window).grid(row=0, column=0, padx=2, pady=10)

        # Create category name to inform user what kind of input they should have
        self.MultivaluedLabel = Label(self.Window,
                                      text="Multivalued Parameters: Input either a single value or multiple values "
                                           + "seperated by commas (e.g. value1,value2,value3)",
                                      font="Helvetica 16").place(x=0, y=0)

        # create a Label
        self.labelInput1 = Label(self.Window,
                                 text="Developer Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=0, padx=2, pady=2)

        # create a entry box for typing the input
        self.InputText1 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText1.grid(row=1, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput2 = Label(self.Window,
                                 text="Genre Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=2, padx=2, pady=2)

        # create a entry box for typing the input
        self.InputText2 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText2.grid(row=1, column=3, padx=2, pady=2)

        # create a Label
        self.labelInput3 = Label(self.Window,
                                 text="Store Name(s): ",
                                 font="Helvetica 12").grid(row=2, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText3 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText3.grid(row=2, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput4 = Label(self.Window,
                                 text="Platform Name(s): ",
                                 font="Helvetica 12").grid(row=2, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText4 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText4.grid(row=2, column=3, padx=2, pady=2)

        # create a Label
        self.labelInput5 = Label(self.Window,
                                 text="Parent Platform(s): ",
                                 font="Helvetica 12").grid(row=3, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText5 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText5.grid(row=3, column=1, padx=2, pady=2)

        # Place spacer before category label so category label covers it
        self.Spacer1 = Label(self.Window).grid(row=4, column=0, padx=2, pady=10)

        # Create category name to inform user what kind of input they should have
        self.SingleValuedLabel = Label(self.Window,
                                       text="Single Valued Parameters: Input a single value only",
                                       font="Helvetica 16").place(x=0, y=135)

        # create a Label
        self.labelInput6 = Label(self.Window,
                                 text="Game Title: ",
                                 font="Helvetica 12").grid(row=5, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText6 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText6.grid(row=5, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput7 = Label(self.Window,
                                 text="Playtime: ",
                                 font="Helvetica 12").grid(row=5, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText7 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText7.grid(row=5, column=3, padx=2, pady=2)

        # create a Label
        self.labelInput8 = Label(self.Window,
                                 text="ESRB Rating: ",
                                 font="Helvetica 12").grid(row=6, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText8 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText8.grid(row=6, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput9 = Label(self.Window,
                                 text="Metacritic Rating: ",
                                 font="Helvetica 12").grid(row=7, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.MetaCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14")

        self.MetaCombo['values'] = ('Greater than or equal to',
                                    'Less than or equal to')

        self.MetaCombo.current(0)
        self.MetaCombo.grid(row=7, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText9 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText9.grid(row=7, column=2, padx=2, pady=2)

        # create a Label
        self.labelInput10 = Label(self.Window,
                                  text="User Rating: ",
                                  font="Helvetica 12").grid(row=8, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.UserCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14")

        self.UserCombo['values'] = ('Greater than or equal to',
                                    'Less than or equal to')

        self.UserCombo.current(0)
        self.UserCombo.grid(row=8, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText10 = Entry(self.Window,
                                 font="Helvetica 14")

        self.InputText10.grid(row=8, column=2, padx=2, pady=2)

        # create a Label
        self.labelInput11 = Label(self.Window,
                                  text="Release Date: ",
                                  font="Helvetica 12").grid(row=9, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText11 = Entry(self.Window,
                                 font="Helvetica 14")
        self.InputText11.grid(row=9, column=1, padx=2, pady=2)

        # create a Search Button along with action
        self.go = Button(self.Window,
                         text="Search for game to update",
                         font="Helvetica 20 bold",
                         command=lambda: SearchUpdate(self, self.InputText1.get(), self.InputText2.get(),
                                                      self.InputText3.get(), self.InputText4.get(),
                                                      self.InputText5.get(),
                                                      self.InputText6.get(), self.InputText7.get(),
                                                      self.InputText8.get(),
                                                      self.InputText9.get(), self.InputText10.get(),
                                                      self.InputText11.get()))

        self.go.grid(row=10, column=0, padx=2, pady=2)

        self.Window.mainloop()


class SearchResultsUpdatePage:

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
                                  height=20,
                                  selectmode=SINGLE,
                                  width=100,
                                  xscrollcommand=self.HorizontalScroll.set,
                                  yscrollcommand=self.VerticalScroll.set)

        self.HorizontalScroll.config(command=self.ResultsBox.xview())
        self.VerticalScroll.config(command=self.ResultsBox.yview())

        self.ResultsBox.insert(1, ['Game ID', 'Title', 'Playtime', 'Release Date', 'ESRB Rating', 'Metacritic Rating',
                                   'User Rating', 'Developer'])

        i = 2
        for item in results:
            self.ResultsBox.insert(i, item)
            i += 1

        self.HorizontalScroll.pack(side=BOTTOM, fill=X)
        self.VerticalScroll.pack(side=RIGHT, fill=Y)
        self.ResultsBox.pack()

        self.Instructions = Label(self.window,
                                  text="Select the record you want to update.",
                                  font="Helvetica 16").pack()

        self.WishlistButton = Button(self.window,
                                     text="Select record",
                                     font="Helvetica 10 bold",
                                     command=lambda: GrabUpdateRecord(self, self.ResultsBox.curselection()),
                                     width=20,
                                     height=2).pack()

        self.window.mainloop()


class UpdatePage:

    # Constructor
    def __init__(self, record):
        # Declare tkinter window and configure
        self.Window = Tk()
        self.Window.title("DB Search")
        self.Window.minsize(1280, 720)

        # Place spacer before category label so category label covers it
        self.Spacer1 = Label(self.Window).grid(row=4, column=0, padx=2, pady=10)

        # Create category name to inform user what kind of input they should have
        self.SingleValuedLabel = Label(self.Window,
                                       text="Single Valued Parameters: Input a single value only",
                                       font="Helvetica 16").place(x=0, y=0)

        # create a Label
        self.labelInput6 = Label(self.Window,
                                 text="Game Title: ",
                                 font="Helvetica 12").grid(row=5, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText6 = Entry(self.Window,
                                font="Helvetica 14",
                                )
        self.InputText6.insert(0, record[1])

        self.InputText6.grid(row=5, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput7 = Label(self.Window,
                                 text="Playtime: ",
                                 font="Helvetica 12").grid(row=5, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText7 = Entry(self.Window,
                                font="Helvetica 14")
        self.InputText7.insert(0, record[2])
        
        self.InputText7.grid(row=5, column=3, padx=2, pady=2)

        # create a Label
        self.labelInput8 = Label(self.Window,
                                 text="ESRB Rating: ",
                                 font="Helvetica 12").grid(row=6, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText8 = Entry(self.Window,
                                font="Helvetica 14")

        self.InputText8.insert(0, record[4])
        self.InputText8.grid(row=6, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput9 = Label(self.Window,
                                 text="Metacritic Rating: ",
                                 font="Helvetica 12").grid(row=7, column=0, padx=2, pady=2)

        self.MetaRate = Entry(self.Window,
                                font="Helvetica 14")
        self.MetaRate.insert(0, record[5])
        self.MetaRate.grid(row=7, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput10 = Label(self.Window,
                                  text="User Rating: ",
                                  font="Helvetica 12").grid(row=8, column=0, padx=2, pady=2)

        self.UserRate = Entry(self.Window,
                                font="Helvetica 14")
        self.UserRate.insert(0, record[6])
        self.UserRate.grid(row=8, column=1, padx=2, pady=2)

        # create a Label
        self.labelInput11 = Label(self.Window,
                                  text="Release Date: ",
                                  font="Helvetica 12").grid(row=9, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.InputText11 = Entry(self.Window,
                                 font="Helvetica 14")
        self.InputText11.grid(row=9, column=1, padx=2, pady=2)
        self.InputText11.insert(0, record[3])
        # create a Search Button along with action
        self.go = Button(self.Window,
                         text="Update Record (Transaction)",
                         font="Helvetica 20 bold",
                         command=lambda: UpdateRecord(self,
                                                      self.InputText6.get(), self.InputText7.get(),
                                                      self.InputText8.get(),
                                                      self.MetaRate.get(), self.UserRate.get(),
                                                      self.InputText11.get(), record[0]))

        self.go.grid(row=10, column=0, padx=2, pady=2)

        # create a Search Button along with action
        self.goTrigger = Button(self.Window,
                                text="Update Record (Trigger)",
                                font="Helvetica 20 bold",
                                command=lambda: UpdateRecordTrigger(self,
                                                                    self.InputText6.get(), self.InputText7.get(),
                                                                    self.InputText8.get(),
                                                                    self.MetaRate.get(), self.UserRate.get(),
                                                                    self.InputText11.get(), record[0]))

        self.goTrigger.grid(row=11, column=0, padx=2, pady=2)

        self.Window.mainloop()


class HomePage:

    # Constructor
    def __init__(self):
        # Declare tkinter window and configure
        self.window = Tk()
        self.window.title("DB Home Page")
        self.window.minsize(1280, 720)

        # Create Links to our functionalities
        self.SearchButton = Button(self.window, text="Search", font="Helvetica 20 bold", command=SearchPage, width=80,
                                   height=7).pack()
        self.WishlistButton = Button(self.window, text="Wishlist", font="Helvetica 20 bold", command=StartWishlist,
                                     width=80, height=7).pack()
        self.UpdateButton = Button(self.window, text="Update", font="Helvetica 20 bold", command=UpdateSearchPage,
                                   width=80, height=7).pack()

        self.window.mainloop()


# Functions for buttons

def Search(self, devname, genname, stoname, platname, parentplat, gamtitl, playtime, esrbrate, metacritrate, userrate,
           reldate):
    # For now the initial statement will join all tables together and return only the useful info
    statement = """
				SELECT distinct 
				g.game_id, title, playtime, first_release_date, ESRB_rating, metacritic_rating, user_rating,
				d.name as Developer
				from game g join gamedeveloper gd on g.game_id = gd.game_id
					join developer d on d.developer_id = gd.developer_id
					join gamegenre gg on g.game_id = gg.game_id
					join genre gen on gg.genre_id = gen.genre_id
					join gameplatform gp on g.game_id = gp.game_id
					join platform p on gp.platform_id = p.platform_id
					join gameparentplatform gpp on g.game_id = gpp.game_id
					join parentplatform pp on gpp.parentplatform_id = pp.parentplatform_id
					join gamestore gs on g.game_id = gs.game_id
					join store s on gs.store_id = s.store_id
					WHERE """
    # Variable to tell if the AND needs to be added before the string
    isFirstInput = 0

    # Single valued
    if gamtitl:
        isFirstInput = 1
        statement = statement + "title like '%" + gamtitl + "%'"
    if playtime:
        if isFirstInput == 1:
            # less than playtime for now
            statement = statement + " AND playtime < " + str(playtime)
        else:
            isFirstInput = 1
            statement = statement + "playtime < " + str(playtime)
    if esrbrate:
        if isFirstInput == 1:
            statement = statement + " AND ESRB_rating like '%" + esrbrate + "%'"
        else:
            isFirstInput = 1
            statement = statement + "ESRB_rating like '%" + esrbrate + "%'"
    if metacritrate:
        if isFirstInput == 1:
            # greater than metacritic rating for now
            statement = statement + " AND metacritic_rating > " + str(metacritrate)
        else:
            isFirstInput = 1
            statement = statement + "metacritic_rating > " + str(metacritrate)
    if userrate:
        if isFirstInput == 1:
            # greater than user rating for now
            statement = statement + " AND user_rating > " + str(userrate)
        else:
            isFirstInput = 1
            statement = statement + "user_rating > " + str(userrate)
    if reldate:
        if isFirstInput == 1:
            statement = statement + " AND first_release_date like '%" + str(reldate) + "%'"
        else:
            isFirstInput = 1
            statement = statement + "first_release_date like '%" + str(reldate) + "%'"
    # Multivalued
    if devname:
        devs = devname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for dev in devs:
                statement = statement + "d.name like '%" + dev + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for dev in devs:
                statement = statement + "d.name like '%" + dev + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if genname:
        genres = genname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for gen in genres:
                statement = statement + "genre like '%" + gen + "%' OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for gen in genres:
                statement = statement + "genre like '%" + gen + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if stoname:
        stores = stoname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for store in stores:
                statement = statement + "s.name like '%" + store + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for store in stores:
                statement = statement + "s.name like '%" + store + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if platname:
        platforms = platname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for platform in platforms:
                statement = statement + "p.name like '%" + platform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for platform in platforms:
                statement = statement + "p.name like '%" + platform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if parentplat:
        parentplatforms = parentplat.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for parentplatform in parentplatforms:
                statement = statement + "pp.name like '%" + parentplatform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for parentplatform in parentplatforms:
                statement = statement + "pp.name like '%" + parentplatform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"

    cursor_object.execute(statement)
    games = cursor_object.fetchall()

    self.Window.destroy()
    g = SearchResultsPage(games)


def SearchUpdate(self, devname, genname, stoname, platname, parentplat, gamtitl, playtime, esrbrate, metacritrate,
                 userrate, reldate):
    # For now the initial statement will join all tables together and return only the useful info
    statement = """
				SELECT distinct 
				g.game_id, title, playtime, first_release_date, ESRB_rating, metacritic_rating, user_rating,
				d.name as Developer
				from game g join gamedeveloper gd on g.game_id = gd.game_id
					join developer d on d.developer_id = gd.developer_id
					join gamegenre gg on g.game_id = gg.game_id
					join genre gen on gg.genre_id = gen.genre_id
					join gameplatform gp on g.game_id = gp.game_id
					join platform p on gp.platform_id = p.platform_id
					join gameparentplatform gpp on g.game_id = gpp.game_id
					join parentplatform pp on gpp.parentplatform_id = pp.parentplatform_id
					join gamestore gs on g.game_id = gs.game_id
					join store s on gs.store_id = s.store_id
					WHERE """
    # Variable to tell if the AND needs to be added before the string
    isFirstInput = 0

    # Single valued
    if gamtitl:
        isFirstInput = 1
        statement = statement + "title like '%" + gamtitl + "%'"
    if playtime:
        if isFirstInput == 1:
            # less than playtime for now
            statement = statement + " AND playtime < " + str(playtime)
        else:
            isFirstInput = 1
            statement = statement + "playtime < " + str(playtime)
    if esrbrate:
        if isFirstInput == 1:
            statement = statement + " AND ESRB_rating like '%" + esrbrate + "%'"
        else:
            isFirstInput = 1
            statement = statement + "ESRB_rating like '%" + esrbrate + "%'"
    if metacritrate:
        if isFirstInput == 1:
            # greater than metacritic rating for now
            statement = statement + " AND metacritic_rating > " + str(metacritrate)
        else:
            isFirstInput = 1
            statement = statement + "metacritic_rating > " + str(metacritrate)
    if userrate:
        if isFirstInput == 1:
            # greater than user rating for now
            statement = statement + " AND user_rating > " + str(userrate)
        else:
            isFirstInput = 1
            statement = statement + "user_rating > " + str(userrate)
    if reldate:
        if isFirstInput == 1:
            statement = statement + " AND first_release_date like '%" + str(reldate) + "%'"
        else:
            isFirstInput = 1
            statement = statement + "first_release_date like '%" + str(reldate) + "%'"
    # Multivalued
    if devname:
        devs = devname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for dev in devs:
                statement = statement + "d.name like '%" + dev + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for dev in devs:
                statement = statement + "d.name like '%" + dev + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if genname:
        genres = genname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for gen in genres:
                statement = statement + "genre like '%" + gen + "%' OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for gen in genres:
                statement = statement + "genre like '%" + gen + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if stoname:
        stores = stoname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for store in stores:
                statement = statement + "s.name like '%" + store + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for store in stores:
                statement = statement + "s.name like '%" + store + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if platname:
        platforms = platname.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for platform in platforms:
                statement = statement + "p.name like '%" + platform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for platform in platforms:
                statement = statement + "p.name like '%" + platform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
    if parentplat:
        parentplatforms = parentplat.split(",")
        if isFirstInput == 1:
            statement = statement + " AND ("
            for parentplatform in parentplatforms:
                statement = statement + "pp.name like '%" + parentplatform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"
        else:
            isFirstInput = 1
            statement = statement + "("
            for parentplatform in parentplatforms:
                statement = statement + "pp.name like '%" + parentplatform + "%' OR "
            # Splicing to get rid of the extra " OR "
            statement = statement[:-4]
            statement = statement + ")"

    cursor_object.execute(statement)
    games = cursor_object.fetchall()
    self.Window.destroy()
    g = SearchResultsUpdatePage(games)


def AddToWishlist(self, records):
    # Open wishlist JSON if exists otherwise start fresh and dump to directory
    try:
        with open('wishlist.json', 'r') as file:
            writeDict = json.load(file)
    except:
        writeDict = {'stored': []}

    for record in records:
        writeDict['stored'].append(self.ResultsBox.get(record)[0])

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

    if len(listpassthrough) != 0:
        statement = """
					SELECT distinct 
					g.game_id, title, playtime, first_release_date, ESRB_rating, metacritic_rating, user_rating,
					d.name as Developer
					from game g join gamedeveloper gd on g.game_id = gd.game_id
						join developer d on d.developer_id = gd.developer_id
						join gamegenre gg on g.game_id = gg.game_id
						join genre gen on gg.genre_id = gen.genre_id
						join gameplatform gp on g.game_id = gp.game_id
						join platform p on gp.platform_id = p.platform_id
						join gameparentplatform gpp on g.game_id = gpp.game_id
						join parentplatform pp on gpp.parentplatform_id = pp.parentplatform_id
						join gamestore gs on g.game_id = gs.game_id
						join store s on gs.store_id = s.store_id
					WHERE """

        for id in listpassthrough:
            statement += "g.game_id = '" + str(id) + "' OR "

        statement = statement[:-4]

        cursor_object.execute(statement)
        games = cursor_object.fetchall()

    else:
        games = []

    g = WishlistPage(games)


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


def GrabUpdateRecord(self, record):
    recordToUpdate = self.ResultsBox.get(record)
    self.window.destroy()
    g = UpdatePage(recordToUpdate)


def UpdateRecord(self, gamtitl, playtime, esrbrate, metacritrate,
                 userrate, reldate, gameid):
  
    updateStatement =    "UPDATE game g" \
                        " SET title = '" + gamtitl + "'," \
                        " playtime = '" + playtime + "'," \
                        " ESRB_rating = '" + esrbrate + "'," \
                        " metacritic_rating = '" + metacritrate + "',"\
                        " user_rating = '" + userrate + "'," \
                        " first_release_date = '"  + reldate + "'" \
                        " WHERE game_id = " + gameid                   
    
    # TO DO: Check integrity of transaction
    cursor_object.execute(updateStatement)
    data_base.commit()
    tkinter.messagebox.showinfo('Update Status', "Update Successful, nice!")
    self.Window.destroy()

def createTrigger():
    # Creates the trigger in the user's database
    try:
        """
        CREATE TRIGGER
        """    
    # Trigger already exists in user's database so do nothing
    except:
        donothing = 1
    return
    
def UpdateRecordTrigger(self, gamtitl, playtime, esrbrate,
                        metacritrate, userrate, reldate, gameid):
    """
    Does update and calls trigger
    """
    print("Working on it")
    tkinter.messagebox.showinfo('Update Status', "As if I know")
    self.Window.destroy()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Setting up Database Connection
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

with open("connectorConfig.json", "r") as f:
    config = json.load(f)
connection_config = config["mysql"]
data_base = mysql.connector.connect(**connection_config)

# Preparing a cursor object to use throughout app
cursor_object = data_base.cursor()

# Creating the update trigger
createTrigger()

# create a GUI class object
g = HomePage()