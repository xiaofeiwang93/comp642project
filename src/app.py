from flask import Flask
from Services.loginService import login

def create_app(test_config = None):
    get=['GET']
    post=['POST']
    both=['GET','POST']

    app = Flask(__name__, template_folder='views')

    app.add_url_rule('/', methods=both, view_func=login)

    return app


app = create_app()