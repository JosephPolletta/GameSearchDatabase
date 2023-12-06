"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GUI to Search Your Videogame Database:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# Import all the required modules
import tkinter.messagebox
from tkinter import *
import json
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
        self.devLabel = Label(self.Window,
                                 text="Developer Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=0, padx=2, pady=2)

        # create a entry box for typing the input
        self.devInput = Entry(self.Window,
                                font="Helvetica 14")

        self.devInput.grid(row=1, column=1, padx=2, pady=2)

        # create a Label
        self.genreLabel = Label(self.Window,
                                 text="Genre Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=2, padx=2, pady=2)

        # create a entry box for typing the input
        self.genreInput = Entry(self.Window,
                                font="Helvetica 14")

        self.genreInput.grid(row=1, column=3, padx=2, pady=2)

        # create a Label
        self.storeLabel = Label(self.Window,
                                 text="Store Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=4, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.storeInput = Entry(self.Window,
                                font="Helvetica 14")

        self.storeInput.grid(row=1, column=5, padx=2, pady=2)

        # create a Label
        self.platformLabel = Label(self.Window,
                                 text="Platform Name(s): ",
                                 font="Helvetica 12").grid(row=2, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.platformInput = Entry(self.Window,
                                font="Helvetica 14")

        self.platformInput.grid(row=2, column=1, padx=2, pady=2)

        # create a Label
        self.parentplatformLabel = Label(self.Window,
                                 text="Parent Platform(s): ",
                                 font="Helvetica 12").grid(row=2, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.parentplatformInput = Entry(self.Window,
                                font="Helvetica 14")

        self.parentplatformInput.grid(row=2, column=3, padx=2, pady=2)

        # Place spacer before category label so category label covers it
        self.Spacer1 = Label(self.Window).grid(row=3, column=0, padx=2, pady=10)

        # Create category name to inform user what kind of input they should have
        self.SingleValuedLabel = Label(self.Window,
                                       text="Single Valued Parameters: Input a single value only",
                                       font="Helvetica 16").place(x=0, y=100)

        # create a Label
        self.gametitleLabel = Label(self.Window,
                                 text="Game Title: ",
                                 font="Helvetica 12").grid(row=4, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.gametitleInput = Entry(self.Window,
                                font="Helvetica 14")

        self.gametitleInput.grid(row=4, column=1, padx=2, pady=2)

        # create a Label
        self.playtimeLabel = Label(self.Window,
                                 text="Playtime: ",
                                 font="Helvetica 12").grid(row=4, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.playtimeInput = Entry(self.Window,
                                font="Helvetica 14")

        self.playtimeInput.grid(row=4, column=3, padx=2, pady=2)

        # create a Label
        self.ESRBLabel = Label(self.Window,
                                 text="ESRB Rating: ",
                                 font="Helvetica 12").grid(row=4, column=4, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.ESRBRatingInput = Entry(self.Window,
                                font="Helvetica 14")

        self.ESRBRatingInput.grid(row=4, column=5, padx=2, pady=2)

        self.ESRBRatingInput.grid(row=4, column=5, padx=2, pady=2)

        # create a Label
        self.metacriticLabel = Label(self.Window,
                                 text="Metacritic Rating: ",
                                 font="Helvetica 12").grid(row=5, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.MetaCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14",
                                      width=2)

        self.MetaCombo['values'] = ('>=',
                                    '<=')

        self.MetaCombo.current(0)
        self.MetaCombo.grid(row=5, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.metacriticInput = Entry(self.Window,
                                font="Helvetica 14")

        self.metacriticInput.grid(row=5, column=2, padx=2, pady=2)

        # create a Label
        self.userrateLabel = Label(self.Window,
                                  text="User Rating: ",
                                  font="Helvetica 12").grid(row=6, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.UserCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14",
                                      width=2)

        self.UserCombo['values'] = ('>=',
                                    '<=')

        self.UserCombo.current(0)
        self.UserCombo.grid(row=6, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.userrateInput = Entry(self.Window,
                                 font="Helvetica 14")

        self.userrateInput.grid(row=6, column=2, padx=2, pady=2)

        # create a Label
        self.releasedateLabel = Label(self.Window,
                                  text="Release Date: ",
                                  font="Helvetica 12").grid(row=7, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.releasedateInput = Entry(self.Window,
                                 font="Helvetica 14")

        self.releasedateInput.grid(row=7, column=1, padx=2, pady=2)

        # create a Search Button along with action
        self.go = Button(self.Window,
                         text="Search",
                         font="Helvetica 20 bold",
                         command=lambda: Search(self, self.devInput.get(), self.genreInput.get(),
                                                self.storeInput.get(), self.platformInput.get(), self.parentplatformInput.get(),
                                                self.gametitleInput.get(), self.playtimeInput.get(), self.ESRBRatingInput.get(),
                                                self.metacriticInput.get(), self.userrateInput.get(), self.releasedateInput.get(),
                                                self.MetaCombo.get(), self.UserCombo.get(), 0))

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

        self.ResultsBox = ttk.Treeview(self.window,
                                       show='headings',
                                       xscrollcommand=self.HorizontalScroll.set,
                                       yscrollcommand=self.VerticalScroll.set)

        self.HorizontalScroll.config(command=self.ResultsBox.xview())
        self.VerticalScroll.config(command=self.ResultsBox.yview())

        self.ResultsBox['columns'] = ('Game ID', 'Title', 'Playtime', 'Release Date', 'ESRB Rating', 'Metacritic Rating',
                                      'User Rating', 'Developer')

        for col in self.ResultsBox['columns']:
            self.ResultsBox.heading(col, text=col)
            self.ResultsBox.column(col, width=120, minwidth=120, anchor="w")

        for item in results:
            self.ResultsBox.insert('', 'end', values=item)

        self.HorizontalScroll.pack(side=BOTTOM, fill=X)
        self.VerticalScroll.pack(side=RIGHT, fill=Y)
        self.ResultsBox.pack()

        self.Instructions = Label(self.window,
                                  text="Select all records you want to store in your wishlist. (Control+Click for "
                                       "multiple selections)",
                                  font="Helvetica 16").pack()

        self.WishlistButton = Button(self.window,
                                     text="Add to wishlist",
                                     font="Helvetica 10 bold",
                                     command=lambda: AddToWishlist(self, self.ResultsBox.selection()),
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

        self.WishlistBox = ttk.Treeview(self.window,
                                        show='headings',
                                        xscrollcommand=self.HorizontalScroll.set,
                                        yscrollcommand=self.VerticalScroll.set)

        self.HorizontalScroll.config(command=self.WishlistBox.xview())
        self.VerticalScroll.config(command=self.WishlistBox.yview())

        self.WishlistBox['columns'] = (
                                      'Game ID', 'Title', 'Playtime', 'Release Date', 'ESRB Rating', 'Metacritic Rating',
                                      'User Rating', 'Developer')

        for col in self.WishlistBox['columns']:
            self.WishlistBox.heading(col, text=col)
            self.WishlistBox.column(col, width=120, minwidth=120, anchor="w")

        for item in results:
            self.WishlistBox.insert('', 'end', values=item)

        self.HorizontalScroll.pack(side=BOTTOM, fill=X)
        self.VerticalScroll.pack(side=RIGHT, fill=Y)
        self.WishlistBox.pack()

        self.Instructions = Label(self.window,
                                  text="Select all records you want remove from your wishlist. (Control+Click for "
                                       "multiple selections)",
                                  font="Helvetica 16").pack()

        self.WishlistButton = Button(self.window,
                                     text="Remove from wishlist",
                                     font="Helvetica 10 bold",
                                     command=lambda: RemoveFromWishlist(self, results, self.WishlistBox.selection()),
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
        self.devLabel = Label(self.Window,
                                 text="Developer Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=0, padx=2, pady=2)

        # create a entry box for typing the input
        self.devInput = Entry(self.Window,
                                font="Helvetica 14")

        self.devInput.grid(row=1, column=1, padx=2, pady=2)

        # create a Label
        self.genreLabel = Label(self.Window,
                                 text="Genre Name(s): ",
                                 font="Helvetica 12").grid(row=1, column=2, padx=2, pady=2)

        # create a entry box for typing the input
        self.genreInput = Entry(self.Window,
                                font="Helvetica 14")

        self.genreInput.grid(row=1, column=3, padx=2, pady=2)

        # create a Label
        self.storeLabel = Label(self.Window,
                                 text="Store Name(s): ",
                                 font="Helvetica 12").grid(row=2, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.storeInput = Entry(self.Window,
                                font="Helvetica 14")

        self.storeInput.grid(row=2, column=1, padx=2, pady=2)

        # create a Label
        self.platformLabel = Label(self.Window,
                                 text="Platform Name(s): ",
                                 font="Helvetica 12").grid(row=2, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.platformInput = Entry(self.Window,
                                font="Helvetica 14")

        self.platformInput.grid(row=2, column=3, padx=2, pady=2)

        # create a Label
        self.parentplatformLabel = Label(self.Window,
                                 text="Parent Platform(s): ",
                                 font="Helvetica 12").grid(row=3, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.parentplatformInput = Entry(self.Window,
                                font="Helvetica 14")

        self.parentplatformInput.grid(row=3, column=1, padx=2, pady=2)

        # Place spacer before category label so category label covers it
        self.Spacer1 = Label(self.Window).grid(row=4, column=0, padx=2, pady=10)

        # Create category name to inform user what kind of input they should have
        self.SingleValuedLabel = Label(self.Window,
                                       text="Single Valued Parameters: Input a single value only",
                                       font="Helvetica 16").place(x=0, y=135)

        # create a Label
        self.gametitleLabel = Label(self.Window,
                                 text="Game Title: ",
                                 font="Helvetica 12").grid(row=5, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.gametitleInput = Entry(self.Window,
                                font="Helvetica 14")

        self.gametitleInput.grid(row=5, column=1, padx=2, pady=2)

        # create a Label
        self.playtimeLabel = Label(self.Window,
                                 text="Playtime: ",
                                 font="Helvetica 12").grid(row=5, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.playtimeInput = Entry(self.Window,
                                font="Helvetica 14")

        self.playtimeInput.grid(row=5, column=3, padx=2, pady=2)

        # create a Label
        self.ESRBLabel = Label(self.Window,
                                 text="ESRB Rating: ",
                                 font="Helvetica 12").grid(row=6, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.ESRBRatingInput = Entry(self.Window,
                                font="Helvetica 14")

        self.ESRBRatingInput.grid(row=6, column=1, padx=2, pady=2)

        # create a Label
        self.metacriticLabel = Label(self.Window,
                                 text="Metacritic Rating: ",
                                 font="Helvetica 12").grid(row=7, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.MetaCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14",
                                      width=2)

        self.MetaCombo['values'] = ('>=',
                                    '<=')

        self.MetaCombo.current(0)
        self.MetaCombo.grid(row=7, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.metacriticInput = Entry(self.Window,
                                font="Helvetica 14")

        self.metacriticInput.grid(row=7, column=2, padx=2, pady=2)

        # create a Label
        self.userrateLabel = Label(self.Window,
                                  text="User Rating: ",
                                  font="Helvetica 12").grid(row=8, column=0, padx=2, pady=2)

        # create a combobox for selecting <= or >=
        n = tkinter.StringVar()
        self.UserCombo = ttk.Combobox(self.Window,
                                      textvariable=n,
                                      font="Helvetica 14",
                                      width=2)

        self.UserCombo['values'] = ('>=',
                                    '<=')

        self.UserCombo.current(0)
        self.UserCombo.grid(row=8, column=1, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.userrateInput = Entry(self.Window,
                                 font="Helvetica 14")

        self.userrateInput.grid(row=8, column=2, padx=2, pady=2)

        # create a Label
        self.releasedateLabel = Label(self.Window,
                                  text="Release Date: ",
                                  font="Helvetica 12").grid(row=9, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.releasedateInput = Entry(self.Window,
                                 font="Helvetica 14")
        self.releasedateInput.grid(row=9, column=1, padx=2, pady=2)

        # create a Search Button along with action
        self.go = Button(self.Window,
                         text="Search for game to update",
                         font="Helvetica 20 bold",
                         command=lambda: Search(self, self.devInput.get(), self.genreInput.get(),
                                                self.storeInput.get(), self.platformInput.get(),
                                                self.parentplatformInput.get(),
                                                self.gametitleInput.get(), self.playtimeInput.get(),
                                                self.ESRBRatingInput.get(),
                                                self.metacriticInput.get(), self.userrateInput.get(),
                                                self.releasedateInput.get(), self.MetaCombo.get(), self.UserCombo.get(), 1))

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

        self.ResultsBox = ttk.Treeview(self.window,
                                       show='headings',
                                       selectmode='browse',
                                       xscrollcommand=self.HorizontalScroll.set,
                                       yscrollcommand=self.VerticalScroll.set)

        self.HorizontalScroll.config(command=self.ResultsBox.xview())
        self.VerticalScroll.config(command=self.ResultsBox.yview())

        self.ResultsBox['columns'] = (
                                      'Game ID', 'Title', 'Playtime', 'Release Date', 'ESRB Rating', 'Metacritic Rating',
                                      'User Rating', 'Developer')

        for col in self.ResultsBox['columns']:
            self.ResultsBox.heading(col, text=col)
            self.ResultsBox.column(col, width=120, minwidth=120, anchor="w")

        for item in results:
            self.ResultsBox.insert('', 'end', values=item)

        self.HorizontalScroll.pack(side=BOTTOM, fill=X)
        self.VerticalScroll.pack(side=RIGHT, fill=Y)
        self.ResultsBox.pack()

        self.Instructions = Label(self.window,
                                  text="Select the record you want to update.",
                                  font="Helvetica 16").pack()

        self.SelectButton = Button(self.window,
                                   text="Select record",
                                   font="Helvetica 10 bold",
                                   command=lambda: GrabUpdateRecord(self, self.ResultsBox.selection()),
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
        self.gametitleLabel = Label(self.Window,
                                 text="Game Title: ",
                                 font="Helvetica 12").grid(row=5, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.gametitleInput = Entry(self.Window,
                                font="Helvetica 14",
                                )
        self.gametitleInput.insert(0, record['values'][1])

        self.gametitleInput.grid(row=5, column=1, padx=2, pady=2)

        # create a Label
        self.playtimeLabel = Label(self.Window,
                                 text="Playtime: ",
                                 font="Helvetica 12").grid(row=5, column=2, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.playtimeInput = Entry(self.Window,
                                font="Helvetica 14")
        self.playtimeInput.insert(0, record['values'][2])

        self.playtimeInput.grid(row=5, column=3, padx=2, pady=2)

        # create a Label
        self.ESRBLabel = Label(self.Window,
                                 text="ESRB Rating: ",
                                 font="Helvetica 12").grid(row=6, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.ESRBRatingInput = Entry(self.Window,
                                font="Helvetica 14")

        self.ESRBRatingInput.insert(0, record['values'][4])
        self.ESRBRatingInput.grid(row=6, column=1, padx=2, pady=2)

        # create a Label
        self.metacriticLabel = Label(self.Window,
                                 text="Metacritic Rating: ",
                                 font="Helvetica 12").grid(row=7, column=0, padx=2, pady=2)

        self.MetaRate = Entry(self.Window,
                              font="Helvetica 14")

        self.MetaRate.insert(0, record['values'][5])
        self.MetaRate.grid(row=7, column=1, padx=2, pady=2)

        # create a Label
        self.userrateLabel = Label(self.Window,
                                  text="User Rating (input as '#.#'):",
                                  font="Helvetica 12").grid(row=8, column=0, padx=2, pady=2)

        self.UserRate = Entry(self.Window,
                              font="Helvetica 14")

        self.UserRate.insert(0, record['values'][6])
        self.UserRate.grid(row=8, column=1, padx=2, pady=2)

        # create a Label
        self.releasedateLabel = Label(self.Window,
                                  text="Release Date: ",
                                  font="Helvetica 12").grid(row=9, column=0, padx=2, pady=2)

        # create a entry box for
        # typing the input
        self.releasedateInput = Entry(self.Window,
                                 font="Helvetica 14")
        self.releasedateInput.grid(row=9, column=1, padx=2, pady=2)
        self.releasedateInput.insert(0, record['values'][3])

        # create a Search Button along with action
        self.go = Button(self.Window,
                         text="Update Record (Transaction)",
                         font="Helvetica 20 bold",
                         command=lambda: UpdateRecord(self,
                                                      self.gametitleInput.get(), self.playtimeInput.get(),
                                                      self.ESRBRatingInput.get(),
                                                      self.MetaRate.get(), self.UserRate.get(),
                                                      self.releasedateInput.get(), record['values'][0]))

        self.go.grid(row=10, column=0, padx=2, pady=2)

        # create a Search Button along with action
        self.goTrigger = Button(self.Window,
                                text="Update Record (Trigger)",
                                font="Helvetica 20 bold",
                                command=lambda: UpdateRecordTrigger(self,
                                                                    self.gametitleInput.get(), self.playtimeInput.get(),
                                                                    self.ESRBRatingInput.get(),
                                                                    self.MetaRate.get(), self.UserRate.get(),
                                                                    self.releasedateInput.get(), record['values'][0]))

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
           reldate, metacompare, usercompare, page):
    # Initial statement will join all tables together and return only the useful info
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
    # Variable to tell if there has been any input
    isFirstInput = 0

    # Single valued
    if gamtitl:
        isFirstInput = 1
        statement = statement + "title like '%" + gamtitl + "%'"
    if playtime:
        if isFirstInput == 1:
            statement = statement + " AND playtime = " + str(playtime)
        else:
            isFirstInput = 1
            statement = statement + "playtime = " + str(playtime)
    if esrbrate:
        if isFirstInput == 1:
            statement = statement + " AND ESRB_rating like '%" + esrbrate + "%'"
        else:
            isFirstInput = 1
            statement = statement + "ESRB_rating like '%" + esrbrate + "%'"
    if metacritrate:
        if isFirstInput == 1:
            statement = statement + " AND metacritic_rating " + metacompare + " " + str(metacritrate)
        else:
            isFirstInput = 1
            statement = statement + "metacritic_rating " + metacompare + " " + str(metacritrate)
    if userrate:
        if isFirstInput == 1:
            statement = statement + " AND user_rating " + usercompare + " " + str(userrate)
        else:
            isFirstInput = 1
            statement = statement + "user_rating " + usercompare + " " + str(userrate)
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
            # Splicing to get rid of the extra " OR "
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

    # If there was no input from the user before hitting the search button, it will do a default search for the first 100 records
    if isFirstInput == 0:
        statement = statement[:-6]
        statement += "LIMIT 100"

    cursor_object.execute(statement)
    games = cursor_object.fetchall()

    self.Window.destroy()
    if page == 0:
        SearchResultsPage(games)
    else:
        SearchResultsUpdatePage(games)


def AddToWishlist(self, records):

    print(self.ResultsBox.item(records[0]))

    # Open wishlist JSON if exists otherwise start fresh and dump to directory
    try:
        with open('wishlist.json', 'r') as file:
            writeDict = json.load(file)
    except Exception:
        writeDict = {'stored': []}

    for record in records:
        writeDict['stored'].append(self.ResultsBox.item(record)['values'][0])

    json.dump(writeDict, open("wishlist.json", "w"))

    self.window.destroy()


def StartWishlist():
    # We load the JSON here and then grab all keys (game_ids) and then search them in database and output to form for listbox
    try:
        with open('wishlist.json', 'r') as file:
            wishlist = json.load(file)
            listpassthrough = wishlist['stored']
    except Exception:
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

    WishlistPage(games)


def RemoveFromWishlist(self, totalrecords, removalrecords):

    recordsToBeRemoved = []
    recordsToBeKept = []
    writeDict = {}

    for record in removalrecords:
        recordsToBeRemoved.append(str(self.WishlistBox.item(record)['values'][0]))
    for record in totalrecords:
        if record[0] not in recordsToBeRemoved:
            recordsToBeKept.append(record[0])

    writeDict['stored'] = recordsToBeKept
    json.dump(writeDict, open("wishlist.json", "w"))

    self.window.destroy()


def GrabUpdateRecord(self, record):

    recordToUpdate = self.ResultsBox.item(record)
    self.window.destroy()
    UpdatePage(recordToUpdate)


def UpdateRecord(self, gamtitl, playtime, esrbrate, metacritrate,
                 userrate, reldate, gameid):

    # Calls the created transaction procedure to update with rollback check

    # Translate metacritrate 'none' value into 'null' values for statement (only statement that will be null and numeric)
    if metacritrate == 'None':
        metacritrate = 'null'

    updateStatement = "call TransactionUpdate('" + gamtitl.replace("'", "\\'") + "', " + str(playtime) + ", '" + str(esrbrate) + "', " +\
                      str(metacritrate) + ", " + str(userrate) + ", '" + str(reldate) + "', " + str(gameid) + ")"
    cursor_object.execute(updateStatement)

    # Logic in python to see if update should have passed or failed
    playtimebool = False
    metacritbool = False
    userbool = False

    if (int(playtime) >= 0):
        playtimebool = True

    if (metacritrate != 'null'):
        if (int(metacritrate) >= 0 & int(metacritrate) <= 100):
            metacritbool = True
    else:
        metacritbool = True

    if (userrate[1] == '.'):
        if int(userrate[0]) >= 0 & int(userrate[0]) <= 4 & int(userrate[2]) >= 0 & int(userrate[2]) <= 9:
            userbool = True
        elif userrate == '5.0':
            userbool = True

    if (playtimebool & metacritbool is True & userbool is True):
        tkinter.messagebox.showinfo('Update Status', "Update Successful, nice!")
    else:
        tkinter.messagebox.showinfo('Update Status', "Update Failed!")
    self.Window.destroy()


def createTransactionProcedure():

    procedure = """
    CREATE PROCEDURE TransactionUpdate(
            new_title varchar(250),
        new_playtime int,
        new_ESRB varchar(45),
        new_metascore int,
        new_userscore decimal(3,1),
        new_reldate varchar(45),
        search_gameid varchar(10)
    )
    BEGIN
        START TRANSACTION;
                UPDATE game g
        SET g.title = new_title, g.playtime = new_playtime, g.ESRB_rating = new_ESRB, g.metacritic_rating = new_metascore,
                        g.user_rating = new_userscore, g.first_release_date = new_reldate
                WHERE g.game_id = search_gameid;
                IF (new_playtime >= 0 and ((new_metascore >=0 and new_metascore <= 100) or new_metascore is null)
        and new_userscore >= 0.0 and new_userscore <= 5.0)
        THEN
                        COMMIT;
                ELSE
                        ROLLBACK;
        END IF;
    END
    """

    # If it fails then procedure already exists
    try:
        cursor_object.execute(procedure)
    except Exception as E:
        print(E)


def createTrigger():
    # Creates the trigger in the user's database
    try:
        trigger = """
        CREATE TRIGGER checkColumnIntegrity
        AFTER UPDATE ON game
        FOR EACH ROW
        BEGIN
                IF not (new.playtime >= 0 and ((new.metacritic_rating >=0 and new.metacritic_rating <= 100) or new.metacritic_rating is null)
                and new.user_rating >= 0.0 and new.user_rating <= 5.0)
                THEN
                        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Values for playtime, metacritic_rating, or user_rating
                outside accepted values!';
                END IF;
        END
        """
        cursor_object.execute(trigger)

    # Trigger already exists in user's database so do nothing
    except Exception as E:
        print(E)
    return


def UpdateRecordTrigger(self, gamtitl, playtime, esrbrate,
                        metacritrate, userrate, reldate, gameid):

    # Translate metacritrate 'none' value into 'null' values for statement (only statement that will be null and numeric)
    if metacritrate == 'None':
        metacritrate = 'null'

    try:

        updateStatement = "UPDATE game g " \
                          "SET g.title = '" + gamtitl.replace("'", "\\'") + "', g.playtime = " + str(playtime) + ", g.ESRB_rating = '" \
                          + str(esrbrate) + "', g.metacritic_rating = " + str(metacritrate) + ", g.user_rating = " + str(userrate) \
                          + ", g.first_release_date = '" + str(reldate) + \
                          "' WHERE g.game_id = '" + str(gameid) + "'"

        cursor_object.execute(updateStatement)
        tkinter.messagebox.showinfo('Update Status', "Update Successful, nice!")

    # Update failed due to trigger intercepting bad update
    except Exception as E:
        print(E)
        tkinter.messagebox.showinfo('Update Status', "Update Failed!")

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

# Creating the update transaction procedure
createTransactionProcedure()

# Creating the update trigger
createTrigger()

# create a GUI class object
g = HomePage()
