import streamlit as st
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# ---------------------------
# Firebase Initialization
# ---------------------------
if not firebase_admin._apps:
    # Make sure serviceAccountKey.json is in the same folder and added to .gitignore
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ---------------------------
# Streamlit App Configuration
# ---------------------------
st.set_page_config(page_title="OG Clone", page_icon="🚀", layout="wide")
st.title("🚀 Streamlit OG Clone with Firebase")

# ---------------------------
# User Input Section
# ---------------------------
st.header("User Input Form")
username = st.text_input("Enter your username:")
bio = st.text_area("Enter a short bio:")

if st.button("Save to Firebase"):
    if username and bio:
        try:
            doc_ref = db.collection("users").document(username)
            doc_ref.set({"username": username, "bio": bio})
            st.success(f"✅ Data saved for {username}!")
        except Exception as e:
            st.error(f"Error saving data: {e}")
    else:
        st.error("Please enter both username and bio.")

# ---------------------------
# Display Stored Users
# ---------------------------
st.header("Stored Users from Firebase")

try:
    users_ref = db.collection("users").stream()
    data = [{"username": doc.to_dict()["username"], "bio": doc.to_dict()["bio"]} for doc in users_ref]
    
    if data:
        st.dataframe(pd.DataFrame(data))
    else:
        st.info("No users stored yet.")
except Exception as e:
    st.error(f"Error fetching users: {e}")
