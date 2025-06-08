import streamlit as st
import tempfile
import json
from extract3 import extract_info_from_pdf

st.set_page_config(page_title="Resume Skill Extractor", layout="wide")
st.title("AI Resume Skill Extractor")

st.markdown("Upload a PDF resume to extract key information like **name**, **email**, **skills**, **education**, and get a smart **summary**.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        path = tmp_file.name

    with st.spinner("Extracting information..."):
        extracted = extract_info_from_pdf(path)

    st.success("Extraction Complete!")

    st.subheader("Basic Info")
    st.write(f"**Name:** {extracted['Name']}")
    st.write(f"**Email:** {extracted['Email']}")
    st.write(f"**Phone:** {extracted['Phone']}")

    st.subheader("Education")
    st.text(extracted['Education Section'])

    st.subheader("Experience")
    st.text(extracted['Experience Section'])

    st.subheader("Skills")
    st.text(extracted['Skills Section'])

    st.subheader("Resume Summary")
    st.markdown(extracted['Full Resume Summary'])

    if st.button("Save as JSON"):
        with open("resume_result.json", "w") as f:
            json.dump(extracted, f, indent=4)
        st.success("Saved to `resume_result.json`")