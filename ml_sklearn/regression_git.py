import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# 1. Load data
# ============================================================
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv("data/melb_data.csv")

print("Dataset shape:", df.shape)
print(df.head())


# ============================================================
# 2. Feature / target selection
# ============================================================
target = 'Price'

features = [
    'Rooms',
    'Type',
    'Bedroom2',
    'Bathroom',
    'Car',
    'Landsize',
    'BuildingArea',
    'YearBuilt',
    'Lattitude',
    'Longtitude'
]

X = df[features]
y = df[target]


# ============================================================
# 3. Preprocessing (leakage-safe)
# ============================================================
numeric_features = [
    'Rooms', 'Bedroom2', 'Bathroom', 'Car',
    'Landsize', 'BuildingArea', 'YearBuilt',
    'Lattitude', 'Longtitude'
]

categorical_features = ['Type']

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
dt_model = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('model', DecisionTreeRegressor(max_leaf_nodes=500, random_state=0))
])

rf_model = Pipeline(steps=[
    ('preprocess', preprocessor),
    ('model', RandomForestRegressor(n_estimators=300, random_state=0))
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
def evaluate_regression(model, name):
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)

    mae = mean_absolute_error(y_valid, preds)
    rmse = mean_squared_error(y_valid, preds, squared=False)
    r2 = r2_score(y_valid, preds)

    print(f"\n{name}")
    print("-" * 40)
    print("MAE :", mae)
    print("RMSE:", rmse)
    print("R2  :", r2)


# ============================================================
# 7. Model evaluation
# ============================================================
evaluate_regression(dt_model, "Decision Tree Regressor")
evaluate_regression(rf_model, "Random Forest Regressor")


# ============================================================
# 8. Cross-validation (MAE)
# ============================================================
cv_scores = cross_val_score(
    rf_model,
    X,
    y,
    cv=5,
    scoring='neg_mean_absolute_error'
)

print("\nRandom Forest CV MAE:", -cv_scores.mean())
