import logging
import json

logger = logging.getLogger(__name__)

from data_import.imdb_metadata import ImdbMetadata
from common.os_utils import file_in_project_data_dir

imdb_data_importer = ImdbMetadata()


def test_get_movie_by_id():
    resp_json = imdb_data_importer.get_movie_by_id("tt3896198")

    assert type(resp_json) == dict
    assert len(resp_json.keys()) > 1

    save_to = file_in_project_data_dir("out/example_movie_meta_data.json")
    logger.info(f"saving to {save_to}...")
    with open(save_to, "w", encoding="utf-8") as f:
        json.dump(resp_json, f, indent=4)


def test_get_movie_by_title():
    resp_json = imdb_data_importer.get_movie_by_title(
        "Guardians of the Galaxy Vol. 2"
    )

    assert type(resp_json) == dict
    assert len(resp_json.keys()) > 1

    logger.info(resp_json)


def test_get_movie_by_title_same_title_different_ids():
    resp_json = imdb_data_importer.get_movie_by_title("Crash")

    assert type(resp_json) == dict  # only one match returned!

    logger.info(resp_json)
