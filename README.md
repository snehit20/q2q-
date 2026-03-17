# ❓ Quora Duplicate Question Detection

A **Machine Learning–based Natural Language Processing (NLP) project** that identifies whether two questions asked on Quora are **semantically duplicate**.

This project emphasizes **strong feature engineering combined with classical machine learning**, making the solution **lightweight, interpretable, and deployment-friendly**.

---

# 1. 📌 Project Overview

On platforms like Quora, many users ask the **same question in different wording**. Detecting such duplicates helps:

• Improve search results
• Reduce redundant content
• Organize knowledge more effectively

This system predicts whether **two questions convey the same meaning**.

### Prediction Labels

• **1 → Duplicate Questions**
• **0 → Non-Duplicate Questions**

The model combines:

1. Hand-crafted text similarity features
2. Bag of Words vectorization
3. A **Random Forest classifier**

---

# 2. 🔁 Workflow

The overall machine learning pipeline consists of the following steps:

1. Data cleaning and preprocessing
2. Data sampling and preparation
3. Feature engineering
4. Text vectorization
5. Model training
6. Model evaluation and prediction

---

# 3. 🧩 Feature Engineering

The core strength of this project lies in **carefully engineered features** designed to capture **semantic and structural similarity** between question pairs.

The features are divided into four major groups.

---

# 4. 🔹 Word Overlap Features

These features measure **direct lexical similarity** between the two questions.

1. **common_words_count**
   Number of words that appear in both questions.

2. **total_word_count**
   Total unique words across both questions.

3. **word_share**
   Ratio of common words to total words.

These features capture how much vocabulary is shared between the questions.

---

# 5. 📏 Length-Based Features

These features capture **structural similarity** between question pairs.

1. **abs_len_diff**
   Absolute difference between lengths of the two questions.

2. **mean_len**
   Average length of both questions.

3. **longest_substr_ratio**
   Normalized length of the longest common substring.

These help detect cases where questions have similar structure but slightly different wording.

---

# 6. 🧠 Token-Based Features (Stopword Aware)

These features focus on **meaningful tokens while reducing noise from common stopwords**.

1. **q1_stopwords**
   Number of stopwords in Question 1.

2. **q2_stopwords**
   Number of stopwords in Question 2.

3. **common_stopwords**
   Number of shared stopwords.

4. **common_tokens**
   Number of shared non-stopword tokens.

5. **token_ratio**
   Ratio of shared tokens to total tokens.

This improves semantic comparison by emphasizing important words.

---

# 7. 🔍 Fuzzy Matching Features

Fuzzy matching allows **approximate string comparison**, capturing similarity beyond exact word matches.

The following metrics are used:

1. **fuzz_ratio**
2. **fuzz_partial_ratio**
3. **token_sort_ratio**
4. **token_set_ratio**

These features help detect duplicate questions even when **word order or phrasing differs**.

---

# 8. 🧾 Bag of Words Representation

To convert text into numerical format, the project uses **Bag of Words vectorization**.

### Configuration

CountVectorizer (max_features = 3000)

### Process

1. Vectorize Question 1 text
2. Vectorize Question 2 text
3. Combine vector features with engineered features
4. Create the final feature matrix

This hybrid approach combines **text representation with handcrafted similarity features**.

---

# 9. 🤖 Machine Learning Model

The project uses a **Random Forest Classifier**.

### Why Random Forest?

1. Handles **non-linear relationships between features**
2. Works well with **mixed feature types**
3. Robust against overfitting
4. Provides strong baseline performance

Random Forest is particularly effective when working with **feature-engineered datasets**.

---

# 10. 📊 Model Results

The model demonstrates strong classification performance using:

• Classical NLP techniques
• Extensive feature engineering
• No deep learning models

This makes the solution:

• **Fast**
• **Efficient**
• **Scalable**

---

# 11. 🛠️ Tech Stack

The following tools and libraries were used:

1. **Python**
2. **Pandas**
3. **NumPy**
4. **NLTK**
5. **FuzzyWuzzy**
6. **Scikit-learn**

---

# 12. 📁 Project Structure

Quora-Duplicate-Question-Detection
│
├── dataset.csv
├── quora_duplicate_detection.ipynb
│
├── README.md
│
└── requirements.txt

---

# 13. 🚀 Future Enhancements

Possible improvements for this project include:

1. Replace **Bag of Words with TF-IDF**
2. Experiment with **XGBoost or LightGBM**
3. Use **word embeddings (Word2Vec or GloVe)**
4. Implement **Siamese Neural Networks**
5. Compare results with **Transformer-based models such as BERT**

These improvements could increase the model's semantic understanding and prediction accuracy.

---

# 14. 🧠 Applications

Duplicate question detection can be used in:

• Question–Answer platforms (Quora, StackOverflow)
• Search engines
• Chatbots
• Knowledge base management systems

It helps improve **information retrieval and reduce redundant queries**.

---

# 15. 🏁 Conclusion

This project demonstrates that **strong feature engineering combined with classical machine learning** can achieve powerful results for NLP similarity tasks.

It serves as a **solid baseline approach** before moving to more complex deep learning architectures.

---

# 16. 👨‍💻 Author

**Snehit Singh**
B.Tech – Artificial Intelligence & Machine Learning

Interests:

• Machine Learning
• Natural Language Processing
• AI Systems
• Applied AI Research
