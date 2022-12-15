from typing import Any, cast

from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin
from markupsafe import Markup

from app.tables import Ingridient
from app.widgets import CKTextAreaField


def ingridient_formatter(
    view: "RecipieView", context: Any, model: Ingridient, name: str
) -> Markup:
    return cast(Markup, f"{model.name} {model.quantity} {model.unit_type}")


class IngridienInline(InlineFormAdmin):
    form_columns = ["id", "name", "quantity", "unit_type"]


class RecipieView(ModelView):
    column_list = ["id", "name", "ingridients", "description"]
    # column_formatters =
    inline_models = [IngridienInline(Ingridient)]
    extra_js = ["//cdn.ckeditor.com/4.6.0/standard/ckeditor.js"]
    form_overrides = {"description": CKTextAreaField}
