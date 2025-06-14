# -*- coding: utf-8 -*-
"""Emotion Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XyOPm7v-fPZlfqDrUrIadgi4cyYU9y0O

Emotion Classification Model

Import Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay

"""Load Dataset"""

df = pd.read_csv("/content/training.csv")

#Dimesion
df.shape

#Datatype of Each column
df.dtypes

print(df['label'].unique()) #Return array of unique values
print(df['label'].value_counts()) #To see how many samples belong to each class

"""Label Mapping (bcz Labels are nuemeric)"""

if df['label'].dtype != 'O':
  label_map = {
      0: 'sadness',
      1: 'happy',
      2: 'neutral',
      3: 'anger',
      4: 'fear',
      5: 'surprise'
  }
  df['label'] = df['label'].map(label_map)

df['label'].unique() #Unique values after mapping

"""Clean Labels"""

df['label'] = df['label'].astype(str).str.lower()

"""Distributions of Emotions"""

import seaborn as sns

plt.figure(figsize=(8,5))
sns.countplot(x = 'label', data=df, order= df['label'].value_counts().index, palette= 'magma')
plt.title("Emotion Distribution in Dataset")
plt.xlabel("Emotion")
plt.ylabel("Number of Samples")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Split The Dataset"""

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

"""TF-IDF Vectorizer"""

vectorizer = TfidfVectorizer(stop_words = 'english', max_features = 1000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

"""Train Model"""

model = MultinomialNB()
model.fit(X_train_vec, y_train)

"""Predict On Test Set"""

y_pred = model.predict(X_test_vec)

"""Accuracy"""

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")

"""Confusion Matrix"""

labels = sorted(df['label'].unique())
cm = confusion_matrix(y_test, y_pred, labels = labels)
disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = labels)
disp.plot(xticks_rotation = 45)
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

"""Predict Manually in Code"""

def test_emotion(sentence):
  vec = vectorizer.transform([sentence])
  prediction = model.predict(vec)[0]
  print(f"Sentence: {sentence}\nPredicted Emotion: {prediction}")

test_emotion("im feeling rather rotten so im not very ambitious right now")

test_emotion("i feel a little mellow today")

test_emotion("i find myself in the odd position of feeling supportive of")

test_emotion("i feel just bcoz a fight we get mad to each other n u wanna make a publicity n let the world knows about our fight")

test_emotion("i cant walk into a shop anywhere where i do not feel uncomfortable")

test_emotion("i have seen heard and read over the past couple of days i am left feeling impressed by more than a few companies")

"""Predict: UI Based Using Gradio"""

import gradio as gr

def predict_emotion(text):
  vec = vectorizer.transform([text])
  pred = model.predict(vec)[0]
  return f"Predicted Emotion: {pred}"


gr.Interface(
    fn = predict_emotion,
    inputs = "text",
    outputs = "text",
    title = "Emotion Detector",
    description = "Enter a sentence and it will predict the emotion"
).launch(share=True)

