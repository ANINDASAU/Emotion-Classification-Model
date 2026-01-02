import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load('models/emotion_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Streamlit Page Config
st.set_page_config(page_title="Emotion Detector", page_icon="🎭")

st.title("🎭 Emotion Classification Tool")
st.markdown("Enter a sentence below to see what emotion it conveys.")

# User Input
user_input = st.text_area("How are you feeling?", placeholder="e.g. I am feeling very optimistic about the future...")

if st.button("Analyze Emotion"):
    if user_input.strip():
        # 1. Transform input
        vec_input = vectorizer.transform([user_input])
        # 2. Predict
        prediction = model.predict(vec_input)[0]
        
        # 3. Display Result
        st.success(f"Detected Emotion: **{prediction.upper()}**")
        
        # Add a visual touch
        emoji_map = {"happy": "😊", "sadness": "😢", "anger": "😡", "fear": "😨", "surprise": "😮", "neutral": "😐"}
        st.subheader(f"Mood Score: {emoji_map.get(prediction, '✨')}")
    else:
        st.warning("Please enter some text first.")