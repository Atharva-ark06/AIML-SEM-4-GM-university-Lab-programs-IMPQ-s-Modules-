"""One-hot encode a category from a known vocabulary."""
def one_hot(value,vocabulary):
    if value not in vocabulary: raise ValueError("unknown category")
    return [int(value==category) for category in vocabulary]
if __name__ == "__main__": print(one_hot("dog",["cat","dog","bird"]))