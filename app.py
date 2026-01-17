import streamlit as st
import pickle
import os
import gdown
import helper

# -------------------------------
# Model download configuration
# -------------------------------
MODEL_PATH = "model.pkl"

# Your Google Drive file ID from the link you gave
DRIVE_FILE_ID = "1-X7FthPLqoFi0nKQbd3SzwfHEQOFZzOZ"

MODEL_URL = f"https://drive.google.com/uc?id={DRIVE_FILE_ID}"

# Download model if not present
if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading model..."):
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

# Load model
model = pickle.load(open(MODEL_PATH, "rb"))

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Duplicate Question Detector")
st.header("Duplicate Question Pairs")

q1 = st.text_input("Enter question 1")
q2 = st.text_input("Enter question 2")

if st.button("Find"):
    if q1.strip() == "" or q2.strip() == "":
        st.warning("Please enter both questions")
    else:
        query = helper.query_point_creator(q1, q2)
        result = model.predict(query)[0]

        if result == 1:
            st.success("Duplicate")
        else:
            st.error("Not Duplicate")
