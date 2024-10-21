import logging
from common.es_client import EsClient
from common.time_utils import function_timer
from elasticsearch import NotFoundError as ES_ERROR_NOT_FOUND
from typing import Optional

logger = logging.getLogger(__name__)


class EsIndexer(EsClient):

    def get_index_info(self, index_name: str):
        """return None if a index of specified `index_name` does not exist"""
        try:
            resp = self.es.indices.get(index=index_name)
        except ES_ERROR_NOT_FOUND:
            logger.info(f"Index {index_name} does not exist")
            return None
        return resp

    @function_timer
    def new_index(
        self,
        index_name: str,
        force_recreate: bool = False,
        index_settings: Optional[dict] = None,
    ):
        """
        NOTE: https://www.elastic.co/guide/en/elasticsearch/reference/7.17/indices-create-index.html#create-index-wait-for-active-shards

        index_name: MUST be lower case. Otherwise a runtime error would be returned:
            elasticsearch.BadRequestError: BadRequestError(400, 'invalid_index_name_exception',
                'Invalid index name [TEST_movie_index], must be lowercase')
        """
        # check index existance
        if self.get_index_info(index_name) is not None:
            if force_recreate:
                logger.warning(
                    f"WARN: index {index_name} already exists. \
                        Force recreating by deleting and creating again now..."
                )
                self.delete_index(index_name)
            else:
                logger.warning(
                    f"WARN: index {index_name} already exists. \
                        Skipped recreating."
                )
                return

        if index_settings is None:
            index_setting = {"number_of_shards": 1, "number_of_replicas": 1}
        # https://elasticsearch-py.readthedocs.io/en/v7.17.12/api.html#elasticsearch.client.IndicesClient.create
        # https://www.elastic.co/guide/en/elasticsearch/reference/7.17/indices-create-index.html
        self.es.indices.create(index=index_name, settings=index_setting)

    def delete_index(self, index_name: str):
        if self.get_index_info(index_name) is None:
            logger.warning(f"index {index_name} does not exist. Skip deleting.")
            return

        # https://elasticsearch-py.readthedocs.io/en/v7.17.12/api.html#elasticsearch.client.IndicesClient.delete
        # https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-delete-alias.html
        self.es.indices.delete(index=index_name)

        # assert deletion finished
        assert self.get_index_info(index_name) is None

    def run(self):
        logger.info(f"running indexing for ES: {self.client_info()}")


if __name__ == "__main__":
    indexer = EsIndexer()
    indexer.run()
