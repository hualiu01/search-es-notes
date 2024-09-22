import os
from elasticsearch import Elasticsearch

from common.os_utils import get_required_env_var
import logging
from typing import Any

logger = logging.getLogger(__name__)


class ES_client:
    ES_USERNAME = "elastic"
    ES_PASSWORD = os.getenv("ELASTIC_PASSWORD")
    LOCAL_ES_ENDPOINT = "http://localhost:9200"

    def __init__(self) -> None:
        self.es_url = get_required_env_var("ES_ENDPOINT")
        self.es_username = get_required_env_var("ES_USERNAME")
        self.es_password = get_required_env_var("ES_PASSWORD")
        self.es = Elasticsearch(
            self.es_url, basic_auth=(self.es_username, self.es_password)
        )

    def client_info(self) -> Any:
        api_response = self.es.info()
        return api_response
