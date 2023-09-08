# Import the SQLAlchemy parts
from sqlalchemy     import create_engine
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy.orm     import sessionmaker

from .configs   import settings 

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()

# database session for prod
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()