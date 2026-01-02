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

├── data/ # Dataset (training.csv)
├── models/ # Trained .pkl files (Model & Vectorizer)
├── app.py # Streamlit Web Application
├── train.py # Model training & export logic
├── requirements.txt # Project dependencies
└── .gitignore # Files excluded from Git

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv myvenv
Activate the environment

Windows

bash
Copy code
myvenv\Scripts\activate
Mac / Linux

bash
Copy code
source myvenv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Train the Model (Optional)
Only required if you want to regenerate the .pkl model files.

bash
Copy code
python train.py
5️⃣ Run the Application
bash
Copy code
streamlit run app.py
📊 Dataset & Model Performance
Algorithm: Multinomial Naive Bayes

Text Preprocessing:

TF-IDF Vectorizer

Stop-word removal

Maximum 1000 features

Accuracy: ~85%
(May vary depending on the dataset and training configuration)

✅ Output
The app predicts the emotional category of user-entered text in real time via a Streamlit web interface.