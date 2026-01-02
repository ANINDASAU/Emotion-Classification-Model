import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Load Data
df = pd.read_csv("data/training.csv")

# 2. Label Mapping
label_map = {0: 'sadness', 1: 'happy', 2: 'neutral', 3: 'anger', 4: 'fear', 5: 'surprise'}
df['label'] = df['label'].map(label_map)

# 3. Vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 4. Train Model
model = MultinomialNB()
model.fit(X, y)

# 5. Export (Pickle)
joblib.dump(model, 'models/emotion_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')
print("Model and Vectorizer saved successfully in /models!")