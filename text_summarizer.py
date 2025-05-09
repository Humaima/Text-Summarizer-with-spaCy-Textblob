# Importing and loading libraries
import spacy 
from collections import defaultdict
from string import punctuation

# Defining function for spacy model
def install_spacy_model():
    """Helper function to download the required spaCy model if not present"""
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading spaCy English model...")
        from spacy.cli import download
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    return nlp

def summarize_text(text, num_sentences=3):
    """
    Summarizes a paragraph into the most important sentences.
    
    Args:
        text (str): The input text to summarize
        num_sentences (int): Number of sentences to include in summary
        
    Returns:
        str: The summarized text
    """
    # Load spaCy model
    nlp = install_spacy_model()
    
    # Process the text
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
    
    # Score sentences based on word frequencies
    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text.lower() in word_freq:
                if sent not in sentence_scores:
                    sentence_scores[sent] = word_freq[word.text.lower()]
                else:
                    sentence_scores[sent] += word_freq[word.text.lower()]
    
    # Select top sentences
    ranked_sentences = sorted(
        sentence_scores.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    # Get the top sentences
    summary_sentences = [sent[0].text for sent in ranked_sentences[:num_sentences]]
    
    # Join sentences to form summary
    summary = ' '.join(summary_sentences)
    
    return summary

# Test the function
if __name__ == "__main__":
    sample_text = """
    Natural language processing (NLP) is a subfield of linguistics, computer science, 
    and artificial intelligence concerned with the interactions between computers and 
    human language, in particular how to program computers to process and analyze 
    large amounts of natural language data. The goal is a computer capable of 
    "understanding" the contents of documents, including the contextual nuances of 
    the language within them. The technology can then accurately extract information 
    and insights contained in the documents as well as categorize and organize the 
    documents themselves. Challenges in natural language processing frequently involve 
    speech recognition, natural language understanding, and natural language generation.
    NLP has its roots in the 1950s. In 1950, Alan Turing published an article titled 
    "Computing Machinery and Intelligence" which proposed what is now called the Turing 
    test as a criterion of intelligence. The Georgetown experiment in 1954 involved fully 
    automatic translation of more than sixty Russian sentences into English. 
    The authors claimed that within three or five years, machine translation would be 
    a solved problem. However, real progress was much slower, and after the ALPAC report 
    in 1966, which found that ten-year-long research had failed to fulfill the expectations, 
    funding for machine translation was dramatically reduced. Little further research in 
    machine translation was conducted until the late 1980s.
    """
    
    print("Original Text:")
    print(sample_text)
    print("\nSummary:")
    print(summarize_text(sample_text))