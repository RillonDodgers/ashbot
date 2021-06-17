from masoniteorm.connections import ConnectionResolver

DATABASES = {
  "default": "sqlite",
  "sqlite": {
    "driver": "sqlite",
    "database": "ashbot.sqlite3",
  }
}

DB = ConnectionResolver().set_connection_details(DATABASES)
