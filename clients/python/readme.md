# Get Started
__prerequisite__ 
1. have a ES cluster running locally
   1. how to: https://www.elastic.co/guide/en/elasticsearch/reference/current/run-elasticsearch-locally.html 
2. config a `.env` with the following
```
ES_ENDPOINT = http://localhost:9200
ES_USERNAME = 
ES_PASSWORD = 

# OMDB API key generated from https://www.omdbapi.com/apikey.aspx
#   Note: set to be learning purpose on generating keys
OMDb_API=http://www.omdbapi.com
OMDB_API_KEY=
OMDB_LOCAL_DATA_DIR=../../data/imdb
```
__venv__
Make vew `.venv` is none exists, and install requirements to the `.venv` by running:
```
make
```
To run all the tests:
```
make test
```


__for Developers__
To reformat
```
make format
```

# How to

## query imdb api (1000 per day cap) 
To query IMDB for all movies in `../../data/imdb/out/IMDB*.txt`
```
make query_IMDB_movie_metadata
```

## run ES indexing
```
make run_data_indexing
```

## add new movies

First, download the html to folder `../../data/imdb/xxx.html`.
Then, add parser def and call-in-main in file `src/data_import/imdb_movie_title_crawler.py`.
At last, run:
```
make parse_or_crawl_movie_titles
```
The, re indexing ES if necessary.