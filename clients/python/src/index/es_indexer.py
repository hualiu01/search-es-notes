import logging
from common.es_client import EsClient

logger = logging.getLogger(__name__)


class EsIndexer:
    def __init__(self):
        self.es_client: EsClient = EsClient()

    def run(self):
        logger.info(f"running indexing for ES {self.es_client.client_info()}")


if __name__ == "__main__":
    indexer = EsIndexer()
    indexer.run()
