from datetime import datetime
from typing import List

from flask import render_template, request
from Models.Bookings.Booking import Booking
from Models.Movies.Movie import Movie
from Models.Movies.Screening import Screening

class MovieTicketController:
    def __init__(self, db_service, login_service, common_service, movie_service) -> None:
        """!
        Constructor for the MovieTicketController class. Implement the Inversion of Control (IoC) principle here via Dependency Injection - constructor injection.

        :param ticket_system: An instance of the MovieTicketSystem.
        """
        self.db_service = db_service
        self.login_service = login_service
        self.common_service = common_service
        self.movie_service = movie_service

    def login(self):
        self.login_service.login()
        return render_template('Common/login_view.html')
    
    def home(self):
        """!
        home page

        :param ticket_system: None.
        """
        movie_list = self.movie_service.get_all_movies()
        return render_template('home.html', movie_list=movie_list)

    def view_movie_list(self):
        movie_list = self.movie_service.get_all_movies()
        return render_template('./Movies/movie_list.html', movie_list=movie_list)
    
    def view_movie_detail(self, movie_id: int):
        """!
        Search for movies based on id.

        :param id: The id of the movie.
        :return: A Movie objects matching the id.

        """
        movie = self.movie_service.get_movie_by_id(movie_id)
        return render_template('./Movies/movie_detail.html', movie=movie)

    def search_movies(self):
        """!
        Search for movies based on title, language, genre, and release date.

        :param title: The title of the movie to search for.
        :param language: The language of the movie.
        :param genre: The genre of the movie.
        :param release_date: The release date of the movie.
        :return: List of Movie objects matching the search criteria.
        """

        movie = Movie()
        movie.title = request.form.get('titleSearch')
        movie.language = request.form.get('languageSearch')
        movie.genre = request.form.get('genreSearch')
        movie.release_date = request.form.get('releasedateSearch')

        movie_list = self.movie_service.search_movies(movie)
        
        return render_template('./Movies/movie_list.html', movie_list=movie_list)
    
    def search_movies_by_title(self):
        """!
        Search for movies based on title.

        :param title: The title of the movie to search for.
        :return: List of Movie objects matching the search criteria.
        """

        title = request.form.get('search')

        movie_list = self.movie_service.search_movies_by_title(title)
        
        return render_template('./Movies/movie_list.html', movie_list=movie_list)

    def view_screenings(self, movie: Movie) -> List[Screening]:
        """!
        View available screenings for a selected movie.

        :param movie: The selected Movie object.
        :return: List of Screening objects for the movie.
        """
        pass

    def book_tickets(self, movie_title: str, customer_name: str, seats: List[int]) -> Booking:
        """!
        Book tickets for a movie on behalf of a customer.

        :param movie_title: The title of the movie to book.
        :param customer_name: The name of the customer making the booking.
        :param seats: List of seat numbers to book.
        :return: A Booking object representing the booking.
        """
        pass

    def get_available_seats(self, movie_title: str) -> List[int]:
        """!
        Get a list of available seats for a specific movie.

        :param movie_title: The title of the movie for which to retrieve available seats.
        :return: List of available seat numbers.
        """
        pass

    def get_customer_bookings(self, customer_name: str) -> List[Booking]:
        """!
        Get a list of bookings made by a specific customer.

        :param customer_name: The name of the customer for whom to retrieve bookings.
        :return: List of Booking objects made by the customer.
        """
        pass

    def cancel_booking(self, booking: Booking) -> None:
        
        """!
        Cancel a booking and provide a refund to the customer.

        :param booking: The booking to be canceled.
        """
        pass