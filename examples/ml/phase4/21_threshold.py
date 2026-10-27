"""Apply a threshold to scores in [0, 1]."""
def predict_threshold(scores,threshold=0.5):
    if not 0<=threshold<=1: raise ValueError("threshold must be in [0, 1]")
    if any(not 0<=s<=1 for s in scores): raise ValueError("scores must be in [0, 1]")
    return [int(s>=threshold) for s in scores]
if __name__ == "__main__": print(predict_threshold([0.2,0.55,0.9],0.6))