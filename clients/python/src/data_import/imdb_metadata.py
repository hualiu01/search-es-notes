from common.http_utils import get_req
from common.os_utils import get_required_env_var


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
