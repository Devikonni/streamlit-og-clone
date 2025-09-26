import streamlit as st
import pandas as pd

st.set_page_config(page_title="OG Clone", page_icon="🚀", layout="wide")

st.title("🚀 Streamlit OG Clone App")

st.write("Welcome! This is your OG Clone app.")

# Input example
username = st.text_input("Enter your username:")
if st.button("Submit"):
    st.success(f"Hello, {username}! This is a demo OG clone app.")

# Example table
data = {
    "Username": ["Alice", "Bob", "Charlie"],
    "Score": [90, 85, 78]
}
df = pd.DataFrame(data)
st.dataframe(df)
