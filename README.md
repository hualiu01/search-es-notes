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
│   ├── python
│   │   ├── Makefile
│   │   ├── README.md
│   │   ├── pyproject.toml
│   │   ├── requirements.in
│   │   ├── requirements.txt
│   │   ├── src
│   │   └── tests
│   └── restapi
│       ├── bulk_inseart_docs.sh
│       ├── data
│       ├── delete_index.sh
│       ├── new_index.sh
│       └── search_1_to_be_or_not_to_be.sh
├── data
│   ├── imdb
│   │   ├── IMDB_Top_250_Movies.html
│   │   ├── IMDB_best_picture_oscar_nominees_by_year.csv
│   │   ├── out
│   │   ├── raw
│   │   └── readme.md
│   └── iyf
│       ├── IYF_top_score_page__0.html
│       ├── out
│       └── raw
└── docs
    ├── 0_es_overview.md
    ├── 1_es_architecture.md
    ├── 2_es_query_lang.md
    ├── 3_es_rest_api_examples.md
    └── ElasticStack7.pdf

15 directories, 24 files
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
│   │   ├── dynamic_webpage_utils.py
│   │   ├── es_client.py
│   │   ├── http_utils.py
│   │   ├── os_utils.py
│   │   └── time_utils.py
│   ├── data_import
│   │   ├── __init__.py
│   │   ├── imdb_metadata.py
│   │   ├── imdb_movie_lists.py
│   │   └── iyf_movie_list.py
│   ├── index
│   │   ├── __init__.py
│   │   └── es_indexer.py
│   └── search
│       └── es_searcher.py
└── tests
    ├── common
    │   ├── test_dynamic_webpage_utils.py
    │   └── test_es_client.py
    ├── data_import
    │   └── test_imdb_metadata.py
    ├── index
    │   └── test_es_indexer.py
    └── search
        └── test_es_seacher.py

10 directories, 23 files
```



