import requests
import re
from common.os_utils import file_in_project_data_dir

def query_imdb_top_250_movie_titles() -> list:

    # Note: load from manually downloaded html instead of CURL, because of 403
    with open(file_in_project_data_dir("IMDB_Top_250_Movies.html"), 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Regular expression pattern to match "name":"<any string>"
    pattern = r'"name":"(.*?)"'

    # Find the table containing the movie list
    movies = re.findall(pattern, text)

    # Scrape and print movie details
    titles = []
    for movie in movies:
        title = movie
        titles.append(title)

    return titles[:-1] # the last item is "'IMDb Top 250 Movies'"
