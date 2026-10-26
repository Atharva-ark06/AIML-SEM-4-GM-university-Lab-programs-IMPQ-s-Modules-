"""Deterministic index split for demonstrating train/test separation."""
def split_indices(size, test_fraction=0.2):
    if size < 2 or not 0 < test_fraction < 1:
        raise ValueError("size >= 2 and fraction between 0 and 1 required")
    cut = max(1, min(size - 1, round(size * (1 - test_fraction))))
    return list(range(cut)), list(range(cut, size))

if __name__ == "__main__":
    print(split_indices(10, 0.3))