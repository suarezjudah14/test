import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

st.title("🏠 Home")
st.subheader("Hi, I am Judah Suarez I am a BSCS student.")

st.write("""
This portfolio app presents my background, learning progress, study routine,
and simple interactive tools that show my understanding of Streamlit.
""")

st.info("Explore the sidebar to view the other pages of this app.")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}! Welcome to my portfolio app.")