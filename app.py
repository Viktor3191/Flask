from flask import Flask, render_template
from sqlalchemy import SQLalchemy
import datetime

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLalchemy(app)


class Article(db.Model):
    id = db.Column(db.Intejer, primari_key=True)
    title = db.Column(db.String(100), nullabl=False)
    intro = db.Column(db.String(300), nullabl=False)
    text = db.Column(db.Text, nullabl=False)
    date = db.Column(db.DataTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


class ArticleMine(db.Model):
    id = db.Column(db.Intejer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DataTime, default=datetime.datetime)
    image = db.Column(db.LargeBinary(length=500), nullable=False)
    grade = db.Column(db.Intejer, nullable=False)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'hello' + name + '-' + str(id)


@app.route('/mine')
def mine():
    return render_template('mine.html')


if __name__ == '__main__':
    app.run(debug=True)
