# Example 3.26 — AutoML regression (FLAML + California housing, replaces auto_ml + Boston) (README Step 15)
# TODO:
# - X, y = fetch_california_housing(return_X_y=True); train_test_split
# - from flaml import AutoML; automl = AutoML()
# - automl.fit(X_train, y_train, task='regression', time_budget=60)
# - print automl.best_estimator and r2_score on the test set
# Expected: the winning model name and a test R^2.
