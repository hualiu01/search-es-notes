import os
from typing import Any


def get_required_env_var(name: str) -> Any:
    val = os.getenv(name, "not set")
    if val == "not set":
        raise KeyError(f"Required environment variable {name} is missing.")
    return val
