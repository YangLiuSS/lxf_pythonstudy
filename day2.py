# coding=UTF-8
# liuyang

from  flask import Flask

app =  Flask(__name__)


@app.route('/profile/<uid>/')
def index(uid):
    return 'profile' + uid




if __name__ == '__main__':
    app.run(debug=True)