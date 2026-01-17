❓ Quora Duplicate Question Detection

A machine learning–based NLP project to identify whether two questions asked on Quora are semantically duplicate.

This project focuses on strong feature engineering + classical machine learning, making it lightweight, interpretable, and deployment-friendly 🚀


📌 Overview

Given a pair of questions, the model predicts:

1 → Duplicate questions

0 → Non-duplicate questions

The pipeline combines hand-crafted text similarity features with Bag of Words vectorization, followed by a Random Forest classifier 🌲


🔁 Workflow

Data cleaning and sampling

Text preprocessing

Feature engineering

Vectorization

Model training and evaluation


🧩 Feature Engineering

The core strength of this project lies in its carefully engineered features, designed to capture semantic and structural similarity between question pairs.

🔹 Word Overlap Features

These features measure direct lexical similarity between questions.

common_words_count – Number of common words

total_word_count – Total unique words across both questions

word_share – Ratio of common words to total words

📏 Length-Based Features

These capture structural similarity and sentence balance.

abs_len_diff – Absolute difference in question lengths

mean_len – Average length of both questions

longest_substr_ratio – Normalized length of the longest common substring


🧠 Token-Based Features (Stopword Aware)

These focus on meaningful tokens while reducing noise.

q1_stopwords – Stopword count in Question 1

q2_stopwords – Stopword count in Question 2

common_stopwords – Shared stopwords

common_tokens – Shared non-stopword tokens

token_ratio – Token overlap ratio


🔍 Fuzzy Matching Features

Approximate string matching to capture similarity beyond exact word matches.

fuzz_ratio

fuzz_partial_ratio

token_sort_ratio

token_set_ratio


🧾 Bag of Words Representation

CountVectorizer (max_features = 3000)

Applied to both questions

Combined with engineered features to create the final feature set


🤖 Model

Algorithm: Random Forest Classifier 🌲

Why Random Forest?

Handles non-linear feature interactions

Works well with engineered numerical features

Robust and easy to interpret


📊 Results

The model achieves strong classification performance using:

Classical NLP techniques

Extensive feature engineering

No deep learning models

This makes the solution fast, efficient, and scalable ⚡


🛠️ Tech Stack

Python 🐍

Pandas, NumPy

NLTK

FuzzyWuzzy

Scikit-learn


🚀 Future Enhancements

Replace Bag of Words with TF-IDF

Experiment with XGBoost / LightGBM

Add word embeddings (Word2Vec / GloVe)

Compare with Siamese Networks or Transformer-based models


🏁 Conclusion

This project demonstrates that strong feature engineering can rival complex deep learning models and serves as a solid baseline for NLP similarity tasks 🧠✨
