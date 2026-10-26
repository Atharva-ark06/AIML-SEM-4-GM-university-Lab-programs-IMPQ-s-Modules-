"""Calculate F1 from precision and recall."""
def f1_score(precision, recall):
    total = precision + recall
    return 2 * precision * recall / total if total else 0.0

if __name__ == "__main__":
    print(f1_score(0.8, 0.6))