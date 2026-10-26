"""Predict the most frequent training label as a simple baseline."""
def majority_label(labels):
    if not labels:
        raise ValueError("labels must not be empty")
    counts = {label: labels.count(label) for label in labels}
    return max(counts, key=lambda label: (counts[label], str(label)))

def predict_majority(training_labels, number_of_rows):
    return [majority_label(training_labels)] * number_of_rows

if __name__ == "__main__":
    print(predict_majority(["cat", "dog", "cat"], 4))