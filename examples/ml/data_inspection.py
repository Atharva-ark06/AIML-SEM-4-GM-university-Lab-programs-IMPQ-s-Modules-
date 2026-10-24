"""Inspect the included synthetic travel dataset."""
from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "datasets" / "toy_travel.csv"


def main():
    frame = pd.read_csv(DATASET)
    print("Shape:", frame.shape)
    print("\nColumn types:\n", frame.dtypes)
    print("\nMissing values:\n", frame.isna().sum())
    print("\nPreview:\n", frame.head().to_string(index=False))


if __name__ == "__main__":
    main()
