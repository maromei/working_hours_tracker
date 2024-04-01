import re

from pathlib import Path
from datetime import datetime


ISO_DATE_FORMAT_RE = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"


def has_open_time(time_file_path: Path) -> bool:

    last_line: str = ""
    with open(time_file_path, "r") as time_file:

        lines = time_file.readlines()
        if len(lines) == 0:
            return False

        last_line = lines[-1]

    pattern = f"(?<=({ISO_DATE_FORMAT_RE} \| )){ISO_DATE_FORMAT_RE}"
    has_end = re.search(pattern, last_line)

    return has_end is None


def add_end_time(time_file_path: Path, time: datetime) -> None:

    if not has_open_time(time_file_path):
        add_start_time(time_file_path, time)

    all_lines: list[str] = []
    with open(time_file_path, "r") as time_file:
        all_lines = time_file.readlines()

    time_str: str = get_time_str(time)
    all_lines[-1] = f"{all_lines[-1]}{time_str}\n"

    with open(time_file_path, "w") as time_file:
        time_str = "".join(all_lines)
        time_file.write(time_str)


def add_start_time(time_file_path: Path, time: datetime) -> None:

    if has_open_time(time_file_path):
        add_end_time(time_file_path, time)

    time_str: str = get_time_str(time)
    time_str = f"{time_str} | "

    with open(time_file_path, "a+") as time_file:
        time_file.write(time_str)


def get_time_str(time: datetime) -> str:

    time = time.replace(microsecond=0)  # gets rid of everything with a .

    time_str = time.isoformat()
    time_str = time_str.split("+")[0]  # gets rid of potential timezone adder

    return time_str
