# AI-Powered Cybersecurity Threat Detection 🛡️💻

An intelligent Intrusion Detection System (IDS) that utilizes machine learning to identify network anomalies and potential cyberattacks in real-time traffic logs.

## 🚀 Key Features
- **Supervised Anomaly Detection:** Leverages a Random Forest Classifier to distinguish between 'Normal' and 'Malicious' traffic.
- **SOC-Style Metrics:** Automatically generates a Confusion Matrix to visualize True Positives and False Alarms.
- **Automated Preprocessing:** Handles protocol encoding (TCP/UDP/ICMP) and feature scaling for raw network logs.
- **High Performance:** Achieved over 90% accuracy in detecting simulated brute-force and DoS patterns.

## 🛠️ Tech Stack
- **Language:** Python 3.10
- **Libraries:** Scikit-Learn, Pandas, NumPy, Seaborn (Visualization)
- **Algorithm:** Random Forest (Ensemble Learning)

## 📊 Performance Proof
- **Accuracy:** ~92%
- **Detection Result:** Check the `outputs/metrics.png` for the detailed Confusion Matrix.

## 📂 Project Structure
- `src/detector.py`: Core data preprocessing and normalization logic.
- `main.py`: Model training, evaluation, and visualization pipeline.
- `outputs/`: Performance heatmaps and threat logs.

<img width="600" height="600" alt="metrics" src="https://github.com/user-attachments/assets/9c68c164-bdfc-42eb-9b69-f528796adadf" />

