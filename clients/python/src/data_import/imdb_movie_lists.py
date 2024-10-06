import re
from common.os_utils import file_in_project_data_dir, remove_all_file_with_suffix_in_dir
import logging
from imdb_metadata import ImdbMetadata
import csv 

import argparse
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
from enum import Enum

class MovieList(Enum):
    IMDB_TOP_250="IMDB_Top_250_Movies.html"
    OSCAR_BEST_PICTURE_NOMINEES="IMDB_best_picture_oscar_nominees_by_year.csv"

class ImdbMovieList(ABC):
    SAVE_TO=None

    def _save(self, id_and_names):
         # save to file
        with open(self.SAVE_TO, "w", encoding="utf-8") as f:
            logger.info(f"saving url and titles to file {self.SAVE_TO}...")
            f.writelines([m + "\n" for m in id_and_names])

    @abstractmethod
    def parse(self) -> None:
        pass


class ImdbMovieListTop250(ImdbMovieList):

    FP_IMDN_TOP250 = file_in_project_data_dir(MovieList.IMDB_TOP_250.value)
    SAVE_TO = file_in_project_data_dir("out/IMDB_Top_250_Movies.txt")

    def parse(self) -> None:
        # Note: load from manually downloaded html instead of CURL(->403)
        with open(self.FP_IMDN_TOP250, "r", encoding="utf-8") as f:
            text = f.read()

        # find matches from html file
        pattern = r'"url":"(.*?)","name":"(.*?)"'
        matches = re.findall(pattern, text)
        assert len(matches) == 250

        # parse url and title
        try:
            id_and_names = []
            for i in range(len(matches)):
                match = matches[i]
                id_and_names.append(f"{match[0]},{match[1]}")
        except IndexError:
            logger.error(f"error parsing url and title out of:{match}")
        
        self._save(id_and_names)

class ImdbMovieListOscarBestPictureNominees(ImdbMovieList):

    FP_IMDN_OSCAR_BP_NOMINEES = file_in_project_data_dir(MovieList.OSCAR_BEST_PICTURE_NOMINEES.value)
    SAVE_TO = file_in_project_data_dir("out/IMDB_Oscar_Best_Picture_nominees.txt")

    def parse(self) -> None:
        with open(self.FP_IMDN_OSCAR_BP_NOMINEES, "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            next(csv_reader)  # Skip the header
            id_and_names = [f"{row[7]},{row[5]}" for row in csv_reader]
        
        self._save(id_and_names)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # Using the enum values as choices
    parser.add_argument(
        "list", 
        type=str, 
        choices=[movie_list.name for movie_list in MovieList], 
        nargs='+')

    parser.add_argument(
        "--mode", 
        type=str, 
        choices=["only_add_new", "update_specified_list", "replace_all"],
        default="only_add_new")
    
    args = parser.parse_args()
    movie_lists = args.list

    if args.mode == "replace_all":
        remove_all_file_with_suffix_in_dir(file_in_project_data_dir(ImdbMetadata.SAVE_TO_RAW_DIR), filter_file_suffix="json")
    
    imdb = ImdbMetadata()
    for ml in movie_lists:
        if ml == MovieList.IMDB_TOP_250.name:
            _top250 = ImdbMovieListTop250()
            _top250.parse()
            imdb.batch_download_movie_metadata_from_file(_top250.SAVE_TO, mode=args.mode)
        elif ml == MovieList.OSCAR_BEST_PICTURE_NOMINEES.name:
            logger.info("todo: implement oscar best picture parser")
            _oscar_bp_nm = ImdbMovieListOscarBestPictureNominees()
            _oscar_bp_nm.parse()
            imdb.batch_download_movie_metadata_from_file(_oscar_bp_nm.SAVE_TO, mode=args.mode)
        else:
            pass