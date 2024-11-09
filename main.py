from flask import Flask
from usercontroller import user

app = Flask(__name__)
app.register_blueprint(user)


@app.route('/test')
def test():
    return 'hello from test.'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
