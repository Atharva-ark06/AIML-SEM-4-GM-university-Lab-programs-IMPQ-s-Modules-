"""Count labels and report proportions."""
from collections import Counter
def class_distribution(labels):
    if not labels: raise ValueError("labels must not be empty")
    counts=Counter(labels); total=len(labels)
    return {label:{"count":count,"proportion":count/total} for label,count in counts.items()}
if __name__ == "__main__": print(class_distribution(["pass","fail","pass"]))