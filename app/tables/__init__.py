from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
engine = create_engine(
    "sqlite:///example.sqlite",
    connect_args={"check_same_thread": False},
)
session = scoped_session(sessionmaker(bind=engine))


from app.tables.articles import Article
from app.tables.quizes import Quiz, QuizAnswer, QuizQuestion
from app.tables.recipies import Ingridient, Recipie, UnitType
from app.tables.user import Subscribtion, User

Base.metadata.create_all(engine)  # Create tables
