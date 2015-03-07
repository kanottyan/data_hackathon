#coding:utf-8
from app import db
from datetime import datetime
from sqlalchemy.orm import synonym
from werkzeug import check_password_hash, generate_password_hash


class Entry(db.Model):
    __tablename__ = 'entries'
    #__table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
                    id=self.id, title=self.title)


class User(db.Model):
    __tablename__ = 'users'
    #__table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default='', nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    _password = db.Column('password', db.String(100), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        if password:
            #strip()は空白削除
            password = password.strip()
        self._password = generate_password_hash(password)
    #自分で定義したオブジェクトに、独自のアクセサを持った属性を追加できる機能
    password_descriptor = property(_get_password, _set_password)
    password = synonym('_password', descriptor = password_descriptor)

    def check_password(self, password):
        password = password.strip()
        if not password:
            return False
        return check_password_hash(self.password, password)

    @classmethod
    def authenticate(cls, query, email, password):
        user = query(cls).filter(cls.email==email).first()
        if user is None:
            return None, False
        return user, user.check_password(password)

    def __repr__(self):
        return u'<User id={self.id} email={self.email!r}>'.format(self=self)


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, default="", nullable = False)
    title = db.Column(db.String(200), default="", nullable = False)
    category = db.Column(db.String(100), default="", nullable = False)
    publish_date = db.Column(db.DateTime)
    is_cook = db.Column(db.Integer, default="", nullable = False)
    is_nikkei = db.Column(db.Integer, default="", nullable = False)

    def __repr__(self):
        return 'article: %r, id: %r' % (self.name, self.id)