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
> tree -L 3 -I "*.pyc" clients/python
clients/python
├── Makefile
├── README.md
├── pyproject.toml
├── requirements.in
├── requirements.txt
├── src
│   ├── common
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── es_client.py
│   │   ├── http_utils.py
│   │   └── os_utils.py
│   ├── data_import
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── imdb_metadata.py
│   │   └── imdb_movie_lists.py
│   ├── index
│   │   ├── __init__.py
│   │   └── es_indexer.py
│   └── search
│       └── es_searcher.py
└── tests
    ├── common
    │   ├── __pycache__
    │   └── test_es_client.py
    ├── data_import
    │   ├── __pycache__
    │   └── test_imdb_metadata.py
    └── ingest
        ├── __pycache__
        └── test_ingester.py
```