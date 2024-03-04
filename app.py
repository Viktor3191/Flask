from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'about us'


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'hello' + name + '-' + id


@app.route('/mine/<name>')
def mine(name):
    return 'hello %s' % name


if __name__ == '__main__':
    app.run(debug=True)
