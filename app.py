import streamlit as st
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load trained model
model = tf.keras.models.load_model("model.h5")

# Load IMDB word index
word_index = imdb.get_word_index()

# Encode user review
def encode_review(text):
    encoded = []
    for word in text.lower().split():
        encoded.append(word_index.get(word, 2))  # 2 = unknown word
    return encoded

st.title("🎬 IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict sentiment")

review = st.text_area("Movie Review")

if st.button("Predict Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review")
    else:
        encoded_review = encode_review(review)
        padded_review = pad_sequences([encoded_review], maxlen=200)

        prediction = model.predict(padded_review)[0][0]

        if prediction > 0.5:
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")