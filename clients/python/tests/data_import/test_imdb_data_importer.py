import logging 

logger = logging.getLogger(__name__)

from data_import.imdb_data_importer import ImdbDataImporter

imdb_data_importer = ImdbDataImporter()

def test_get_movie_by_id():
    resp_json = imdb_data_importer.get_movie_by_id("tt3896198")

    assert type(resp_json) == dict
    logger.info(resp_json)
