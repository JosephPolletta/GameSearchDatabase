"""

Python file to create the "games" database in MySQL that we will be using

"""

import mysql.connector
from configparser import ConfigParser
import json

with open("connectorConfig.json", "r") as f:
   config = json.load(f)


connection_config = config["mysql"]
dataBase = mysql.connector.connect(host=connection_config["host"],
                                    user=connection_config["user"],
                                 passwd=connection_config["passwd"])

# Preparing a cursor object
cursorObject = dataBase.cursor()

# Creating database
cursorObject.execute("CREATE DATABASE GAMES")