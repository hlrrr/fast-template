# Import the SQLAlchemy parts
from sqlalchemy     import create_engine
from sqlalchemy.ext.declarative     import declarative_base
from sqlalchemy.ext.asyncio     import create_async_engine, AsyncSession
from sqlalchemy.orm     import sessionmaker

from .configs   import settings 

'''
for sycnronous databse session
'''
# engine = create_engine(settings.DATABASE_URL)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# SessionLocal = sessionmaker(autocommit=False,
#                             autoflush=False,
#                             bind=engine)


'''
for asyncronous database session
'''
engine = create_async_engine(settings.DATABASE_URL,   # need async support driver(asyncpg)
                       future=True)     # for asyncrouse feature     

SessionLocal = sessionmaker(engine,
                                  class_ = AsyncSession,
                                  expire_on_commit=False)
 
Base = declarative_base()

async def get_db_async():
    async with SessionLocal() as db:
        yield db
        await db.commit()    