"""Calculate missing-value percentages for a column represented by None."""
def missing_percentage(values):
    if not values:
        return 0.0
    return 100.0 * sum(value is None for value in values) / len(values)

if __name__ == "__main__":
    print(missing_percentage([2, None, 5, None]))