# Хранение моделей баз данных
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func



#  макет объекта Заметки
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(2500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
            # при указании внешнего ключа, ссылка на таблицу User, в lower регистре - user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 1:М

#  макет объекта Пользователь
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # 1:М
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
            # при указании отношений, ссылка на таблицу Note, в upper регистре - Note
    notes = db.relationship('Note')