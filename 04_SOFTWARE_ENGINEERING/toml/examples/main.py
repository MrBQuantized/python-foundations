import tomllib
from pprint import pprint
from pathlib import Path
import os

PATH = Path(__file__).resolve().parent
FILE = PATH / "config.toml"
print(PATH)
os.chdir(PATH)
print("Current working directory: ", os.getcwd())


def load_toml() -> dict:
    """Load TOML data from file"""

    with open(FILE, 'rb') as f:
        toml_data: dict = tomllib.load(f)
        return toml_data
    

if __name__ == "__main__":
    data: dict = load_toml()
    pprint(data, sort_dicts=False)