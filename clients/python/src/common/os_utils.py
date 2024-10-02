import os
from typing import Any


def get_required_env_var(name: str) -> Any:
    val = os.getenv(name, "not set")
    if val == "not set":
        raise KeyError(f"Required environment variable {name} is missing.")
    return val

def file_in_project_data_dir(file_name: str):
    data_dir = get_required_env_var("OMDB_LOCAL_DATA_DIR")
    return f"{data_dir}/{file_name}"