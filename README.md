IMDB Movie Review Sentiment Analysis

RNN + TensorFlow + Streamlit

This project is about predicting whether a movie review is Positive or Negative using Deep Learning.
It uses the IMDB movie review dataset from Keras, trains a Recurrent Neural Network (RNN), and deploys the model using Streamlit so users can test it in real time.

🚀 What this project does

Takes a movie review as input

Understands the sequence of words

Predicts the sentiment:

😊 Positive

😞 Negative

✨ Features

Uses built-in IMDB dataset from Keras

Text preprocessing with padding

Embedding + SimpleRNN model

Binary sentiment classification

Interactive Streamlit web app

Easy to understand and interview-friendly

🧠 Technologies Used

Python

TensorFlow / Keras

Recurrent Neural Network (SimpleRNN)

Streamlit

📁 Project Structure
imdb_sentiment_app/
│
├── project.ipynb        # Model training on IMDB dataset
├── app.py               # Streamlit web application
├── model.h5             # Trained RNN model
├── requirements.txt     # Required libraries
├── README.md

📊 Dataset Information

IMDB Movie Reviews Dataset

Total 50,000 reviews

25,000 for training

25,000 for testing

Labels:

1 → Positive review

0 → Negative review

Reviews are already converted into numerical word indices

🏗️ Model Architecture (Simple)
Embedding Layer
↓
SimpleRNN
↓
Dense Layer (Sigmoid)

What each layer does

Embedding Layer
Converts word numbers into meaningful vectors

RNN Layer
Learns the order and context of words

Dense Layer
Predicts whether the review is positive or negative

▶️ How to Run the Project Locally
1️⃣ Install required libraries
pip install -r requirements.txt

2️⃣ Train the model
python train_model.py


(This step creates model.h5)

3️⃣ Run the Streamlit app
streamlit run app.py
