from common.http_utils import get_req
from common.os_utils import (
    get_required_env_var,
    file_in_project_data_dir,
    remove_all_file_with_suffix_in_dir,
)

import logging
import json
from os.path import isfile

logger = logging.getLogger(__name__)


class ImdbMetadata:

    SAVE_TO_RAW_DIR = "raw"

    def __init__(self):
        self.omdb_api = get_required_env_var("OMDb_API")
        self.omdb_api_key = get_required_env_var("OMDB_API_KEY")

    def get_movie_by_id(self, imdb_movie_id: str):
        return get_req(
            self.omdb_api, {"i": imdb_movie_id, "apikey": self.omdb_api_key}
        )

    def get_movie_by_title(self, imdb_movie_title: str):
        return get_req(
            self.omdb_api, {"t": imdb_movie_title, "apikey": self.omdb_api_key}
        )

    def batch_download_movie_metadata_from_file(self, url_title_fp, mode):
        logger.info(
            f"downloading movie metadata for movies in file {url_title_fp} with mode={mode}..."
        )
        with open(
            file_in_project_data_dir(url_title_fp), "r", encoding="utf-8"
        ) as f:
            cn = 0
            cn_skipped = 0
            for url_title in f.readlines():

                tokens = url_title.strip().split(",")
                url = tokens[0]
                id = url.split("/")[-2]

                save_to = file_in_project_data_dir(
                    f"{self.SAVE_TO_RAW_DIR}/{id}.json"
                )

                if mode == "only_add_new" and isfile(save_to):
                    cn_skipped += 1

                    # print every 20 movies
                    if cn_skipped % 20 == 0:
                        logger.info(f"{cn_skipped} skipped")

                    continue

                resp_json = self.get_movie_by_id(id)

                with open(save_to, "w", encoding="utf-8") as f:
                    logger.info(f"saving to {save_to}...")
                    json.dump(resp_json, f, indent=4)

                cn += 1

                # print every 20 movies
                if cn % 20 == 0:
                    logger.info(
                        f"{cn} refreshed/updated or added by querying the IMDB API"
                    )

            logger.info(
                f"{cn} refreshed/updated or added by querying the IMDB API"
            )
