# 🎭 Emotion Detection App

An interactive **Machine Learning web application** that predicts the emotional tone of text input.  
Built using **Natural Language Processing (NLP)** and a **Multinomial Naive Bayes** classifier.

---

## 🚀 Features

- **Real-time Prediction:** Get instant emotion labels for any English sentence  
- **NLP Pipeline:** Uses TF-IDF Vectorization for text processing  
- **Clean UI:** Simple and intuitive interface built with Streamlit  
- **Multiclass Classification:** Detects 6 emotions:
  - Sadness  
  - Joy  
  - Love  
  - Anger  
  - Fear  
  - Surprise  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **ML Libraries:** Scikit-Learn, Pandas, NumPy  
- **UI Framework:** Streamlit  
- **Model Persistence:** Joblib  

---

## 📁 Project Structure
```text
├── models/             # Trained .pkl files (Model & Vectorizer)
├── app.py              # Streamlit Web Application
├── train.py            # Model training & Export logic
├── training.csv        # Dataset
├── requirements.txt    # Library dependencies
└── .gitignore          # Files to exclude from Git

```
---
## ⚙️ Installation & Setup
## 1️⃣ Clone the Repository

- git clone https://github.com/ANINDASAU/Emotion-Classification-Model.git

## 2️⃣ Create a Virtual Environment
- python -m venv myvenv
- Activate the environment:
*Windows:*
- myvenv\Scripts\activate
*Mac / Linux:*
- source myvenv/bin/activate
## 3️⃣ Install Dependencies
- pip install -r requirements.txt
## 4️⃣ Train the Model (Optional)
- Only required if you want to regenerate the .pkl model files.
- python train.py
- 
## 5️⃣ Run the Application

- streamlit run app.py

---
## 📊 Dataset & Model Performance
- The model utilizes the Multinomial Naive Bayes algorithm for classification.
- Text Preprocessing
- Vectorization: TF-IDF Vectorizer
- Stop-word removal: Included
- Feature Limit: Maximum 1,000 features

# Performance
- Accuracy: ~85% (May vary depending on the dataset and training configuration)

## ✅ Output
- The application predicts the emotional category of user-entered text in real-time via a clean, interactive Streamlit web interface.
