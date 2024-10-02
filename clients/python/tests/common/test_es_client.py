from common.es_client import EsClient
import logging

logger = logging.getLogger(__name__)

es = EsClient()


def test_es_connection():
    logger.info(es.client_info())
