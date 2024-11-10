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