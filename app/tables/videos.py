from enum import Enum

from sqlalchemy import Column, Date
from sqlalchemy import Enum as EnumT
from sqlalchemy import Float, Integer, String, Text

from app.tables import Base


class VideoTrain(Base):
    __tablename__ = "video train"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(Text)
    first_free_video = ...
    videos = #TODO: m2m to videos
    recipies = ...
    articles = ...


class Videos(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True)
    video_link = Column(String)
    # включающие теги, по которым будет идти отбор контента
    quiz_instance = ...


#TODO: что энто такое
class Webinar:
    ...
