import logging 
import json

logger = logging.getLogger(__name__)

from data_import.imdb_data_importer import ImdbDataImporter
from common.os_utils import file_in_project_data_dir

imdb_data_importer = ImdbDataImporter()

def test_get_movie_by_id():
    resp_json = imdb_data_importer.get_movie_by_id("tt3896198")

    assert type(resp_json) == dict
    assert len(resp_json.keys()) > 1 

    save_to = file_in_project_data_dir("example_movie_meta_data.json")
    logger.info(f"saving to {save_to}...")
    with open(save_to, 'w', encoding='utf-8') as f:
        json.dump(resp_json, f, indent=4)
