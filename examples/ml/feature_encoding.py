"""Encode categorical values using one-hot encoding."""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def encode_categories(values):
    """Fit an encoder and return encoded array and output feature names."""
    frame = pd.DataFrame({"category": values})
    encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
    transformed = encoder.fit_transform(frame[["category"]])
    return transformed, encoder.get_feature_names_out(["category"]).tolist()


def main():
    encoded, names = encode_categories(["budget", "standard", "premium", "budget"])
    print("Features:", names)
    print(encoded.astype(int))


if __name__ == "__main__":
    main()
