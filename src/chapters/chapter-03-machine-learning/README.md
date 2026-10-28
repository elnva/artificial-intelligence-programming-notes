# Chapter 03 — Machine Learning

> Book chapter: **Chapter 3 — Machine Learning** (book pages 53–116).

## Goal

By the end of this chapter you will:

- Explain in your own words the five families of machine learning the chapter covers: supervised (classification and regression), unsupervised, semi-supervised, reinforcement, and ensemble learning.
- Have hand-typed every Python example in the chapter (Examples 3.1 through 3.28) and attempted all 21 exercises.
- Know the scikit-learn rhythm by heart: load data → split into train/test → `fit()` → `predict()` → score.
- Know when an AutoML tool (PyCaret, LazyPredict) saves you time, and when it hides too much.

## Prerequisites

- Chapter 02 done: `.venv` active, NumPy, pandas, Matplotlib and scikit-learn installed.
- Run every example from inside `examples/` (`cd src/chapters/chapter-03-machine-learning/examples`) so relative file names such as `iris.csv` resolve next to the scripts.

## Modernization vs. the book

| Book | This repo | Why |
| ---- | --------- | --- |
| `gym` (Example 3.23) | `gymnasium` | OpenAI Gym is unmaintained; Gymnasium is its drop-in successor. `reset()` now returns `(obs, info)` and `step()` returns five values (`terminated` and `truncated` replace `done`). Use `CartPole-v1` with `render_mode="human"`. |
| `auto_ml` + Boston housing (Example 3.26) | `flaml` + California housing | `auto_ml` stopped at Python 3.6, and the Boston dataset was removed from scikit-learn 1.2. FLAML is a small, maintained AutoML library; California housing is the book's own Exercise 3.18 dataset. |
| PyCaret, LazyPredict locally (Examples 3.27, 3.28) | Google Colab | Both pin old scikit-learn versions and would downgrade the library in `.venv`. The book itself suggests Colab for LazyPredict. |

If any other example breaks on Python 3.10 / scikit-learn 1.7, note it in `notes.md` and we patch it in chat.

## Chapter outline (book sections you will cover)

- 3.1 Introduction
- 3.2 Supervised Learning: Classifications — SVM, naive Bayes, LDA, PCA, decision tree, random forest, K-NN, comparison
- 3.3 Supervised Learning: Regressions — linear, polynomial, least squares, multiple linear, logistic
- 3.4 Unsupervised Learning — K-means
- 3.5 Semi-supervised Learning — label spreading
- 3.6 Reinforcement Learning — Q-learning, CartPole
- 3.7 Ensemble Learning — voting classifier and regressor
- 3.8 AutoML
- 3.9 PyCaret
- 3.10 LazyPredict
- 3.11 Summary
- 3.12 Chapter Review Questions

## How to read the steps

Each step has four parts:

1. **Teach** — a short explanation of what the step is about and why it matters.
2. **Do** — the concrete action you take.
3. **Expected** — what you should see if it worked.
4. **Tell me when done** — your cue to ping Claude so the next step gets unlocked.

Do not skim ahead. The point is to absorb each idea before moving on.

## Steps

### Step 1 — Read section 3.1 (what machine learning is)

- **Teach**: Traditional programming is rules + data → answers. Machine learning flips it: data + answers → rules (a trained model). Section 3.1 sorts ML into supervised, unsupervised, semi-supervised, reinforcement, and ensemble learning. Every later step in this chapter belongs to one of those boxes.
- **Do**: Read section 3.1. In `notes.md`, under **Insights**, write one sentence per family (five sentences) in your own words.
- **Expected**: Five short bullets in `notes.md`. No code yet.
- **Tell me when done**: reply with `step 1 done`.

### Step 2 — Install the extra libraries for this chapter

- **Teach**: Most of the chapter needs only scikit-learn, which you already have. A few examples need more: Statsmodels (Example 3.15a), NetworkX (Example 3.22 draws the routing graph), Gymnasium (Example 3.23), and FLAML (Example 3.26, see the modernization table).
- **Do**: With `(.venv)` active, run:
  ```bash
  pip install statsmodels networkx "gymnasium[classic-control]" "flaml[automl]"
  ```
- **Expected**: `pip list` shows `statsmodels`, `networkx`, `gymnasium`, `flaml`.
- **Tell me when done**: reply with `step 2 done`.

### Step 3 — SVM: your first classifier, and Exercises 3.1, 3.2 (Examples 3.1, 3.2)

- **Teach**: A support vector machine finds the boundary that separates classes with the widest possible margin. In scikit-learn every classifier follows the same pattern: create it, call `fit(X, y)` with known samples, then call `predict()` on new ones. `X` is a 2-D array (one row per sample, one column per feature); `y` is a 1-D array of labels.
- **Do**:
  1. Open `examples/01-svm-gender.py`. Build `X` from four people (height, weight, shoe size) and `y` from their genders (0/1). Train `svm.SVC()`, predict a new person.
  2. Open `examples/02-svm-iris.py`. Load iris with `datasets.load_iris()`, train an SVM on it, predict one flower.
  3. **Exercise 3.1** — Open `exercises/ex-3-1-svm-six-samples.py`. Same as Example 3.1 with six samples.
  4. **Exercise 3.2** — Open `exercises/ex-3-2-svm-petal-features.py`. Same as Example 3.2 but use only petal length and width (columns 2 and 3) as `X`. Note in `notes.md` whether the prediction changed.
- **Expected**: Each script prints a predicted class.
- **Tell me when done**: reply with `step 3 done`.

### Step 4 — Iris from a CSV file, and Exercise 3.3 (Examples 3.3, 3.4)

- **Teach**: Real data usually arrives as CSV, so these two examples read iris with `pd.read_csv()` instead of the built-in loader. Example 3.4 also tours the pandas inspection toolkit: `df.shape`, `df.head()`, `df.tail()`, `df.describe()`, `df.isna().sum()`, `df.groupby(...).size()`, `df.hist()`, `scatter_matrix()`. Run those every time you meet a new dataset.
- **Do**:
  1. Open `examples/04-svm-iris-url.py` first. Read iris from the URL in the book, inspect it with the functions above, train an SVM.
  2. Save that same CSV as `examples/iris.csv` (`curl -o iris.csv <URL from the book>`).
  3. Open `examples/03-svm-iris-csv.py`. Read `iris.csv` from disk and train the SVM.
  4. **Exercise 3.3** — Open `exercises/ex-3-3-iris-scatter.py`. Scatter-plot sepal length vs. sepal width for every flower.
- **Expected**: Shape `(150, 5)`, summary tables, a histogram window, a scatter matrix, a scatter plot.
- **Tell me when done**: reply with `step 4 done`.

### Step 5 — Breast cancer data and train/test split, and Exercise 3.4 (Examples 3.5, 3.6)

- **Teach**: Testing a model on the data it trained on tells you nothing. `train_test_split()` holds back a share of the data (20 % here) that the model never sees during training. `confusion_matrix` and `classification_report` then show where the model is right and wrong, class by class.
- **Do**:
  1. Open `examples/05-cancer-data.py`. Load `load_breast_cancer()`, print feature names, data, and target names.
  2. Open `examples/06-svm-cancer.py`. Put the data in a DataFrame, split 80/20, train `SVC`, print the confusion matrix and classification report.
  3. **Exercise 3.4** — Open `exercises/ex-3-4-cancer-histograms.py`. Plot histograms of mean radius, area (size), texture, and smoothness.
- **Expected**: A 2×2 confusion matrix and a report with precision/recall/f1; four histograms.
- **Tell me when done**: reply with `step 5 done`.

### Step 6 — Naive Bayes and LDA, and Exercises 3.5, 3.6 (Examples 3.7, 3.8)

- **Teach**: Naive Bayes assumes features are independent and picks the most probable class with Bayes' theorem. It is fast and works well with little data. LDA (linear discriminant analysis) projects the data onto the direction that best separates the classes. `make_classification()` generates a fake dataset of any size, which is handy for experiments.
- **Do**:
  1. Open `examples/07-naive-bayes.py`. Load iris with `return_X_y=True`, train `GaussianNB`, predict one flower.
  2. Open `examples/08-lda.py`. Generate 1,000 samples × 4 features with `make_classification()`, train `LinearDiscriminantAnalysis`, predict one sample.
  3. **Exercise 3.5** — Open `exercises/ex-3-5-save-load-model.py`. Train naive Bayes, save the model to a file with `joblib.dump`, load it with `joblib.load`, predict with the loaded model.
  4. **Exercise 3.6** — Open `exercises/ex-3-6-lda-six-features.py`. Same as Example 3.8 with 6 features and 2,000 samples.
- **Expected**: Predicted classes print; a `.joblib` file appears next to the exercise.
- **Tell me when done**: reply with `step 6 done`.

### Step 7 — PCA (dimension reduction), and Exercise 3.7 (Examples 3.9, 3.10)

- **Teach**: PCA is not a classifier. It rotates the data so the first few axes (components) hold most of the variation, which lets you squash four features down to two and plot them. It is often a pre-processing step before classification.
- **Do**:
  1. Open `examples/09-pca.py`. Generate data with `make_classification()`, fit `PCA`, print the explained variance and components.
  2. Open `examples/10-pca-iris.py`. Plot raw iris in 3-D, transform it with PCA, plot PC1 vs. PC2 colored by species.
  3. **Exercise 3.7** — Open `exercises/ex-3-7-pca-cancer.py`. Same as Example 3.10 on the breast cancer data.
- **Expected**: In the PCA plot the species form visible clusters.
- **Tell me when done**: reply with `step 7 done`.

### Step 8 — Decision tree, random forest, K-NN, and Exercises 3.8, 3.9 (Examples 3.11, 3.12, 3.13)

- **Teach**: A decision tree asks a chain of yes/no questions about the features. A random forest trains many trees on random slices of the data and lets them vote, which usually beats one tree. K-NN classifies a point by the majority label of its K nearest neighbors. All three use the same `fit`/`predict` calls, so only the import changes.
- **Do**:
  1. Open `examples/11-decision-tree.py`. Split iris, train `DecisionTreeClassifier`, print how many test points were mislabeled out of the total.
  2. Open `examples/12-random-forest.py`. Same with `RandomForestClassifier`.
  3. Open `examples/13-knn.py`. Same with `KNeighborsClassifier`.
  4. **Exercise 3.8** — Open `exercises/ex-3-8-tree-wine.py`. Decision tree on `load_wine()`.
  5. **Exercise 3.9** — Open `exercises/ex-3-9-forest-diabetes.py`. Random forest on `load_diabetes()`. Its target is a continuous number, not a class: try `RandomForestRegressor` and note in `notes.md` why a classifier is the wrong tool here.
- **Expected**: "Mislabeled N out of M" lines; N is small for iris.
- **Tell me when done**: reply with `step 8 done`.

### Step 9 — Compare classifiers in one loop, and Exercise 3.10 (Example 3.14)

- **Teach**: Because every scikit-learn classifier shares the same interface, you can put eight of them in a list and train them all in one `for` loop. This is the quickest way to find a good model for a new dataset.
- **Do**:
  1. Open `examples/14-classify-compare.py`. Put the eight classifier names and objects in two lists, split iris 50/50, loop: fit, score, print the accuracy of each.
  2. **Exercise 3.10** — Open `exercises/ex-3-10-compare-diabetes.py`. Same loop on `load_diabetes()`. Same continuous-target caveat as Exercise 3.9: swap in the regressor versions and compare R² scores instead.
- **Expected**: One accuracy line per classifier; most are above 90 % on iris.
- **Tell me when done**: reply with `step 9 done`.

### Step 10 — Regression: line, polynomial, curve fit, and Exercise 3.11 (Examples 3.15, 3.15a, 3.16, 3.17)

- **Teach**: Classification predicts a category; regression predicts a number. `scipy.stats.linregress` fits a straight line and returns its slope and intercept. Statsmodels does the same but prints a full statistical summary. `np.polyfit` fits a polynomial, and `scipy.optimize.curve_fit` fits any function you write (here an exponential decay).
- **Do**:
  1. Open `examples/15-linear-regression.py`. Fit a line to the x/y arrays with `linregress`, print slope and intercept, plot points and line.
  2. Open `examples/15a-linear-regression-statsmodels.py`. Fit the same data with `sm.OLS`, print the summary.
  3. Open `examples/16-polynomial-regression.py`. Fit a degree-3 polynomial with `np.poly1d(np.polyfit(...))`, plot it.
  4. Open `examples/17-least-squares.py`. Define `func(x, a, b, c)` for `a * exp(-b x) + c`, fit with `curve_fit`, print the best-fit parameters.
  5. **Exercise 3.11** — Open `exercises/ex-3-11-linreg-more-points.py`. Example 3.15 with more points, plus axis labels, title, legend, and grid.
- **Expected**: Four plots with fitted curves through the data; slope close to 0.9 in Example 3.15.
- **Tell me when done**: reply with `step 10 done`.

### Step 11 — Multiple linear and logistic regression, and Exercise 3.12 (Examples 3.18, 3.19)

- **Teach**: Multiple linear regression predicts one number from several inputs, so `x` becomes 2-D while `y` stays 1-D. Logistic regression, despite its name, is a classifier: it squashes a linear function through a sigmoid to output a probability between 0 and 1.
- **Do**:
  1. Open `examples/18-multiple-linear-regression.py`. Build a 2-D `x` and 1-D `y`, fit `LinearRegression`, print R², intercept, and coefficients.
  2. Open `examples/19-logistic-regression.py`. Build `X`, `y`, fit `LogisticRegression`, predict a sample.
  3. **Exercise 3.12** — Open `exercises/ex-3-12-linnerud-regression.py`. Multiple linear regression on `load_linnerud()`.
- **Expected**: R² and coefficients print; a predicted class prints.
- **Tell me when done**: reply with `step 11 done`.

### Step 12 — K-means and semi-supervised learning, and Exercises 3.13, 3.14, 3.15 (Examples 3.20, 3.21)

- **Teach**: K-means is unsupervised: you give it points but no labels, and it finds K groups by moving K centers until they settle. Semi-supervised learning sits in between: only a few points carry labels (the rest are `-1`), and `LabelSpreading` spreads those labels to their unlabeled neighbors.
- **Do**:
  1. Open `examples/20-kmeans.py`. Build two groups of points, fit `KMeans(n_clusters=2)`, print labels and centers, predict a new point.
  2. Open `examples/21-semi-supervised.py`. Build the points, label only the first and last, fit `LabelSpreading`, print the spread labels.
  3. **Exercise 3.13** — Open `exercises/ex-3-13-kmeans-blobs.py`. Example 3.20 with data from `make_blobs()`.
  4. **Exercise 3.14** — Open `exercises/ex-3-14-semi-more-points.py`. Sketch the points on paper, add two more per group, update the program.
  5. **Exercise 3.15** — Open `exercises/ex-3-15-semi-three-groups.py`. Add a third group, with exactly one labeled point per group.
  - Note: the book says Exercises 3.14 and 3.15 modify Example 3.20, but they come right after Example 3.21 and talk about labeled points, so build them on Example 3.21.
- **Expected**: Cluster labels and two centers print; every point ends up with a 0/1 (or 0/1/2) label.
- **Tell me when done**: reply with `step 12 done`.

### Step 13 — Reinforcement learning, and Exercise 3.16 (Examples 3.22, 3.23)

- **Teach**: In reinforcement learning an agent learns by trial and error from rewards. Q-learning fills a table of "how good is action A in state S" by exploring a graph many times; the best route is then read straight from the table. Example 3.23 lets a random agent play CartPole so you can see what an environment, an action, and a reward look like in code.
- **Do**:
  1. Open `examples/q_utils.py`. Write the helper functions (graph drawing with NetworkX, reward matrix, Q update). This file has no number prefix so `22-q-test.py` can import it: `from q_utils import *`.
  2. Open `examples/22-q-test.py`. Define the seven-node routing list and goal, train Q, print the best path from 0 to 6.
  3. Open `examples/23-gym-cartpole.py`. Run 20 CartPole episodes with random actions, using the Gymnasium API (see the modernization table).
  4. **Exercise 3.16** — Open `exercises/ex-3-16-q-routing-eight-states.py`. Design your own eight-node graph, solve it with Q-learning.
- **Expected**: A graph window, a Q-table, the shortest path `[0, 1, 3, 6]`; a CartPole window falling over repeatedly.
- **Tell me when done**: reply with `step 13 done`.

### Step 14 — Ensemble learning, and Exercise 3.17 (Examples 3.24, 3.25)

- **Teach**: Ensemble learning combines several models so their errors cancel out. `VotingClassifier` takes a vote between classifiers; `VotingRegressor` averages regressors. `cross_val_score` gives a fairer accuracy than a single train/test split by rotating which slice is held out.
- **Do**:
  1. Open `examples/24-ensemble-classifier.py`. Combine logistic regression, random forest, naive Bayes, and SVM in `VotingClassifier` on iris; print the cross-validated accuracy of each and of the ensemble.
  2. Open `examples/25-ensemble-regressor.py`. Combine gradient boosting, random forest, linear regression, and MLP in `VotingRegressor` on diabetes; plot each model's predictions.
  3. **Exercise 3.17** — Open `exercises/ex-3-17-ensemble-knn.py`. Add `KNeighborsClassifier` to Example 3.24.
- **Expected**: One accuracy line per model; the ensemble is about as good as the best single model. A plot of predictions.
- **Tell me when done**: reply with `step 14 done`.

### Step 15 — AutoML, PyCaret, LazyPredict, and Exercises 3.18–3.21 (Examples 3.26, 3.27, 3.28)

- **Teach**: AutoML tools try many models and settings for you and report a ranked table. They are great for a first look at a dataset and bad for understanding why a model works. See the modernization table: FLAML replaces `auto_ml`, and PyCaret/LazyPredict run on Google Colab.
- **Do**:
  1. Open `examples/26-automl.py`. Load `fetch_california_housing()`, split it, run FLAML's `AutoML().fit(..., task="regression", time_budget=60)`, print the best model and test R². This also covers **Exercise 3.18**, so `exercises/ex-3-18-automl-california.py` only needs a different time budget or metric.
  2. Open `examples/27-pycaret.py`. Type it here, then paste it into a Colab notebook (`!pip install pycaret` first). Set up classification on iris, compare all models.
  3. Open `examples/28-lazypredict.py`. Same: type it here, run on Colab (`!pip install lazypredict`). Parts a–e: install, classify iris, plot accuracies, regress California housing, plot R².
  4. **Exercises 3.19–3.21** — Open the matching `exercises/ex-3-19…`, `ex-3-20…`, `ex-3-21…` files: PyCaret on breast cancer, LazyPredict with another classification dataset, LazyPredict with another regression dataset.
- **Expected**: Each tool prints a ranked table of models.
- **Tell me when done**: reply with `step 15 done`.

### Step 16 — Chapter review and recap

- **Teach**: Section 3.12 has chapter review questions. Answering them in your own words consolidates the chapter. We also fill the **Recap** section at the bottom of this file with three takeaways.
- **Do**:
  1. Read section 3.11 (Summary).
  2. Open `notes.md`. Under **Chapter 3 review answers**, answer every review question in section 3.12 in one to three sentences each.
  3. Fill the **Recap** section below with three bullets.
  4. Update `docs/plan.md` row for Chapter 03 from `in-progress` to `done`.
- **Expected**: `notes.md` has answers, this file has a recap, the roadmap shows `done`.
- **Tell me when done**: reply with `step 16 done` — that closes the chapter.

## Exercises

The book embeds 21 exercises in Chapter 3. They are folded into the steps above so you do them in context:

| Exercise | Step | Builds on |
| -------- | ---- | --------- |
| 3.1, 3.2 | 3 | Examples 3.1, 3.2 |
| 3.3 | 4 | Example 3.4 |
| 3.4 | 5 | Example 3.6 |
| 3.5, 3.6 | 6 | Examples 3.7, 3.8 |
| 3.7 | 7 | Example 3.10 |
| 3.8, 3.9 | 8 | Examples 3.11, 3.12 |
| 3.10 | 9 | Example 3.14 |
| 3.11 | 10 | Example 3.15 |
| 3.12 | 11 | Example 3.18 |
| 3.13, 3.14, 3.15 | 12 | Examples 3.20, 3.21 |
| 3.16 | 13 | Example 3.22 |
| 3.17 | 14 | Example 3.24 |
| 3.18–3.21 | 15 | Examples 3.26, 3.27, 3.28 |

Each exercise file lives in `exercises/` (sibling of this README) with the naming pattern `ex-3-N-<short-name>.py`.

## Recap

Filled in at the end of the chapter. Three bullets, your three biggest takeaways:

- (key idea 1)
- (key idea 2)
- (key idea 3)

When the recap is written, all examples and exercises are typed, and Chapter 3 review answers are in `notes.md`, change the row in [`../../../docs/plan.md`](../../../docs/plan.md) for Chapter 03 from `in-progress` to `done`.
