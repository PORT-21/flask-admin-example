from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship

from app.tables import Base
from app.tables.user import users_to_quizes

questions_to_answers = Table(
    "questions_to_answers",
    Base.metadata,
    Column("question_id", ForeignKey("quiz_questions.id")),
    Column("answer_id", ForeignKey("quiz_awailable_answers.id")),
)

#  опросник
class Quiz(Base):
    __tablename__ = "quizes"
    id = Column(Integer, primary_key=True)
    users = relationship("User", secondary=users_to_quizes, back_populates="quizes")
    questions = ...

    @classmethod
    def generate_quiz_from_questions(*questios) -> "Quiz":
        ...


# TODO: типы вопросов, описать
class QuizQuestion(Base):
    __tablename__ = "quiz_questions"
    id = Column(Integer, primary_key=True)


class QuizAnswer(Base):
    # TODO: авить различные типы ответов
    __tablename__ = "quiz_awailable_answers"

    id = Column(Integer, primary_key=True)
    answer = Column(Text)
    # filters = relationship(
    # "Filter", back_populates="awailable_answers", secondary=questions_to_answers
    # )


# class Filter(Base):
#     __tablename__ = "tags"

#     id = Column(Integer, primary_key=True)
#     name = Column(String(40))

# type include or exclude
# expression
# value
