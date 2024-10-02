from data_import.imdb_index_top_250 import query_imdb_top_250_movie_titles
import logging 

logger = logging.getLogger(__name__)

def test_query_imdb_top_250():
    movie_titles = query_imdb_top_250_movie_titles()
    
    logger.info(movie_titles)
    assert(len(movie_titles)==250)
