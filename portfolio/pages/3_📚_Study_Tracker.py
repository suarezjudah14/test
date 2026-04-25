import streamlit as st
import pandas as pd

st.set_page_config(page_title="Study Tracker", page_icon="📚", layout="wide")

st.title("📚 Study Tracker")

st.write("This page helps track study time for different subjects.")

subject = st.selectbox(
    "Choose a subject",
    ["Programming", "Database Management", "Networking", "Web Development", "Other"]
)

hours = st.slider("How many hours did you study today?", 0, 10, 2)

if st.button("Save Study Record"):
    st.success(f"You studied {subject} for {hours} hour/s today.")

st.subheader("Sample Weekly Study Plan")

data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Subject": ["Programming", "Database", "Networking", "Web Development", "Review"],
    "Target Hours": [2, 2, 1, 2, 3]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

total_hours = sum(data["Target Hours"])
st.metric("Total Weekly Target Study Hours", total_hours)

if hours >= 3:
    st.balloons()
    st.success("Great study effort today!")
else:
    st.info("Keep going. Small progress still matters.")