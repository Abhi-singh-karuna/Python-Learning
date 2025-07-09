# app/db.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import logging

DATABASE_URL = "mysql+pymysql://root:123456789@localhost/testpython"

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    metadata = MetaData()
    logger.info("Database connection successful.")
except Exception as e:
    logger.error("Database connection failed!", exc_info=True)
    raise e
# test comments