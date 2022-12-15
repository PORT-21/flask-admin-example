from sqlalchemy import Column, Date, Integer, String, Text

from app.tables import Base


class Article(Base):
    # статьи
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(Text)
    creation_date = Column(Date)

    @property
    def reading_time(self) -> int:
        # время чтения в минутах
        ...
