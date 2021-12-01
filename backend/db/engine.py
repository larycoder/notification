from sqlalchemy import create_engine
import json
import sys

# load config
config = {}
with open("./config.json", "r") as jsonFile:
    text = jsonFile.read()
    config = json.loads(text)

if not config:
    print("DB could not load configuration...")
    sys.exit(1)

# sqlite engine
sql_connection = config["db"]["connection"]
engine = create_engine(sql_connection, echo=True, future=True)
