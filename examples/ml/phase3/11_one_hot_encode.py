"""One-hot encode categories in a stable, sorted column order."""
def one_hot(values, categories=None):
    categories = sorted(set(values)) if categories is None else list(categories)
    return categories, [[int(value == category) for category in categories] for value in values]

if __name__ == "__main__":
    labels, matrix = one_hot(["blue", "red", "blue"])
    print(labels, matrix)