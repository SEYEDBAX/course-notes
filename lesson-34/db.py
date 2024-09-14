from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from models import *

from urllib.parse import quote

username = "example"
password = "example"
host = "localhost"
db = "example"

url_postgresql = f"postgresql+psycopg2://{username}:{quote(password)}@{host}/{db}"
url_mongodb = f"mongodb://{username}:{quote(password)}@{host}/{db}"

engine = create_engine('postgresql+psycopg2://example:example@localhost/example')
Base = declarative_base()