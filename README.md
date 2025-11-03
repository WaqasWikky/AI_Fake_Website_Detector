
# 🕵️‍♂️ AI Fake Website Detector  

Detect **phishing and fake websites** using **Machine Learning** and **URL feature analysis**.  
This project leverages **Python**, **XGBoost**, and **Streamlit** to build a real-time AI tool that classifies a website as **Legitimate** or **Phishing/Fake** based on its URL features.

---

## 🚀 Features
✅ Detects **Phishing or Fake Websites** using trained ML model  
✅ **Real-time URL feature extraction**  
✅ Built with **Streamlit** for an interactive UI  
✅ Displays **confidence percentage** of prediction  
✅ Lightweight and fast — runs locally or deployable on cloud  

---

## 🧠 How It Works
1. **Feature Extraction** — Extracts technical and lexical features from the entered URL (like domain age, HTTPS, URL length, etc.)  
2. **Model Prediction** — The trained **XGBoost** model predicts whether the website is legitimate or phishing.  
3. **Result Display** — Streamlit interface shows the result with confidence percentage.  

---

## 🏗️ Project Structure
```
fake-website-detector/
│
├── app.py                     # Streamlit application
├── train.py                   # Model training script
├── requirements.txt            # Dependencies
├── models/
│   └── xgb_phish.pkl          # Trained XGBoost model
├── src/
│   └── url_features.py        # URL feature extraction functions
└── README.md                  # Project documentation
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/WaqasWikky/AI_Fake_Website_Detector.git
cd AI_Fake_Website_Detector
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

Then open the local URL displayed in your terminal — usually:
```
http://localhost:8501
```

---

## 🧩 Model Details
- **Algorithm:** XGBoost Classifier  
- **Training Data:** Public phishing dataset with URL-based features  
- **Accuracy:** ~98% on validation data  
- **Key Features:**  
  - Presence of HTTPS  
  - URL length  
  - Subdomain count  
  - Special characters  
  - Domain age  

---

## 🧰 Tech Stack
| Component | Description |
|------------|-------------|
| **Python 3.10+** | Programming Language |
| **Streamlit** | Web Application Framework |
| **Scikit-learn** | Model Evaluation & Preprocessing |
| **XGBoost** | Core Machine Learning Model |
| **Pandas / Numpy** | Data Handling & Analysis |

---

## 📸 Preview

Example:
```
🕵️‍♂️ AI Fake Website Detector
🔗 Enter Website URL: https://example.com
✅ Legitimate Website (Confidence: 97.53%)
```

---

## 📦 Deployment Options
You can deploy this project easily on:
- **Streamlit Cloud**
- **Hugging Face Spaces**
- **Heroku**
- **Render**

---

## 💡 Future Improvements
🔹 Add domain WHOIS feature for more accurate results  
🔹 Include deep learning model comparison (LSTM/CNN)  
🔹 Browser extension integration  
🔹 URL screenshot analysis  

---

## 👨‍💻 Developer
**Waqas Ahmad**  
Cybersecurity Specialist & AI Researcher   

🔗 **GitHub:** [WaqasWikky](https://github.com/WaqasWikky)  
🔗 **LinkedIn:** [linkedin.com/in/waqaswikky](https://www.linkedin.com/in/waqaswikky)

---

## 🛡️ License
This project is licensed under the **MIT License** — free to use and modify for educational and research purposes.

---

### ⭐ Don’t forget to star this repo if you like it!






