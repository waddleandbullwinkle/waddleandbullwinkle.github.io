from flask import Flask, request, jsonify, session, g, redirect, url_for, abort, \
     render_template, flash, json
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='supersecretdevelopmentkey',
    SESSION_COOKIE_NAME = 'in_out_board',
    SQLALCHEMY_DATABASE_URI = 'pics.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = True
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

class Pictures(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    path = db.Column(db.String)

db_adapter = SQLAlchemyAdapter(db, Pictures)

def add_entries():
    entry = Pictures(path="pics/polaroidfarshot.jpg")
    db.session.add(entry)
    entry = Pictures(path="pics/waddle1.jpg")
    db.session.add(entry)
    db.commit()


@app.route('/')
def mainpage():
    add_entries()
    pics = Pictures.query.order_by(Pictures.id.desc()).all()
    return render_template("index.html", pics=pics)







if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run()
