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
        # pattern = r'"name":"(.*?)"'
        pattern = r'"url":"(.*?)","name":"(.*?)"'

        # Find the table containing the movie list
        matches = re.findall(pattern, text)
        # movies = movies[:-1]  # the last item is "'IMDb Top 250 Movies'"
        logger.info(f"re found {len(matches)} matches")
        try:
            id_and_names = []
            for i in range(len(matches)):
                match = matches[i]
                id_and_names.append(f"{match[0]},{match[1]}")
            # match = None
            # id_and_names = [f"{match[1]},{match[2]}" for match in matches]
        except IndexError:
            logger.error(f"error parsing url and title out of:{match}")

        if save_to:
            with open(save_to, "w", encoding="utf-8") as f:
                logger.info(f"saving url and titles to file {save_to}...")
                f.writelines([m + "\n" for m in id_and_names])
            return []
        else:
            return id_and_names  # the last item is "'IMDb Top 250 Movies'"


if __name__ == "__main__":
    movie_crawler = ImdbMovieTitleCrawler()
    movie_crawler.crawl_imdb_top_250_movie_titles(
        save_to=file_in_project_data_dir("out/IMDB_Top_250_Movies.txt")
    )
