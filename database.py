from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_url= f"mysql+pymysql://{os.getenv("dbuser")}; {os.getenv("dbhost")}; {os.getenv("dbport")}; {os.getenv("dbname")}"

engine = create_engine(db_url)

session = sessionmaker(bind=engine)

db = session()