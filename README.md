# Videogame Search Database App!
## Requirements
In order to ensure that you've met all requirements to begin to setup the database and app, take a look at and follow the steps in the requirements.txt file.

Additionally, you must have python-connector-sql and tkinter installed
<br/>
To install: open your command prompt and run these two pip installers
<br/>
<code>pip3 install python-connector-mysql</code>
<br/>
<code>pip3 install tk</code>

## Generating the database
To create and populate the games database you’ll need to have MySQL installed, an environment to run Python code, and the following files from this GitHub repo (located in the "Setup" folder):

* DBConnectorConfig.json
* create_games_db.py
* create_game_tables.py
* insert_into_tables.py
  
It's highly recommended that these files are all stored in a folder together to ensure there are no directory issues

Additionally, you'll need to download and extract the gamedata folder and house it in the same location as the other files. 
<br/>
The data file can be downloaded here: https://drive.google.com/file/d/1ItOqp7xj-HBor4Wtk8_qKGaCgptWfaix/view

### Creating and populating the database:
Once all of the prerequisites are met, start by **opening the DBConnectorConfig.json and editing the three values mapped to "host", "user", and "passwd"** to reflect how your MySQL server is configured (typically “host” can stay as “localhost” and "user" can stay as "root" however the password will need to be changed to how your MySQL login was configured).

Next, **run the create_games_db.py file**, which will create the empty games database.

After the database has been created, run the create_game_tables.py file, which will execute the SQL commands to create the tables for the games database.

Finally, **open the insert_into_tables.py file and alter the string “path_to_games” to the directory where all of the necessary json data files are stored on your machine**, and then run the **insert_into_tables.py** file, which will parse the json files in your directory and then execute SQL to insert the game data into the database.

## Setting up/using the app

### App Setup
To setup the app, you'll need the **gui.py file** and the **DBConnectorConfig.json**. Make sure these two files are housed in the same location. 

We recommend creating a new folder titled 'GamesDB' or something similar to house these two files as a wishlist.json file will also be getting created in this folder

### Running/Using the app
Once the app is setup you are free to **run the gui.py file**!

Using the app is relatively straightforward, you'll be greeted with three buttons: "Search", "Wishlist", and "Update". 

#### Search:
"Search" will open a new window where you can input as many or as little fields as you'd like to query by into any of the labeled textboxes. Upon clicking the search button the database will be queried
based on your input and a window displaying the results will appear. From this window, you can select as many records as you'd like from the table and then click the "Add to wishlist" button to add to record to your wishlist of games.

#### Wishlist:
"Wishlist" will show you a table of the games that are currently in your wishlist. From here, you can look at your wishlist and remove any games you no longer want in your wishlist by selecting all of the games you'd like to remove and then clicking the button "Remove from wishlist".

#### Update:
"Update" will open a new window where you can input as many or as little fields as you'd like to query by into any of the labeled textboxes. Upon clicking the "Search for game to update button the database will be queried
based on your input and a window displaying the results will appear. From this window, you can select the game that you'd like to update (Only 1) and then click the "Select record" button. This will bring up a new window that allows you to alter the game's different attributes. Once the game has been sufficiently updated, you can either click the "Update Record (Transaction)" button or the "Update Record (Trigger)" button to finish the update.
