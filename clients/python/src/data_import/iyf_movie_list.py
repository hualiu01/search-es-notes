"""
The IyfMovieList class provides ways to 
1) query and download JS rendered dynamic webpage of "best movies" and "most popular movies", and add checkpoint by
    saving to  `data/iyf/out/iyf_movie_list_of_rate.json` and `data/iyf/out/iyf_movie_list_of_popularity.json`
2) parse the webpage to get movie name, rating, popularity, genra and save to `data/iyf/raw/<movie_name>_<year>.json`
"""
from common.os_utils import (
    get_required_env_var,
    file_in_project_data_dir,
)
from common.dynamic_webpage_utils import dynamic_query_url_with_chrome_driver_and_save
import logging

import argparse
from abc import ABC, abstractmethod
from enum import Enum

logger = logging.getLogger(__name__)

class IyfMovieList(ABC):
    DOWNLOAD_HTML = None  # the place to save the raw html after query the iyf url
    SAVE_TO = None  # the place to sve the parsed movie id(formed by concating "title" and "year") and movie titles
    
    @abstractmethod
    def download(self) -> None:
        """
        Download iyf top score and most populary from website and save to local data iyf folder
        """
        pass

    # @abstractmethod
    # def parse(self) -> None:
    #     """
    #     A parse function which loads local stored move list files in various formats (such as .html, .csv).
    #         Then, parse out tuple (id, name). At last store in self.SAVE_TO by calling self._save().
    #     """
    #     pass

    def _save(self, id_and_names):
        # save to file
        with open(self.SAVE_TO, "w", encoding="utf-8") as f:
            logger.info(f"saving url and titles to file {self.SAVE_TO}...")
            f.writelines([m + "\n" for m in id_and_names])
        
class IyfMovieListTopScores(IyfMovieList):
    
    TOP_SCORE_PAGE_N = str(get_required_env_var("TOP_SCORE_PAGE_N"))
    DOWNLOAD_HTML_FILE_PREFIX = "IYF_top_score_page_"
    IYF_TOP_SCORE_PAGE_N = get_required_env_var("IYF_TOP_SCORE_PAGE_N")
    
    def download(self):
        for page in range(int(self.TOP_SCORE_PAGE_N)):
            logger.info(f"download {str(page+1)} of {self.TOP_SCORE_PAGE_N}...")
            download_to = file_in_project_data_dir(
                file_name=f"{self.DOWNLOAD_HTML_FILE_PREFIX}_{page}.html",
                data_type="IYF")
            dynamic_query_url_with_chrome_driver_and_save(
                url = f"{self.IYF_TOP_SCORE_PAGE_N}{str(page+1)}",
                save_to = download_to)
            logger.info(f"saved to {download_to}...")

if __name__ == "__main__":
    iyf = IyfMovieListTopScores()
    # iyf.download()




    
