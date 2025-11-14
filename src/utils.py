#Stores general functions used across whole project.

from pathlib import Path
import pandas as pd

def load_CSV(path: str | Path) -> pd.DataFrame:
    """Load a CSV file and reutrn a pandas data frame."""
    return pd.read_csv(path)

def save_CSV(dataframe: pd.DataFrame, path: str | Path):
    """Saves a dataframe as a CSV file."""
    Path(path).parent.mkdir(parents = True, exist_ok = True)
    dataframe.to_csv(path, index = False)
