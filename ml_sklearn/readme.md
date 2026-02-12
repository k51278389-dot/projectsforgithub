# Classical Machine Learning with scikit-learn

## Overview
This repository demonstrates **end-to-end classical machine learning workflows** using scikit-learn.
It focuses on **engineering-correct pipelines**, consistent preprocessing, and proper evaluation for both
regression and classification problems.

Rather than showcasing many algorithms, this project emphasizes **workflow design, data handling, and reproducibility**.

---

## Projects Included

### 1. Regression Pipeline – Melbourne Housing Prices
Predicts house prices using structured tabular data.

Key aspects:
- Supervised regression problem
- Train / validation split
- Feature selection and preprocessing
- Decision Tree and Random Forest regressors
- Evaluation using MAE, MSE, and R²
- Optional cross-validation

File:
- `regression_git.py`

Dataset:
- `melb_data.csv`

---

### 2. Classification Pipeline – Titanic Survival Prediction
Predicts passenger survival using demographic and travel features.

Key aspects:
- Binary classification problem
- Handling missing values
- Categorical encoding
- Decision Tree and Random Forest classifiers
- Pipeline + ColumnTransformer usage
- Evaluation using accuracy and classification metrics

File:
- `classifier_git.py`

Dataset:
- `Titanic-Dataset.xls`

---

## Key ML Concepts Demonstrated
- Regression vs classification workflows
- Train / validation splitting
- Feature preprocessing
- Handling missing values
- Categorical encoding
- Pipelines and ColumnTransformer
- Tree-based models
- Cross-validation
- Evaluation metrics

---

## Project Structure
```text
ml_sklearn/
│
├── regression_git.py
├── classifier_git.py
├── data/
│   ├── melb_data.csv
│   └── Titanic-Dataset.xls
├── README.md
└── requirements.txt
