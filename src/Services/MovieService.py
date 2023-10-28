from typing import List
from Services.DbService import DbService
from ViewModels.MovieViewModel import MovieViewModel

class MovieService:
    def get_all_movies() -> List[MovieViewModel]:
        """!
        Get a list of all movies.

        :return: List of Movie View Model.
        """
        movie_list = DbService.read_all_records(DbService.movieDbName)
        movie_view_models = MovieService.map_movie_view_model(movie_list)

        for model in movie_view_models:
            MovieService.get_movie_media(model.id, model)

        return movie_view_models
    
    def get_movie_media(movie_id: int, movie_view_model: MovieViewModel) -> None:
        """!
        Add media address to MovieViewModel.

        :return: List of Movie View Model.
        """
        movie_media = DbService.search_record_by_id(movie_id, DbService.movieMediaDbName)
        MovieService.map_movie_media_view_model(movie_media, movie_view_model)
    
    def map_movie_view_model(movie_list) -> List[MovieViewModel]:
        """!
        Map the movie_list from dictionary into movie view model.

        :return: List of Movie View Model.
        """
        movie_view_models = []

        for movie_info in movie_list:
            movie = MovieViewModel()
            movie.id = movie_info.get('id')
            movie.title = movie_info.get('title')
            movie.description = movie_info.get('description')
            movie.duration_mins = movie_info.get('duration_mins')
            movie.language = movie_info.get('language')
            movie.release_date = movie_info.get('release_date')
            movie.country = movie_info.get('country')
            movie.genre = movie_info.get('genre')
            movie.cardsrcaddress = movie_info.get('cardsrcaddress')
            movie.detailbanneraddress = movie_info.get('detailbanneraddress')

            movie_view_models.append(movie)

        return movie_view_models
    
    def map_movie_media_view_model(movie_media, movie_view_model) -> None:
        """!
        Map the movie_media_list from dictionary into movie view model.

        :return: None.
        """
        movie_view_model.cardsrcaddress = movie_media.get('cardsrcaddress')
        movie_view_model.detailbanneraddress = movie_media.get('detailbanneraddress')
            

