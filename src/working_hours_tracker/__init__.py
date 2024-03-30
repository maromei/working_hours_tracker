import os
import dotenv

from pathlib import Path

dotenv_path_str: str | None = os.environ.get("WORKING_HOURS_TRACKER_DOTENV_PATH")

dotenv_path: Path = Path()
if dotenv_path_str is None:
    dotenv_path = Path(__file__).parent / "default.env"
else:
    dotenv_path = Path(dotenv_path_str)

dotenv.load_dotenv(dotenv_path)
