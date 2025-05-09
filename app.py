import streamlit as st
import spacy
from collections import defaultdict
from string import punctuation
from spacy.cli import download

# Set page config
st.set_page_config(
    page_title="Text Summarizer",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to ensure spaCy model is downloaded
def setup_spacy():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        st.warning("Downloading spaCy English model... (this may take a few minutes)")
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
        st.success("Model downloaded successfully!")
    return nlp

# Summarization function
def summarize_text(text, num_sentences=3):
    nlp = setup_spacy()
    doc = nlp(text)
    
    # Remove stop words and punctuation
    stop_words = spacy.lang.en.stop_words.STOP_WORDS
    words = [
        token.text.lower() 
        for token in doc 
        if token.text.lower() not in stop_words 
        and token.text not in punctuation
    ]
    
    # Calculate word frequencies
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    
    # Normalize frequencies
    max_freq = max(word_freq.values()) if word_freq else 1
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq
    
    # Score sentences
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word.text.lower()]
                else:
                    sentence_scores[sent] += word_freq[word.text.lower()]
    
    # Get top sentences
    ranked_sentences = sorted(
        sentence_scores.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    summary_sentences = [sent[0].text for sent in ranked_sentences[:num_sentences]]
    return ' '.join(summary_sentences)

# UI Components
def main():
    st.title("✂️ Text Summarizer")
    st.markdown("""
    Paste your text below and get a concise summary powered by spaCy.
    """)
    
    with st.sidebar:
        st.header("Settings")
        num_sentences = st.slider(
            "Number of sentences in summary",
            min_value=1,
            max_value=10,
            value=3
        )
        st.markdown("---")
        st.markdown("### How it works")
        st.markdown("""
        1. Paste your text in the box
        2. Adjust summary length with the slider
        3. Click 'Summarize' button
        """)
    
    # Text input area
    input_text = st.text_area(
        "Input Text",
        height=300,
        placeholder="Paste your text here..."
    )
    
    # Summarize button
    if st.button("Summarize"):
        if input_text.strip():
            with st.spinner("Generating summary..."):
                summary = summarize_text(input_text, num_sentences)
                
                st.subheader("Summary")
                st.write(summary)
                
                # Show stats
                col1, col2 = st.columns(2)
                original_words = len(input_text.split())
                summary_words = len(summary.split())
                
                with col1:
                    st.metric("Original Length", f"{original_words} words")
                with col2:
                    st.metric("Summary Length", f"{summary_words} words", 
                              delta=f"-{original_words - summary_words} words")
                
                st.markdown("---")
                st.subheader("Visual Comparison")
                st.text_area(
                    "Original Text (for comparison)",
                    input_text,
                    height=200,
                    disabled=True
                )
        else:
            st.warning("Please enter some text to summarize")

if __name__ == "__main__":
    main()