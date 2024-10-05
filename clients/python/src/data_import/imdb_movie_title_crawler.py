import re
from common.os_utils import file_in_project_data_dir
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class ImdbMovieTitleCrawler:

    FP_IMDN_TOP250 = file_in_project_data_dir("IMDB_Top_250_Movies.html")

    def crawl_imdb_top_250_movie_titles(
        self, save_to: Optional[str] = None
    ) -> list:
        # Note: load from manually downloaded html instead of CURL(->403)
        with open(self.FP_IMDN_TOP250, "r", encoding="utf-8") as f:
            text = f.read()

        # Regular expression pattern to match "name":"<any string>"
        pattern = r'"name":"(.*?)"'

        # Find the table containing the movie list
        movies = re.findall(pattern, text)
        movies = movies[:-1]  # the last item is "'IMDb Top 250 Movies'"

        if save_to:
            with open(save_to, "w", encoding="utf-8") as f:
                logger.info(f"saving IMDB-TOP-250 movie titles file {save_to}")
                f.writelines([m + "\n" for m in movies])
            return []
        else:
            return movies  # the last item is "'IMDb Top 250 Movies'"


if __name__ == "__main__":
    movie_crawler = ImdbMovieTitleCrawler()
    movie_crawler.crawl_imdb_top_250_movie_titles(
        save_to=file_in_project_data_dir("out/IMDB_Top_250_Movies.txt")
    )
