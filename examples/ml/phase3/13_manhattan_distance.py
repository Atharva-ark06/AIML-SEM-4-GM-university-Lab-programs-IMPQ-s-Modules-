"""Manhattan distance between two equal-dimensional vectors."""
def manhattan_distance(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have equal dimensions")
    return sum(abs(a - b) for a, b in zip(left, right))

if __name__ == "__main__":
    print(manhattan_distance([1, 2], [4, 6]))