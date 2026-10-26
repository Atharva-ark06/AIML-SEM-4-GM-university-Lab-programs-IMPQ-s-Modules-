"""Min-max scaling using min/max learned from training values."""
def fit_minmax(values):
    if not values:
        raise ValueError("values must not be empty")
    return min(values), max(values)

def transform(values, minimum, maximum):
    if minimum == maximum:
        return [0.0 for _ in values]
    return [(x - minimum) / (maximum - minimum) for x in values]

if __name__ == "__main__":
    stats = fit_minmax([10, 20, 30])
    print(transform([15, 25], *stats))