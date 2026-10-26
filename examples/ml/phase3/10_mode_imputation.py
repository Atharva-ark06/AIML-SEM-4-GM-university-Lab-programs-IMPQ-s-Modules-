"""Impute missing values with the most frequent observed value."""
def mode_impute(values):
    observed = [v for v in values if v is not None]
    if not observed:
        raise ValueError("cannot impute a fully missing sequence")
    counts = {v: observed.count(v) for v in observed}
    mode = max(counts, key=lambda v: (counts[v], str(v)))
    return [mode if v is None else v for v in values]

if __name__ == "__main__":
    print(mode_impute(["red", None, "blue", "red"]))