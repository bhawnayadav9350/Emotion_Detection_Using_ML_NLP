import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords
try:
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Load saved files
vectorizer = pickle.load(open("bow_vectorizer", "rb"))
model = pickle.load(open("lr_model.pkl", "rb"))

stop_words = set(stopwords.words('english'))

# Remove punctuation
def remove_punc(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))

# Remove numbers
def remove_num(txt):
    new = ""
    for i in txt:
        if not i.isdigit():
            new += i
    return new

# Remove emojis / non-ascii characters
def remove_emoji(txt):
    new = ""
    for i in txt:
        if i.isascii():
            new += i
    return new

# Remove stopwords
def remove_stopwords(txt):
    words = txt.split()
    cleaned = []

    for word in words:
        if word.lower() not in stop_words:
            cleaned.append(word)

    return " ".join(cleaned)

# Complete preprocessing pipeline
def preprocess_text(text):

    text = text.lower()

    text = remove_punc(text)

    text = remove_num(text)

    text = remove_emoji(text)

    text = remove_stopwords(text)

    return text


# Streamlit UI
st.title("Emotion Detection App")

user_input = st.text_area("Enter your sentence")

if st.button("Predict"):

    processed_text = preprocess_text(user_input)

    vector = vectorizer.transform([processed_text])

    prediction = model.predict(vector)[0]

    emotion_map = {
        0: "Sadness 😢",
        1: "Joy 😊",
        2: "Love ❤️",
        3: "Anger 😡",
        4: "Fear 😨",
        5: "Surprise 😲"
    }

    st.success(f"Predicted Emotion: {emotion_map[prediction]}")