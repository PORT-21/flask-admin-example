from flask_admin.contrib.sqla import ModelView

from app.widgets import CKTextAreaField


class ArticleView(ModelView):
    column_list = ["id", "name", "content", "creation_date"]

    extra_js = ["//cdn.ckeditor.com/4.6.0/standard/ckeditor.js"]
    form_overrides = {"content": CKTextAreaField}
