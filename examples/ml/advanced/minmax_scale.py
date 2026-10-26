"""Min-max scale numeric values to a requested interval."""

def minmax(values: list[float], low: float = 0.0, high: float = 1.0) -> list[float]:
    if not values:
        raise ValueError("values cannot be empty")
    if high < low:
        raise ValueError("high must be greater than or equal to low")
    minimum, maximum = min(values), max(values)
    if minimum == maximum:
        return [low for _ in values]
    return [low + (x - minimum) * (high - low) / (maximum - minimum) for x in values]

if __name__ == "__main__":
    print(minmax([2, 4, 6, 8]))
