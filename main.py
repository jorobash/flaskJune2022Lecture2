from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api
from decouple import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@127.0.0.1:{config("DB_PORT")}/{config("DB_NAME")}'
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app,db)

class BookModel(db.Model):
    __tablename__ = 'books'

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255),nullable=False)
    reader_pk = db.Column(db.Integer,db.ForeignKey('readers.pk'),nullable=False)
    reader = db.relationship('ReaderModel')


    def __repr__(self):
        return f"<{self.pk}> {self.title} {self.author}"

    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}    


class ReaderModel(db.Model):
    __tablename__ = 'readers'
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String,nullable=False)
    last_name = db.Column(db.String,nullable=False)        
    books = db.relationship("BookModel", backref="books", lazy='dynamic')

class Books(Resource):
    def get(self):
        booksData = BookModel.query.all()
        books = [b.as_dict() for b in booksData]
        return {"books": books}
        return "ok"

    def post(self):
        data = request.get_json()    
        book = BookModel(title=data.get('title'),author=data.get('author'),reader_pk=data.get('reader_pk'))
        db.session.add(book)
        db.session.commit()
        return book.as_dict()


api.add_resource(Books,'/books/')


if __name__ == '__main__':
    app.run(debug=True)