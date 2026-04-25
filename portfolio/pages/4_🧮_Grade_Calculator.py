import streamlit as st

st.set_page_config(page_title="Grade Calculator", page_icon="🧮", layout="wide")

st.title("🧮 Grade Calculator")

st.write("Use this simple calculator to estimate your final grade.")

quiz = st.number_input("Quiz Grade", min_value=0.0, max_value=100.0, value=85.0)
activity = st.number_input("Activity Grade", min_value=0.0, max_value=100.0, value=90.0)
exam = st.number_input("Exam Grade", min_value=0.0, max_value=100.0, value=88.0)

st.write("Grade Weights:")
st.write("Quiz: 30 percent")
st.write("Activity: 30 percent")
st.write("Exam: 40 percent")

if st.button("Compute Final Grade"):
    final_grade = (quiz * 0.30) + (activity * 0.30) + (exam * 0.40)

    st.subheader("Result")
    st.metric("Final Grade", round(final_grade, 2))

    if final_grade >= 75:
        st.success("Passed")
    else:
        st.error("Needs improvement")