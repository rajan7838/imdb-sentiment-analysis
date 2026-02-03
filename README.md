IMDB Movie Review Sentiment Analysis

RNN + TensorFlow + Streamlit

This project performs sentiment analysis on movie reviews using the IMDB dataset provided by Keras.
A Recurrent Neural Network (RNN) is trained to classify reviews as Positive or Negative, and the model is deployed using Streamlit for real-time predictions.

🚀 Features

Uses built-in IMDB dataset (tensorflow.keras.datasets.imdb)

Text preprocessing with padding

Embedding + SimpleRNN architecture

Binary sentiment prediction (Positive / Negative)

Interactive Streamlit web app

Interview-friendly & beginner-friendly code

🧠 Tech Stack

Python

TensorFlow / Keras

RNN (SimpleRNN)

Streamlit

📁 Project Structure
imdb_sentiment_app/
│
├── project.ipynb      # Train RNN model on IMDB dataset
├── app.py              # Streamlit web application
├── model.h5            # Trained model
├── requirements.txt    # Project dependencies
└── README.md

📊 Dataset

IMDB Movie Reviews Dataset

50,000 reviews (25k train, 25k test)

Labels:

1 → Positive

0 → Negative

Reviews are already converted into word indices

🏗️ Model Architecture
Embedding Layer
↓
SimpleRNN
↓
Dense (Sigmoid)


Embedding: Learns word semantics

RNN: Captures sequence context

Dense: Predicts sentiment

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Train the model
python train_model.py

3️⃣ Run Streamlit app
streamlit run app.py