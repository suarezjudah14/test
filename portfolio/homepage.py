import streamlit as st

st.set_page_config(
    page_title="Student Productivity Portfolio",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Productivity Portfolio")
st.write("Welcome to my multipage Streamlit web application.")

st.markdown("""
This app shows my profile, skills, study habits, grade calculator, and contact form.

Use the sidebar to open each page:
- Home
- Profile
- Study Tracker
- Grade Calculator
- Contact
""")

st.info("This project is built using Python and Streamlit.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Pages", "5")

with col2:
    st.metric("Framework", "Streamlit")

with col3:
    st.metric("Project Type", "Portfolio App")

st.success("Ready for GitHub and Streamlit Community Cloud deployment.")