import os
import glob
from typing import Any
import logging

logger = logging.getLogger(__name__)


def get_required_env_var(name: str) -> Any:
    val = os.getenv(name, "not set")
    if val == "not set":
        raise KeyError(f"Required environment variable {name} is missing.")
    return val


def file_in_project_data_dir(file_name: str):
    data_dir = get_required_env_var("OMDB_LOCAL_DATA_DIR")
    return f"{data_dir}/{file_name}"


def remove_all_file_with_suffix_in_dir(
    dir: str, filter_file_suffix: str = "json"
):

    # Find all files in the folder with specified suffix
    target_suffix = glob.glob(os.path.join(dir, f"*.{filter_file_suffix}"))

    # Remove each target file
    for t_file in target_suffix:
        logger.info(f"removing {t_file}...")
        os.remove(t_file)
        print(f"Deleted: {t_file}")
