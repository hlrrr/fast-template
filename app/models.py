from sqlalchemy     import Boolean, Column, ForeignKey, Integer, String, Enum, TEXT, DateTime
from sqlalchemy.sql.sqltypes        import TIMESTAMP
from sqlalchemy.sql.expression      import null
from sqlalchemy.orm     import relationship, declarative_mixin

from sqlalchemy_utils   import URLType

from enum   import StrEnum, auto
from datetime   import datetime

from .utils     import Base


class Common(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class SomeTable(Common, Base):
    __talblename__ = 'some table name'
    pass