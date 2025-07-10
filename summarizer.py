import streamlit as st
from utils.summarization import generate_summary

# App title and styling
st.set_page_config(page_title="BrevityAI", layout="centered")
st.title("📝 BrevityAI – AI Text Summarizer")
st.markdown("Summarize long articles, notes, or paragraphs in just one click!")

# Input text
input_text = st.text_area("Enter your text below:", height=300, placeholder="Paste your article, essay, or notes here...")

# Slider options for summary length
col1, col2 = st.columns(2)
with col1:
    min_len = st.slider("Minimum summary length", 30, 100, 30)
with col2:
    max_len = st.slider("Maximum summary length", 50, 300, 130)

# Summarize button
if st.button("✂️ Summarize"):
    with st.spinner("Generating summary..."):
        summary = generate_summary(input_text, max_length=max_len, min_length=min_len)
        st.subheader("🧾 Summary:")
        st.success(summary)

# Footer
st.markdown("---")
st.markdown("🔗 [GitHub Repo](https://github.com/your-username/BrevityAI) &nbsp;&nbsp;&nbsp; Built with ❤️ using Streamlit + Hugging Face")
