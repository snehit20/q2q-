❓ Quora Duplicate Question Detection

This project builds a machine learning model to identify whether two questions from Quora are semantically duplicate or not.
Instead of relying only on deep learning, this approach focuses on strong feature engineering + classical ML, which is efficient, interpretable, and deployment-friendly.

📌 Problem Statement

Given two questions:

Are these two questions asking the same thing?

The model predicts:

1 → Duplicate questions

0 → Non-duplicate questions

🧠 Approach Overview

The pipeline follows these steps:

Data Cleaning & Sampling

Removed null values and duplicates

Randomly sampled 50,000 rows for faster experimentation

Feature Engineering (Core Strength of this Project)

Extracted multiple text similarity features

Combined them with Bag of Words (CountVectorizer)

Model Training

Trained a RandomForestClassifier

Evaluated using accuracy on a held-out test set

🧩 Feature Engineered Columns
1️⃣ Basic Text Similarity Features
Feature Name	Description
common_words_count	Number of common words between both questions
total_word_count	Total unique words in both questions
word_share	Ratio of common words to total words

These features capture surface-level overlap between questions.

2️⃣ Length-Based Features
Feature Name	Description
abs_len_diff	Absolute difference in number of words
mean_len	Average length of both questions
longest_substr_ratio	Length of the longest common substring normalized by question length

These help detect structural similarity between questions.

3️⃣ Token-Based Features (with Stopwords)
Feature Name	Description
q1_stopwords	Stopword count in Question 1
q2_stopwords	Stopword count in Question 2
common_stopwords	Common stopwords between questions
common_tokens	Common non-stopword tokens
token_ratio	Token overlap ratio

These features reduce noise and focus on meaningful tokens.

4️⃣ Fuzzy Matching Features

Powered by FuzzyWuzzy, these features capture approximate string similarity:

Feature Name	Description
fuzz_ratio	Overall similarity score
fuzz_partial_ratio	Partial match similarity
token_sort_ratio	Similarity after sorting tokens
token_set_ratio	Similarity based on unique token sets

These are especially useful when wording differs but intent is the same.

5️⃣ Bag of Words (CountVectorizer)

CountVectorizer(max_features=3000)

Applied to both questions

Converted text into numerical vectors

Concatenated with engineered features

This provides a statistical representation of language.

🤖 Model Used

Algorithm: Random Forest Classifier

Reason:

Handles non-linear feature interactions

Works well with mixed numerical features

Robust to noise

📊 Results

The model achieves strong accuracy using only:

Feature engineering

Classical ML

No deep learning

This makes it:

Fast to train

Easy to deploy

Easy to interpret

🛠️ Tech Stack

Python

Pandas, NumPy

NLTK

FuzzyWuzzy

Scikit-learn

Matplotlib / Seaborn (EDA)

🚀 Future Improvements

Replace BoW with TF-IDF

Try XGBoost / LightGBM

Add word embeddings (Word2Vec / GloVe)

Compare with Siamese Networks or BERT

📌 Key Takeaway

This project shows that good feature engineering can rival complex models.
It’s ideal for:

NLP fundamentals

Interview discussions

Internship-ready portfolios
