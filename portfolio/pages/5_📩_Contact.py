import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📩", layout="wide")

st.title("📩 Contact")

st.write("You can use this form as a sample contact section for your portfolio.")

name = st.text_input("Full Name")
email = st.text_input("Email Address")
reason = st.selectbox(
    "Reason for Contact",
    ["Project Inquiry", "School Activity", "Collaboration", "Other"]
)
message = st.text_area("Message")

if st.button("Submit Message"):
    if name and email and message:
        st.success("Your message has been submitted successfully.")
        st.write("Summary:")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Reason: {reason}")
        st.write(f"Message: {message}")
    else:
        st.error("Please complete all required fields.")

st.markdown("### Social Links")
st.write("GitHub: https://github.com/SuarezJudah14")
st.write("Facebook: https://www.facebook.com/judah.suarez.98")
st.write("Email: judahcababan@email.com")