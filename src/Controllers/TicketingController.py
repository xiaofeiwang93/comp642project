from datetime import datetime
from typing import List

from flask import render_template
from Models.Bookings.Booking import Booking
from Models.Movies.Movie import Movie
from Models.Movies.Screening import Screening

class MovieTicketController:
    def __init__(self, db_service, login_service, common_service, movie_service) -> None:
        """!
        Constructor for the MovieTicketController class.

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
        movie_list = self.movie_service.get_all_movies()
        print(movie_list.count)
        return render_template('home.html', movie_list=movie_list)
    
    def search_movie():
        print("############  inside search movie")

    def view_movie_list(self):
        movie_list = self.movie_service.get_all_movies()
        return render_template('./Movies/movie_list.html', movie_list=movie_list)
    
    def view_movie_detail(self):
        self.common_service.movieDetail()
        return render_template('./Movies/movie_detail.html')

    def search_movies(self, title: str, language: str, genre: str, release_date: datetime) -> List[Movie]:
        """!
        Search for movies based on title, language, genre, and release date.

        :param title: The title of the movie to search for.
        :param language: The language of the movie.
        :param genre: The genre of the movie.
        :param release_date: The release date of the movie.
        :return: List of Movie objects matching the search criteria.
        """
        pass

    def view_movie_details(self, movie: Movie) -> None:
        """!
        View details of a selected movie.

        :param movie: The selected Movie object.
        """
        pass

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