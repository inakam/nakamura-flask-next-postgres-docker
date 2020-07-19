import sys

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{user}:{password}@{host}/{db_name}".format(**{
    'user': 'postgres',
    'password': 'postgres',
    'host': 'postgres-db',
    'db_name': 'POSTGRESDB'
})
app.config['JSON_AS_ASCII'] = False  # JSONの文字化け対策

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    affiliate_code = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.user_id


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('user_id', 'affiliate_code', 'created')


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Hello World from Flask in a uWSGI Nginx Docker container with Python {} (default)".format(
        version
    )
    return message


@app.route("/db")
def db_handler():
    db_user_data = User.query.all()
    user_schema = UserSchema(many=True)
    return make_response(jsonify({
        'code': 200,
        'users': user_schema.dump(db_user_data)
    }))


tasks = [
    {
        'id': 1,
        'title': '日用品を買ってくる',
        'description': 'ミルク、チーズ、ピザ、フルーツ',
        'done': False
    },
    {
        'id': 2,
        'title': 'Python の勉強',
        'description': 'Python で Restful API を作る',
        'done': False
    }
]
@app.route("/tasks")
def tasks_handler():
    return jsonify(tasks=tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
