import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from src.detector import ThreatProcessor
import joblib
import os

def generate_mock_data():
    """Generates synthetic network logs for immediate execution."""
    np.random.seed(42)
    data_size = 1000
    data = {
        'duration': np.random.rand(data_size),
        'protocol_type': np.random.choice(['tcp', 'udp', 'icmp'], data_size),
        'service': np.random.choice(['http', 'smtp', 'ftp'], data_size),
        'src_bytes': np.random.randint(0, 5000, data_size),
        'dst_bytes': np.random.randint(0, 5000, data_size),
        'failed_logins': np.random.choice([0, 1, 2, 3], data_size, p=[0.9, 0.05, 0.03, 0.02]),
        'label': np.random.choice(['normal', 'anomaly'], data_size, p=[0.7, 0.3])
    }
    return pd.DataFrame(data)

def main():
    os.makedirs('models', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)

    # 1. Load Data
    print("📥 Loading Network Traffic Data...")
    df = generate_mock_data()
    
    # 2. Preprocess
    processor = ThreatProcessor()
    X, y = processor.preprocess(df)
    
    # 3. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train Model
    print("🧠 Training AI Threat Detector (Random Forest)...")
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # 5. Evaluate
    y_pred = model.predict(X_test)
    print("\n✅ Detection Report:")
    print(classification_report(y_test, y_pred))
    
    # 6. Save Model
    joblib.dump(model, 'models/threat_model.pkl')
    
    # 7. Visualize Result
    plt.figure(figsize=(8,6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Reds')
    plt.title('Cybersecurity Threat Detection: Confusion Matrix')
    plt.ylabel('Actual State')
    plt.xlabel('AI Prediction')
    plt.savefig('outputs/metrics.png')
    print("📊 Metrics saved to outputs/metrics.png")

if __name__ == "__main__":
    main()