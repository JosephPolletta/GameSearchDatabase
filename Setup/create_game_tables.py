"""

Python file to create the tables of the games database

"""


import mysql.connector
import json


def create_table(config_file, lst_table_descriptions):
    """
    This method takes in the config file path and list of table descriptions and creates tables
    @param lst_table_descriptions: list of table descriptions
    @param config_file:  File Path of the configFile for the database
    """
    with open(config_file, "r") as f:
        config = json.load(f)
    connection_config = config["mysql"]
    data_base = mysql.connector.connect(**connection_config)

    # preparing a cursor object
    cursor_object = data_base.cursor()
    for table_description in lst_table_descriptions:
        cursor_object.execute(table_description)


game_table = """
CREATE TABLE `games`.`game` (
  `game_id` varchar(10) NOT null,
  `title` VARCHAR(200) NULL,
  `playtime` INT NULL,
  `first_release_date` VARCHAR(45) NULL,
  `ESRB_rating` VARCHAR(45) NULL,
  `metacritic_rating` INT NULL,
  `user_rating` DECIMAL(3,1) NULL,
  PRIMARY KEY (`game_id`));
"""

genre_table = """
CREATE TABLE genre (
    genre_id varchar(10) NOT null,
    genre nvarchar(50) NOT null,
    PRIMARY KEY (genre_id)
)
"""
# Games have genres
ghg_table = """
CREATE TABLE gameGenre (
    game_id varchar(10) NOT null,
    genre_id varchar(10) NOT null,
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
)
"""

developer_table = """
CREATE TABLE developer (
    developer_id varchar(10) NOT null,
    name nvarchar(75),
    game_count INT,
    PRIMARY KEY (developer_id)
)
"""

# Developers develop games
ddg_table = """
CREATE TABLE gameDeveloper (
    game_id varchar(10) NOT null,
    developer_id varchar(10) NOT null,
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (developer_id) REFERENCES developer(developer_id)
)
"""

store_table = """
CREATE TABLE store (
    store_id varchar(10) NOT null,
    name nvarchar(50),
    PRIMARY KEY (store_id)
)
"""

# Games are sold at stores
game_store_table = """
CREATE TABLE gameStore (
    game_id varchar(10) NOT null,
    store_id varchar(10) NOT null,
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
)
"""

platform_table = """
CREATE TABLE platform (
    platform_id varchar(10) NOT null,
    name nvarchar(50),
    PRIMARY KEY (platform_id)
)
"""

# Games exist on platforms 
game_platform_table = """
CREATE TABLE gamePlatform (
    game_id varchar(10) NOT null,
    platform_id varchar(10) NOT null,
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (platform_id) REFERENCES platform(platform_id)
)
"""

parentplatform_table = """
CREATE TABLE parentplatform (
    parentplatform_id varchar(10) NOT null,
    name nvarchar(50),
    PRIMARY KEY (parentplatform_id)
)
"""

# Platforms have parent platforms
game_parentplatform_table = """
CREATE TABLE gameParentPlatform (
    game_id varchar(10) NOT null,
    parentplatform_id varchar(10) NOT null,
    FOREIGN KEY (game_id) REFERENCES game(game_id),
    FOREIGN KEY (parentplatform_id) REFERENCES parentplatform(parentplatform_id)
)
"""

lst_table_descriptions = [game_table,genre_table,ghg_table,developer_table,ddg_table,store_table,game_store_table,platform_table,game_platform_table,parentplatform_table, game_parentplatform_table]

create_table(config_file="connectorConfig.json", lst_table_descriptions=lst_table_descriptions)

