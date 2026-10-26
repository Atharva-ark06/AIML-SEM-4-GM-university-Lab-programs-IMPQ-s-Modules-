"""Small example showing why metric choice depends on task costs."""
def choose_metric(task):
    recommendations = {
        "rare_positive_detection": ["recall", "precision", "PR-AUC"],
        "balanced_classification": ["precision", "recall", "F1", "accuracy"],
        "regression": ["MAE", "RMSE"],
        "probability_estimation": ["Brier score", "calibration plot"],
    }
    try:
        return recommendations[task]
    except KeyError as exc:
        raise ValueError(f"unknown task: {task}") from exc

if __name__ == "__main__":
    print(choose_metric("rare_positive_detection"))