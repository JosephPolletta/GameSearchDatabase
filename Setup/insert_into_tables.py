"""

Python file to insert all of the data into the created tables

"""
# Any needed imports
import os
import mysql.connector
import json

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Change this to your directory
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
path_to_games = "YOURPATH"

with open("connectorConfig.json", "r") as f:
    config = json.load(f)
connection_config = config["mysql"]
data_base = mysql.connector.connect(**connection_config)

# Preparing a cursor object
cursor_object = data_base.cursor()

# Dup detector
games_list = []

# List to track genres, platforms, and stores
genre_list = []
platform_list = []
parentplatform_list = []
store_list = []
dev_list = []

# JSON file read
files = os.listdir(path_to_games)
files.sort(reverse=True)


# Method to insert null values so that foreign key errors don't occur
def nullInserts():
    cursor_object.execute("INSERT INTO games." + "platform" + " (platform_id, name)"
                                                              "values (%s, %s)", ("NULL", "No platform"))
    cursor_object.execute("INSERT INTO games." + "parentplatform" + " (parentplatform_id, name)"
                                                                    "values (%s, %s)", ("NULL", "No parent platform"))
    cursor_object.execute("INSERT INTO games." + "store" + " (store_id, name)"
                                                           "values (%s, %s)", ("NULL", "No store"))
    cursor_object.execute("INSERT INTO games." + "genre" + " (genre_id, genre)"
                                                           "values (%s, %s)", ("NULL", "No genre"))
    return


# Procedure to update developer null values
def createUpdateProcedure():
    # The MySQL code to create the procedure
    procedure = """
                CREATE PROCEDURE `updateDeveloper` (target_dev_id varchar(10), new_name varchar(75), new_game_count INT)
                BEGIN
                UPDATE games.developer
                SET name = new_name, game_count = new_game_count
                WHERE developer_id = target_dev_id;
                END
                """
    cursor_object.execute(procedure)

    return


try:
    createUpdateProcedure()
except Exception:
    dummy = 1

nullInserts()

for json_file in files:

    jf = open(path_to_games + json_file)
    data = json.load(jf)

    # For the game JSONS
    if "GameRes" in json_file:
        for game in data["results"]:
            # Insertion into game table
            game_id = game["id"]
            if game_id not in games_list:
                games_list.append(game_id)
                game_title = game["name"]
                playtime = game["playtime"]
                first_release_date = game["released"]
                if (game["esrb_rating"] is None):
                    ESRB_rating = None
                else:
                    ESRB_rating = game["esrb_rating"]["name"]
                metacritic_rating = game["metacritic"]
                user_rating = game["rating"]

                game_tuple = (game_id, game_title, playtime, first_release_date, ESRB_rating, metacritic_rating, user_rating)

                cursor_object.execute(
                    "INSERT INTO games." + "game" + " (game_id, title, playtime, first_release_date, ESRB_rating, metacritic_rating, user_rating)"
                                                    "values (%s, %s,%s, %s,%s, %s, %s)", (game_tuple))

                # Insertion into genre table and gamegenre table
                for genre in game["genres"]:
                    genre_id = genre["id"]
                    genre_name = genre["name"]
                    genre_tuple = (genre_id, genre_name)
                    gamegenre_tuple = (game_id, genre_id)

                    if genre_id not in genre_list:
                        genre_list.append(genre_id)
                        # Insertion into genre table
                        cursor_object.execute("INSERT INTO games." + "genre" + " (genre_id, genre)"
                                                                               "values (%s, %s)", (genre_tuple))

                    # Insertion into gamegenre table
                    cursor_object.execute("INSERT INTO games." + "gamegenre" + " (game_id, genre_id)"
                                                                               "values (%s, %s)", (gamegenre_tuple))

                # Insertion into platform and gameplatform table
                if game["platforms"] is None:
                    cursor_object.execute("INSERT INTO games." + "gameplatform" + " (game_id, platform_id)"
                                                                                  "values (%s, %s)", (game_id, "NULL"))
                else:
                    for platform in game["platforms"]:
                        platform_id = platform["platform"]["id"]
                        platform_name = platform["platform"]["name"]
                        platform_tuple = (platform_id, platform_name)
                        gameplatform_tuple = (game_id, platform_id)
                        if platform_name not in platform_list:
                            platform_list.append(platform_name)
                            # Insertion into platform table
                            cursor_object.execute("INSERT INTO games." + "platform" + " (platform_id, name)"
                                                                                      "values (%s, %s)",
                                                  (platform_tuple))

                        # Insertion into gameplatform table
                        cursor_object.execute("INSERT INTO games." + "gameplatform" + " (game_id, platform_id)"
                                                                                      "values (%s, %s)",
                                              (gameplatform_tuple))

                # Insertion into parentplatform and gameParentPlatform table
                if game["platforms"] is None:
                    cursor_object.execute("INSERT INTO games." + "gameparentplatform" + " (game_id, parentplatform_id)"
                                                                                        "values (%s, %s)",
                                          (game_id, "NULL"))
                else:
                    for parentplatform in game["parent_platforms"]:
                        parentplatform_id = parentplatform["platform"]["id"]
                        parentplatform_name = parentplatform["platform"]["name"]
                        parentplatform_tuple = (parentplatform_id, parentplatform_name)
                        gameparentplatform_tuple = (game_id, parentplatform_id)
                        if parentplatform_name not in parentplatform_list:
                            parentplatform_list.append(parentplatform_name)
                            # Insertion into parentplatform table
                            cursor_object.execute("INSERT INTO games." + "parentplatform" + " (parentplatform_id, name)"
                                                                                            "values (%s, %s)",
                                                  (parentplatform_tuple))

                        # Insertion into gameparentplatform table
                        cursor_object.execute(
                            "INSERT INTO games." + "gameparentplatform" + " (game_id, parentplatform_id)"
                                                                          "values (%s, %s)", (gameparentplatform_tuple))

                        # Insertion into store and gamestore table
                if game["stores"] is None:
                    cursor_object.execute("INSERT INTO games." + "gamestore" + " (game_id, store_id)"
                                                                               "values (%s, %s)", (game_id, "NULL"))
                else:
                    for store in game["stores"]:
                        store_id = store["store"]["id"]
                        store_name = store["store"]["name"]
                        store_tuple = (store_id, store_name)
                        gamestore_tuple = (game_id, store_id)
                        if store_name not in store_list:
                            store_list.append(store_name)
                            # Insertion into store table
                            cursor_object.execute("INSERT INTO games." + "store" + " (store_id, name)"
                                                                                   "values (%s, %s)", (store_tuple))

                        # Insertion into gamestore table
                        cursor_object.execute("INSERT INTO games." + "gamestore" + " (game_id, store_id)"
                                                                                   "values (%s, %s)", (gamestore_tuple))

                # Insert value into dev table
                dev_id = data["d_id"]
                if dev_id not in dev_list:
                    dev_list.append(dev_id)
                    cursor_object.execute("INSERT INTO games." + "developer" + " (developer_id, name, game_count)"
                                          "values (%s, %s, %s)", (dev_id, None, None))

                # Insertion into gamedeveloper table
                gamedev_tuple = (game_id, dev_id)
                cursor_object.execute(
                    "INSERT INTO games." + "gamedeveloper" + " (game_id, developer_id)"
                                                             "values (%s, %s)", (gamedev_tuple))

    # For the dev JSONS
    else:
        for dev in data["results"]:
            # Insertion into developer table
            dev_id = dev["id"]
            dev_name = dev["name"]
            dev_gamescount = dev["games_count"]
            dev_tuple = (dev_id, dev_name, dev_gamescount)
            if dev_id not in dev_list:
                cursor_object.execute("INSERT INTO games." + "developer" + " (developer_id, name, game_count)"
                                      "values (%s, %s, %s)", (dev_tuple))
            else:
                args = [dev_id, dev_name, dev_gamescount]
                cursor_object.callproc("updateDeveloper", args=args)

# Commit changes
data_base.commit()
cursor_object.close()

print("Populated data into games database successfully")
