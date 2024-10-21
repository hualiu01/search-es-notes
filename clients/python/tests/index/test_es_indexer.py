from pytest import fixture
import pytest

from index.es_indexer import EsIndexer

import logging
logger = logging.getLogger(__name__)

@fixture
def default_es_indexer():
    return EsIndexer()

test_index_name = "test_movie_index"

# def test_new_index(default_es_indexer):
#     default_es_indexer.new_index(index_name="test_movie_index")

def test_get_index_info_none_existed(default_es_indexer):
    resp = default_es_indexer.get_index_info(index_name="test_a_none_exit_index")
    assert resp is None

def test_delete_index_none_existed(default_es_indexer):
    resp = default_es_indexer.delete_index(index_name="test_a_none_exit_index")
    assert resp is None

# maek test_new_index as dependent
@pytest.mark.dependency(name="test_new_index")
def test_new_index(default_es_indexer):
    default_es_indexer.new_index(index_name=test_index_name, force_recreate=True)
    resp = default_es_indexer.get_index_info(index_name=test_index_name)
    
    # test
    assert resp is not None
    logger.info(resp)

# Mark test_get_index_info_existed as dependent on test_new_index
# @pytest.mark.dependency(depends=["test_new_index"])
# def test_delete_index(default_es_indexer):
#     default_es_indexer.delete_index(index_name=test_index_name)