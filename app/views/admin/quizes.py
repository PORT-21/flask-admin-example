from sqladmin import ModelView

from app.tables import Quiz


class QuizAdmin(ModelView, model=Quiz):
    column_list = [Quiz.id]
