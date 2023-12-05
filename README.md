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
To create and populate the games database you’ll need to have MySQL installed, an environment to run Python code, and the following files from this GitHub repo:

* connectorConfig.json
* create_games_db.py
* create_game_tables.py
* insert_into_tables.py
  
It's highly recommended that these files are all stored in a folder together to ensure there are no directory issues

Additionally, you'll need to download the gamedata folder and house it in the same location as the other files. The data file can be found here: (INSERT LINK)

### Creating and populating the database:
Once all of the prerequisites are met, start by opening the connectorConfig.json and editing the three values mapped to "host", "user", and "passwd" to reflect how your MySQL server is configured (typically “host” can stay as “localhost” and "user" can stay as "root" however the password will need to be changed to how your MySQL login was configured).

Next, run the create_games_db.py file, which will create the empty games database.

After the database has been created, run the create_game_tables.py file, which will execute the SQL commands to create the tables for the games database.

Finally, open the insert_into_tables.py file and alter the string “path_to_games” to the directory where all of the necessary json data files are stored on your machine, and then run the insert_into_tables.py files, which will parse the json files in your directory and then execute SQL to insert the game data into the database.

## Setting up the app

## Running the app
<code>python3 gui.py</code>
