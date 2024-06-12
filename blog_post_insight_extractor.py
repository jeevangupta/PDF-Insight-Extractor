import os
import streamlit as st
from PyPDF2 import PdfReader
import openai
from dotenv import load_dotenv
load_dotenv()

st.set_page_config("Blog Post (PDF) Insights Extractor", page_icon=":memo:")

st.title("Blog Post PDF Insights Extractor")

key = os.environ.get("OPENAI_API_KEY")

openai.key = key
uploaded_file = st.file_uploader("Select a Resume PDF", type="pdf")

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Extracted PDF Contents")
    st.text_area("", value=text, height=300)


    with open("./blog_post_system_prompt.txt", "r") as f:
        system_prompt = f.read()

    main_prompt = "Here is an blog post: <blog_post>{}</blog_post>"

    if st.button("Extract Insights"):
        #st.subheader("Key")
        #st.text_area("", value=key, height=100)

        with st.spinner("Extracting Insights..."):
            response = openai.chat.completions.create(
                model="gpt-4-turbo-preview",
                max_tokens=1024,
                temperature=0.5,
                seed=456,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role":"user", "content": main_prompt.format(text)}
                ]
            )

            st.subheader("Extracted Insights")
            if response.choices:
                st.write(response.choices[0].message.content)


