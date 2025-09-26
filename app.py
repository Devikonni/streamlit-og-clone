<<<<<<< HEAD
=======
<<<<<<< HEAD
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
=======
>>>>>>> 4a65bdd (Add OG Clone UI components)
import streamlit as st

st.title("🚀 Streamlit OG Clone - Test App")
st.write("✅ Your Streamlit app is running successfully!")

st.write("This is just a test app. Once this works, we can add your OG Clone code here.")
<<<<<<< HEAD
=======
>>>>>>> 4635193 (Add OG Clone UI components)
>>>>>>> 4a65bdd (Add OG Clone UI components)
