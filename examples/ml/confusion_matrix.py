"""Print a confusion matrix and explain its layout."""
from sklearn.metrics import confusion_matrix


def main():
    actual = [0, 0, 1, 1, 1, 0]
    predicted = [0, 1, 1, 1, 0, 0]
    matrix = confusion_matrix(actual, predicted, labels=[0, 1])
    print("Rows = actual class; columns = predicted class")
    print(matrix)


if __name__ == "__main__":
    main()
