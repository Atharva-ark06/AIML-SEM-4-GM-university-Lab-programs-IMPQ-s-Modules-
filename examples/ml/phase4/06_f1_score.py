"""F1 score from precision and recall."""
def f1_score(precision, recall):
    denominator=precision+recall
    return 2*precision*recall/denominator if denominator else 0.0
if __name__ == "__main__": print(f1_score(0.8,0.6))