from typing import cast

from flask import Flask
from flask_admin import Admin, AdminIndexView

from app import tables
from app.views import admin as admin_views


def create_app() -> Flask:
    app = Flask(__name__)

    # app.config["FLASK_ADMIN_SWATCH"] = "Cosmo"
    app.secret_key = "kek"

    admin = Admin(
        app,
        name="demo admin panel",
        index_view=AdminIndexView(name="📃", url="/"),
        template_mode="bootstrap4",
    )

    session = tables.session

    admin.add_view(admin_views.UserView(tables.User, session, name="пользователи"))
    admin.add_view(admin_views.RecipieView(tables.Recipie, session, name="рецепты"))
    admin.add_view(admin_views.ArticleView(tables.Article, session, name="статьи"))
    return cast(Flask, admin.app)


app = create_app()
