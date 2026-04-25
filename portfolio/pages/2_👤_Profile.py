import streamlit as st

st.set_page_config(page_title="Profile", page_icon="👤", layout="wide")

st.title("👤 Profile")

st.write("""
I am a student who wants to improve my skills in programming, design,
problem-solving, and web application development.
""")

st.subheader("Personal Information")

col1, col2 = st.columns(2)

with col1:
    st.write("Course: BS Computer Science")
    st.write("Interest: Web Development")
    st.write("Goal: Become a programmer and create useful applications")

with col2:
    st.write("Favorite Tool: VS Code")
    st.write("Learning Focus: Python and Streamlit")
    st.write("Project Style: Simple and useful systems")

st.subheader("My Learning Goals")

goals = [
    "Build clean and functional web applications",
    "Improve my Python programming skills",
    "Learn how to deploy projects online",
    "Create useful systems for students and communities"
]

for goal in goals:
    st.checkbox(goal)

st.warning("This page contain my personal information.")