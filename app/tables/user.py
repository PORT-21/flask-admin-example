import datetime
from enum import Enum

from sqlalchemy import Column, Date
from sqlalchemy import Enum as EnumT
from sqlalchemy import ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.tables import Base


class Subscribtion(Enum):
    FREE = datetime.timedelta(days=3)
    MONTH = datetime.timedelta(days=30)
    THREE_MONTH = datetime.timedelta(days=30 * 3)
    YEAR = datetime.timedelta(days=30 * 4 * 12)


class SexEnum(Enum):
    male = "MALE"
    female = "FEMAIL"
    helicopter = "HELICOPTER"


users_to_quizes = Table(
    "users_to_quizes",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("quiz_id", ForeignKey("quizes.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    avatar_link = Column(String(255))
    sex = Column(EnumT(SexEnum), default=SexEnum.helicopter)
    quizes = relationship("Quiz", secondary=users_to_quizes, back_populates="users")
    password = Column(String(128))
    phone_number = Column(String(12))
    birthday = Column(Date)
    name = Column(String)
    subscription_type = Column(EnumT(Subscribtion), default=Subscribtion.FREE)
