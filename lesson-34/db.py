from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from models import *

engine = create_engine('postgresql+psycopg2://example:example@localhost/example')
Base = declarative_base()