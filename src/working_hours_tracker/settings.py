import os
from pathlib import Path


def get_time_file_path() -> Path:
    """
    Get the file path to where the times will be saved.

    It is first checked if there is a path in the environment variable
    :code:`TIME_FILE_PATH`. Otherwise it looks for the file at
    :py:func:`settings.get_base_dir` :code:`/times.txt`.

    If the file / directory does not exist, it will be created.

    Returns:
        Path: Path to txt file where the times will be saved.
    """

    path_str: str|None = os.environ.get("TIME_FILE_PATH")

    time_file_path: Path = None
    if path_str is None:
        time_file_path = get_base_dir() / "times.txt"
    else:
        time_file_path = Path(path_str)

    if time_file_path.is_file():
        return time_file_path

    os.mkdir(time_file_path.parent)
    open(time_file_path, "r").close()

    return time_file_path


def get_base_dir() -> Path:
    """
    Gets the Path to the base directory. This directory is the upper most
    level that contains the entire project. Here pretty much all configs
    will be saved.

    Returns:
        Path:
    """

    # The parent chaining is due to the frozen file resulting in
    # addnotespace/lib/addnotespace/settings.pyc.
    # This parent chaining just so happens to also correspond to the
    # dev directory structure.
    BASE_PATH = Path(__file__).parent.parent.parent

    return BASE_PATH
