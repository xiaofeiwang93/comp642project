from typing import List
from Models.Movies.Movie import Movie
from Services.DbService import DbService
from ViewModels.MovieViewModel import MovieViewModel

class MovieService:
    def get_all_movies() -> List[MovieViewModel]:
        """!
        Get a list of all movies.

        :return: List of Movie View Model.
        """
        movie_view_models = []

        movie_list = DbService.read_all_records(DbService.movieDbName)

        for movie_info in movie_list:
            movie_view_model = MovieService.map_movie_view_model(movie_info)
            MovieService.get_movie_media(movie_view_model.id, movie_view_model)
            movie_view_models.append(movie_view_model)

        return movie_view_models
    
    def get_movie_media(movie_id: int, movie_view_model: MovieViewModel) -> None:
        """!
        Add media address to MovieViewModel.

        :return: List of Movie View Model.
        """
        movie_media = DbService.search_record_by_id(movie_id, DbService.movieMediaDbName)
        MovieService.map_movie_media_view_model(movie_media, movie_view_model)
    
    def get_movie_by_id(movie_id: int) -> MovieViewModel:
        """!
        Get a movie by ID.

        :return: Movie View Model.
        """
        movie = DbService.search_record_by_id(movie_id, DbService.movieDbName)
        movie_view_model = MovieService.map_movie_view_model(movie)
        MovieService.get_movie_media(movie_id, movie_view_model)

        return movie_view_model

    def search_movies(movie_search: Movie) -> List[MovieViewModel]:
        """!
        Search for movies based on title, language, genre, and release date.

        :param movie_search: The Movie object containing the search criteria.
        :return: List of Movie View Model objects matching the search criteria.
        """
        movie_view_models = []

        print("### search_movies in Moive Service###")
        print(movie_search)

        movie_list = DbService.search_records_by_multiple_attributes(DbService.movieDbName, movie_search)

        for movie_info in movie_list:
            movie_view_model = MovieService.map_movie_view_model(movie_info)
            MovieService.get_movie_media(movie_view_model.id, movie_view_model)
            movie_view_models.append(movie_view_model)

        return movie_view_models

    def map_movie_view_model(movie_info) -> List[MovieViewModel]:
        """!
        Map the movie_list from dictionary into movie view model.

        :return: List of Movie View Model.
        """

        movie = MovieViewModel()
        movie.id = movie_info.get('id')
        movie.title = movie_info.get('title')
        movie.description = movie_info.get('description')
        movie.duration_mins = movie_info.get('duration_mins')
        movie.language = movie_info.get('language')
        movie.release_date = movie_info.get('release_date')
        movie.country = movie_info.get('country')
        movie.genre = movie_info.get('genre')

        return movie
    
    def map_movie_media_view_model(movie_media, movie_view_model) -> None:
        """!
        Map the movie_media_list from dictionary into movie view model.

        :return: None.
        """
        movie_view_model.cardsrcaddress = movie_media.get('cardsrcaddress')
        movie_view_model.detailbanneraddress = movie_media.get('detailbanneraddress')

