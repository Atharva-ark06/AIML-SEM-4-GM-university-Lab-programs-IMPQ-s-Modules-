"""Summarize fold scores without external dependencies."""
def summarize_scores(scores):
    if not scores: raise ValueError("scores must not be empty")
    average=sum(scores)/len(scores)
    spread=max(scores)-min(scores)
    return {"mean":average,"min":min(scores),"max":max(scores),"range":spread}
if __name__ == "__main__": print(summarize_scores([0.81,0.84,0.79,0.83]))