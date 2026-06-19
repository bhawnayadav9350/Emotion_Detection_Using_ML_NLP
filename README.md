


# Emotion Detection Using NLP

## Project Overview

This project is a Machine Learning-based Emotion Detection System that classifies text into six different emotions: **Sadness, Anger, Love, Surprise, Fear, and Joy**. The application uses Natural Language Processing (NLP) techniques for text preprocessing and a Logistic Regression model for emotion classification. The model is deployed using Streamlit to provide an interactive web interface for users.

## Features

* Text preprocessing and cleaning
* Punctuation and number removal
* Stopword removal using NLTK
* Bag of Words (BoW) vectorization
* Multi-class emotion classification
* Interactive Streamlit web application
* Real-time emotion prediction

## Emotions Detected

| Label | Emotion     |
| ----- | ----------- |
| 0     | Sadness 😢  |
| 1     | Anger 😡    |
| 2     | Love ❤️     |
| 3     | Surprise 😲 |
| 4     | Fear 😨     |
| 5     | Joy 😊      |

## Technologies Used

* Python
* Natural Language Processing (NLP)
* Scikit-Learn
* NLTK
* Pandas
* NumPy
* Streamlit
* Pickle

## Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Text Cleaning
4. Bag of Words Vectorization
5. Train-Test Split
6. Logistic Regression Model Training
7. Model Evaluation
8. Model Deployment using Streamlit

## Project Structure

```text
Emotion-Detection-Using-NLP/
│
├── app.py
├── bow_vectorizer
├── lr_model.pkl
├── requirements.txt
├── README.md
└── Emotion_Detection.ipynb
```

## Installation

Clone the repository:

```bash
git clone https://github.com/bhawnayadav9350/Emotion_Detection_Using_ML_NLP.gitt
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## Sample Prediction

**Input:**

```text
I am feeling very happy today.
```

**Output:**

```text
Joy 😊
```

## Future Improvements

* TF-IDF Vectorization
* Support Vector Machine (SVM) Model
* Deep Learning Models (LSTM, GRU)
* Transformer-based Models (BERT)
* Emotion Probability Visualization
* Multi-language Support

## Author

**Bhawna Yadav**

Final Year B.Tech CSE Student | Data Science & Machine Learning Enthusiast

