from flask import Flask
from flask import redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy 

from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager

from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView 
from flask_admin import AdminIndexView

from flask_security import SQLAlchemyUserDatastore, Security
from flask_security import current_user

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
from models import *
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login',next=request.url))


class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        if is_created:
            model.generate_slug()
        return super().on_model_change(form, model, is_created)

class PostAdminView(AdminMixin, BaseModelView):
    form_columns = ['title',
                'subtitle_full',
                'subtitle_short',
                'thumnail',
                'rating_tag',
                'rating_img',
                'rating_text',
                'author',
                'date',
                'true_info',
                'false_info',
                'ctx_info',
                'origin']

admin = Admin(app,'FlaskApp',url='/', index_view=HomeAdminView(name='Home'))


admin.add_view(PostAdminView(Post, db.session))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

