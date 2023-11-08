import os
from pathlib import Path
from typing import Callable

import numpy as np
from joblib import parallel_backend

DATA_DIR = Path("./data/")


def load_data(array_path: Path) -> np.ndarray:
    raise NotImplementedError


def get_features(array_data: np.ndarray) -> np.ndarray:
    raise NotImplementedError


def walk_filetree(
    extraction_function: Callable[[Path], np.ndarray],
    *,
    parent_directory: Path | None = None,
    target_extension: str = "*.npy",
):
    if parent_directory is None:
        raise ValueError("parent_directory must be specified")
    for dirpath, dirnames, filenames in os.walk(parent_directory):
        for filename in filenames:
            if filename.endswith(target_extension):
                filepath = os.path.join(dirpath, filename)
                filepath = Path(filepath)
                yield extraction_function(filepath)


def main(data_dir: Path) -> None:
    with open(data_dir, "w") as f:
        array_generator = walk_filetree(
            extraction_function=load_data,
            parent_directory=Path(data_dir),
            target_extension="*.npy",
        )
        for data in array_generator:
            # Do something here
            raise NotImplementedError("Define the data extraction behavior.")


if __name__ == "__main__":
    main(DATA_DIR)
