import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from model.load_dataset import load_folder

# Load datasets
X_legit, y_legit = load_folder("legitimate", 0)
X_mal, y_mal = load_folder("malicious", 1)


X = X_legit + X_mal
y = y_legit + y_mal

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=150,
    max_depth=15,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
print(classification_report(y_test, model.predict(X_test)))

# Save model
with open("waf_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ ML WAF model trained and saved")
