"""Suggest metrics based on a declared task and objective."""
def metric_guidance(task,priority):
    guidance={
      ("classification","rare_positive"): ["recall","precision","PR-AUC","confusion matrix"],
      ("classification","balanced"): ["macro-F1","accuracy","confusion matrix"],
      ("regression","large_errors_costly"): ["RMSE","residual analysis"],
      ("regression","typical_absolute_error"): ["MAE","residual analysis"],
    }
    key=(task,priority)
    if key not in guidance: raise ValueError("unsupported task/priority combination")
    return guidance[key]
if __name__ == "__main__": print(metric_guidance("classification","rare_positive"))