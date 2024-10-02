import requests
import re
from common.os_utils import get_required_env_var

def query_imdb_top_250_movie_titles() -> list:

    # Note: load from manually downloaded html instead of CURL, because of 403
    data_dir = get_required_env_var("OMDB_LOCAL_DATA_DIR")
    imdb_top_250_local_html_fp = f"{data_dir}/IMDB_Top_250_Movies.html"
    with open(imdb_top_250_local_html_fp, 'r', encoding='utf-8') as f:
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
