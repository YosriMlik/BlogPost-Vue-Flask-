from os import name
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_marshmallow import Marshmallow
from sqlalchemy import desc
from flask_cors import CORS

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:''@localhost/blog-post'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ma = Marshmallow(app)
CORS(app)

class posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    date_posted = db.Column(db.Text, nullable=False)

    def __init__(self, title, content, author, date, date_posted):
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.date_posted = date_posted
        

class PostSchema(ma.Schema):
    class Meta:
        fields = ('id','title','content','author','date','date_posted')

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/', methods = ['GET'])
def home():
    all_posts = posts.query.order_by(desc(posts.date)).all()
    results = posts_schema.dump(all_posts)
    return jsonify(results)


@app.route('/add-post/', methods = ['POST'])
def addpost():
    title = request.json['title']
    content = request.json['content']
    author = request.json['author']
    # add timedelta only after hosting  + timedelta(hours=1)
    date = datetime.now()
    date_posted = date.strftime("%m/%d/%Y %H:%M:%S")
    new_post = posts(title, content, author, date, date_posted)
    db.session.add(new_post)
    db.session.commit()
    return post_schema.jsonify(new_post)

@app.route('/edit/<id>/', methods = ['POST'])
def edit(id):
    post = posts.query.get_or_404(id)
    title = request.json['title']
    content = request.json['content']
    post.title = title
    post.content = content
    db.session.commit()
    return post_schema.jsonify(post)

@app.route('/delete/<id>', methods = ['DELETE'])
def delete(id):
    post = posts.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return post_schema.jsonify(post)


if __name__ == '__main__':
    app.run(debug=True)