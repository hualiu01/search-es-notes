# search-es-notes

```
> tree -L 3                          
.
├── Installation
│   └── 0_local_installation_steps.md
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
13 directories, 15 files
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
    └── ingest
        └── test_ingester.py
```