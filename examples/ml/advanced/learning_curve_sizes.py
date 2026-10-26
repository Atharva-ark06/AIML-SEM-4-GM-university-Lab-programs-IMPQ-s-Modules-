"""Generate monotonically increasing training-set sizes for learning curves."""
def sample_sizes(total: int, steps: int = 5, minimum: int = 2) -> list[int]:
    if total < minimum or minimum < 1 or steps < 1:
        raise ValueError("require total >= minimum >= 1 and steps >= 1")
    if steps == 1:
        return [total]
    values = [round(minimum + i * (total - minimum) / (steps - 1)) for i in range(steps)]
    return sorted(set(values))

if __name__ == "__main__":
    print(sample_sizes(total=100, steps=6, minimum=10))
