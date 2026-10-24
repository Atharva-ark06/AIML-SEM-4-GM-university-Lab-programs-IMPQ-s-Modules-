"""Show a safe, explicit separation of target and input columns."""
import pandas as pd


def split_target(frame, target_column):
    """Return features and target, rejecting an absent target column."""
    if target_column not in frame.columns:
        raise KeyError(f"Target column not found: {target_column}")
    target = frame[target_column].copy()
    features = frame.drop(columns=[target_column]).copy()
    return features, target


def main():
    frame = pd.DataFrame({"distance_km": [10, 20, 30], "cost_inr": [100, 200, 300]})
    x, y = split_target(frame, "cost_inr")
    print("Features:", list(x.columns))
    print("Target:", y.name)


if __name__ == "__main__":
    main()
