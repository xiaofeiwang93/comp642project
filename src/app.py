from flask import Flask
from Services.commonService import home
from Services.loginService import login

def create_app(test_config = None):
    get=['GET']
    post=['POST']
    both=['GET','POST']

    app = Flask(__name__, template_folder='views')

    app.add_url_rule('/', methods=both, view_func=login)

    app.add_url_rule('/home', methods=both, view_func=home)

    return app


app = create_app()