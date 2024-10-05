from common.http_utils import get_req
from common.os_utils import get_required_env_var, file_in_project_data_dir, remove_all_file_with_suffix_in_dir

import logging 
import json
from os.path import isfile

logger = logging.getLogger(__name__)

class ImdbMetadata:
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
    
    def download_data(url_title):
        tokens = url_title.strip().split(",")
        url = tokens[0]
        title = ",".join(tokens[1:])
        concat_title = "_".join(title.lower().split(" "))
        
        save_to = file_in_project_data_dir(f"raw/{concat_title}.json")
        if isfile(save_to):
            return
        resp_json = imdb_data_importer.get_movie_by_id(url.split("/")[-2])
        
        with open(save_to, "w", encoding="utf-8") as f:
            logger.info(f"saving to {save_to}...")
            json.dump(resp_json, f, indent=4)


    
if __name__ == "__main__":
    imdb = ImdbMetadata()
    imdb_data_importer = ImdbMetadata()

    conf_redownload_all = False

    if conf_redownload_all:
        remove_all_file_with_suffix_in_dir(file_in_project_data_dir("raw"), filter_file_suffix="json")
    
    with open(file_in_project_data_dir("out/IMDB_Top_250_Movies.txt"), 'r',
              encoding='utf-8') as f:
        cn = 0
        for line in f.readlines():
            ImdbMetadata.download_data(url_title=line)
            cn += 1
            logger.info(f"{cn} done")
