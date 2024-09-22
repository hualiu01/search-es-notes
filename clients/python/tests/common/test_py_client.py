from common.py_client import ES_client
import logging

logger = logging.getLogger(__name__)

es = ES_client()


def test_es_connection():
    logger.info(es.client_info())
