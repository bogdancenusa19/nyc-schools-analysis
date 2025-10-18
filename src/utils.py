from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW = PROJECT_ROOT / "data" / "raw"
PROC = PROJECT_ROOT / "data" / "processed"

RAW.mkdir(parents=True, exist_ok=True)
PROC.mkdir(parents=True, exist_ok=True)

def load_raw(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW / name)

def save_processed(df: pd.DataFrame, name: str):
    df.to_csv(PROC / name, index=False)
