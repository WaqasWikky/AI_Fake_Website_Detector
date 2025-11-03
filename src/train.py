import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from xgboost import XGBClassifier

# ==============================
# Configuration
# ==============================
DATA_PATH = 'D:/fake-website-detector/data/dataset_phishing.csv'
MODEL_DIR = 'D:/fake-website-detector/models'
MODEL_OUT = os.path.join(MODEL_DIR, 'xgb_phish.pkl')
ENCODER_OUT = os.path.join(MODEL_DIR, 'label_encoder.pkl')

# ==============================
# Load dataset
# ==============================
print("📂 Loading dataset...")
df = pd.read_csv(DATA_PATH)

print("✅ Dataset loaded with shape:", df.shape)
print("Columns:", df.columns.tolist()[:10], "...")

# Drop columns not needed
if 'url' in df.columns:
    df = df.drop(columns=['url'])

# Define X (features) and y (target)
y = df['status']
X = df.drop(columns=['status'])

# ==============================
# Encode target labels
# ==============================
print("\n🔢 Encoding labels...")
le = LabelEncoder()
y = le.fit_transform(y)  # 'legitimate' -> 0, 'phishing' -> 1
print("Unique encoded labels:", list(le.classes_))

# ==============================
# Split data
# ==============================
print("\n🔹 Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# ==============================
# Train Model
# ==============================
print("\n🤖 Training XGBoost model...")
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)
model.fit(X_train, y_train)

# ==============================
# Evaluate Model
# ==============================
print("\n📊 Evaluating model...")
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ==============================
# Save Model & Encoder
# ==============================
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(model, MODEL_OUT)
joblib.dump(le, ENCODER_OUT)
print(f"\n💾 Model saved to {MODEL_OUT}")
print(f"💾 Label encoder saved to {ENCODER_OUT}")

# ==============================
# Test a Random Sample
# ==============================
sample = X_test.sample(1)
prediction = model.predict(sample)
predicted_label = le.inverse_transform(prediction)[0]
print(f"\n🔍 Sample Prediction: {predicted_label}")

print("Training feature names:")
print(list(X_train.columns))
