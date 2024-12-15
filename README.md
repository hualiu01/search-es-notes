# search-es-notes

```
> tree -L 3 
.
├── Installation
│   ├── 0_local_installation_steps.md
│   ├── 1_docker_compose_es_kibana.md
│   ├── docker-compose.yml
│   └── setup_kibana_pw.sh
├── LICENSE
├── README.md
├── clients
│   └── python
│       ├── Makefile
│       ├── README.md
│       ├── pyproject.toml
│       ├── requirements.in
│       ├── requirements.txt
│       ├── src
│       └── tests
└── data
    └── imdb
        ├── IMDB_Top_250_Movies.html
        ├── IMDB_best_picture_oscar_nominees_by_year.csv
        ├── out
        ├── raw
        └── readme.md

9 directories, 14 files
```

```
> ➜  search-es-notes git:(main) tree -L 3 -I "*.pyc" -I "__pycache__" clients/python
clients/python
├── Makefile
├── README.md
├── pyproject.toml
├── requirements.in
├── requirements.txt
├── src
│   ├── common
│   │   ├── __init__.py
│   │   ├── es_client.py
│   │   ├── http_utils.py
│   │   ├── os_utils.py
│   │   └── time_utils.py
│   ├── data_import
│   │   ├── __init__.py
│   │   ├── imdb_metadata.py
│   │   └── imdb_movie_lists.py
│   ├── index
│   │   ├── __init__.py
│   │   └── es_indexer.py
│   └── search
│       └── es_searcher.py
└── tests
    ├── common
    │   └── test_es_client.py
    ├── data_import
    │   └── test_imdb_metadata.py
    ├── index
    │   └── test_es_indexer.py
    └── search
        └── test_es_seacher.py
```

# ES architecture

## Node

Q: a node == a machine? or n nodes can run on the same machine?
A: __A node refers to an instance of Elasticsearch__, not a machine. Therefore, __any number of nodes can run on the same machine__.

__Each node in a cluster handles the HTTP request__ for a client who wants to send the request to the cluster.

Each __node contains multiple shards__. And the linit of shards per node in ES is 1000 shards per node.
-  you should have a number that is evenly divisible by the number of data nodes. For instance, if you have 3 data nodes, you should have 3, 6 or 9 shards.

The _master nodes_ handles additional tasks, like __setting status of the cluster__, managing indexes and nodes.

# FTS and Interval Query

_Full Text Search (FTS)_ is a feature in databases that allows searching and matching of text documents based on __relevance and ranking__. It is commonly used in applications such as search engines, content management systems, and data analytics.

An _Interval Query_ is a query that __retrieves data based on overlapping or intersecting intervals__. It is commonly used in applications where data is organized into time intervals, such as scheduling, event management, and time-series data analysis.

Interval Query example:
```
POST _search
{
  "query": {
    "intervals" : {
      "my_text" : {  // match field my_text
        "all_of" : {  // any of the following intervals
          "ordered" : true,  // the two intervals has a order
          "intervals" : [
            {
              "match" : {
                "query" : "my favorite food",
                "max_gaps" : 0,  // no gap between terms
                "ordered" : true  // terms need to be in this order
              }
            },
            {
              "any_of" : {
                "intervals" : [
                  { "match" : { "query" : "hot water" } },
                  { "match" : { "query" : "cold porridge" } }
                ]
              }
            }
          ]
        }
      }
    }
  }
}
```