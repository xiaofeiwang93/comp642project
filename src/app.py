from flask import Flask
from Controllers.TicketingController import MovieTicketController
from Services.CommonService import CommonService
from Services.DbService import DbService
from Services.LoginService import LoginService

def create_app(test_config = None):
    get=['GET']
    post=['POST']
    both=['GET','POST']

    app = Flask(__name__, template_folder='views')

    ticketing_controller = MovieTicketController(DbService, LoginService, CommonService)

    app.add_url_rule('/', methods=both, view_func=ticketing_controller.login)

    app.add_url_rule('/home', methods=both, view_func=ticketing_controller.home)

    app.add_url_rule('/movies', methods=both, view_func=ticketing_controller.view_movie_list)

    app.add_url_rule('/movies/1', methods=both, view_func=ticketing_controller.view_movie_detail)

    # db_initial_setup_movie()

    return app


app = create_app()