import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


# ============================================================
# 1. Load data
# ============================================================
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("data/titanic.csv")

print("Dataset shape:", df.shape)
print(df.head())


# ============================================================
# 2. Feature / target selection
# ============================================================
target = 'Survived'

features = [
    'Pclass',
    'Sex',
    'Age',
    'SibSp',
    'Parch',
    'Fare'
]

X = df[features]
y = df[target]


# ============================================================
# 3. Preprocessing
# ============================================================
numeric_features = ['Age', 'SibSp', 'Parch', 'Fare', 'Pclass']
categorical_features = ['Sex']

numeric_transformer = SimpleImputer(strategy='median')

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)


# ============================================================
# 4. Models
# ============================================================
dt_clf = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('model', DecisionTreeClassifier(max_leaf_nodes=50, random_state=0))
])

rf_clf = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('model', RandomForestClassifier(n_estimators=300, random_state=0))
])


# ============================================================
# 5. Train / validation split
# ============================================================
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, random_state=0
)


# ============================================================
# 6. Evaluation helper
# ============================================================
def evaluate_classifier(model, name):
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)

    print(f"\n{name}")
    print("-" * 40)
    print("Accuracy:", accuracy_score(y_valid, preds))
    print("\nClassification Report:")
    print(classification_report(y_valid, preds))


# ============================================================
# 7. Model evaluation
# ============================================================
evaluate_classifier(dt_clf, "Decision Tree Classifier")
evaluate_classifier(rf_clf, "Random Forest Classifier")


# ============================================================
# 8. Cross-validation
# ============================================================
cv_scores = cross_val_score(
    rf_clf,
    X,
    y,
    cv=5,
    scoring='accuracy'
)

print("\nRandom Forest CV Accuracy:", cv_scores.mean())
