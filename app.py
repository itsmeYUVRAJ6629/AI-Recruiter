import streamlit as st
from main import extract_information
st.title("AI RECRUITER-CV analyzer")
st.write(
    "Enter a candidate's experience, skills, or projects "
    "and the system will extract relevant information."
)
text = st.text_area(
    "Candidate Information",
    placeholder="Example: I have experience in Python, machine learning and TensorFlow..."
)

if st.button("Analyze Candidate"):

    if text.strip() == "":
        st.warning("Please enter some candidate information.")

    else:
        result = extract_information(text)

        st.subheader("Extracted Information")

        st.write("### 🧠 Skills")
        if result["skills"]:
            for skill in result["skills"]:
                st.write("•", skill)
        else:
            st.write("No skills detected.")

        st.write("### 🛠️ Technologies")
        if result["technologies"]:
            for technology in result["technologies"]:
                st.write("•", technology)
        else:
            st.write("No technologies detected.")

        st.write("### 💻 Languages")
        if result["languages"]:
            for language in result["languages"]:
                st.write("•", language)
        else:
            st.write("No languages detected.")

        st.subheader("JSON Output")
        st.json(result)