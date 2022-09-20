from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# postgresql://postgres:1773237*@localhost:5432/alembic-db
database_name = "alembic-db"
SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format('postgres', '1773237*', 'localhost:5432', database_name)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1773237*@localhost:5432/alembic-db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()