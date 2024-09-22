import os
from elasticsearch import Elasticsearch

class ES_client:
    
    ES_USERNAME = 'elastic'
    ES_PASSWORD = os.getnenv('ELASTIC_PASSWORD')
    
    def __init__(self):
        self.es = Elasticsearch()