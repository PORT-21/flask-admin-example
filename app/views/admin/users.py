from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import FileUploadField

# def prefix_name(obj, file_data):
#     parts = op.splitext(file_data.filename)
#     return op.secure_filename("file-%s%s" % parts)


# class UserForm(BaseForm):
#     # TODO: сделать read_only
#     id = fields.IntegerField("id")
#     avatar_link = FileUploadField("avatar_link", namegen=prefix_name)
#     name = fields.StringField("name")
#     sex = fields.SelectField("sex")
#     # TODO: quizes
#     # "quizes",
#     phone_number = fields.StringField("phone_number")
#     birthday = fields.DateField("birthday")
#     subscription_type = QuerySelectField(
#         query_factory=lambda: session.query(Subscribtion).all(), widget=Select2Widget()
#     )


class UserView(ModelView):
    can_edit = True
    can_delete = False
    can_create = True
    can_view_details = True
    # form = UserForm
    form_overrides = dict(avatar_link=FileUploadField)

    column_sortable_list = ["id"]
    form_columns = [
        "id",
        "avatar_link",
        "name",
        "sex",
        "phone_number",
        "birthday",
        "subscription_type",
    ]

    # form_extra_fields = {
    #     'clan': sqla.fields.QuerySelectField(
    #         label='Clan',
    #         query_factory=lambda: Clan.query.all(),
    #         widget=Select2Widget()
    #     )
