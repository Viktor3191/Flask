from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

appMine = Flask(__name__)
appMine.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogMine.db'
db = SQLAlchemy(appMine)
appMine.app_context().push()


class ArticleMine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<ArticleMine %r>' % self.id


@appMine.route('/')
def mine():
    return render_template('mine.html')


@appMine.route('/create-mine', methods=['POST', 'GET'])
def create_mine():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        comment = request.form['comment']
        articleMine = ArticleMine(title=title, intro=intro, text=text, comment=comment)
        try:
            db.session.add(articleMine)
            db.session.commit()
            return redirect('/posts-mine')
        except:
            return 'При добавлении статью произошла ошибка'
    else:
        return render_template('create-mine.html')


@appMine.route('/posts-mine')
def posts_mine():
    articlesMine = ArticleMine.query.order_by(ArticleMine.date).all()
    return render_template('posts-mine.html', articlesMine=articlesMine)


if __name__ == '__main__':
    appMine.run(debug=True)
