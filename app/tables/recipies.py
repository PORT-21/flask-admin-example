from enum import Enum

from sqlalchemy import Column
from sqlalchemy import Enum as EnumT
from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.tables import Base


class UnitType(Enum):
    sht = "шт."
    gm = "грамм"


class Ingridient(Base):
    # ингридиенты для рецептов
    __tablename__ = "ingridients"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    # Column(Integer, ForeignKey("Recipie.id"))
    recipie_id = Column(Integer, ForeignKey("recipies.id"))
    recipie = relationship("Recipie", back_populates="ingridients")
    # хардкод
    quantity = Column(Float)
    # единица измерения
    unit_type = Column(EnumT(UnitType), default=UnitType.sht)


class Recipie(Base):
    __tablename__ = "recipies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ingridients = relationship("Ingridient")
    description = Column(Text)
