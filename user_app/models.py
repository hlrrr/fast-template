from sqlalchemy     import Boolean, Column, ForeignKey, Integer, String, Enum, Text, DateTime
from sqlalchemy.sql.sqltypes        import TIMESTAMP
from sqlalchemy.sql.expression      import null
from sqlalchemy.orm     import relationship, declarative_mixin

from sqlalchemy_utils   import URLType

from enum   import StrEnum, auto
from datetime   import datetime

from .utils     import Base


class Status(StrEnum):
    active = auto()
    blocked = auto()    
    deleted = auto()

class SNS_type(StrEnum):
    kakao = auto()
    google = auto()
    naver = auto()


class Common(Base):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class User(Common, Base):
    __talblename__ = 'users'
    
    email = Column(__name_pos=String(length=255), unique=True, nullable=True)
    password = Column(String(length=255), nullable=False)
    sns_type =  Column(__name_pos=Enum, nullable=True)
    status = Column(Enum, default=Status.active)
    marketing_agree = Column(Boolean, nullable=True, default=True)

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Common, Base):
    __tablename__ = "profiles"

    name = Column(String(length=255), nullable=True)
    phone_number = Column(__name_pos=String(length=255), nullable=True)
    profile_img = Column(__name_pos=URLType, nullable=True)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
