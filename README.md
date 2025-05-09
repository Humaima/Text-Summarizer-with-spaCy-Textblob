## 📝 Text Summarizer with spaCy & Textblob

![text-summarizer-logo](https://github.com/user-attachments/assets/312d6674-a279-40c5-bc9a-0d7c87811b48)

A web application that summarizes large paragraphs into concise sentences using NLP techniques powered by spaCy & Textblob and presented through an intuitive Streamlit interface.

![image](https://github.com/user-attachments/assets/60f42379-25c3-4c5e-b877-d36f38c723e7)

*Fig 1: Streamlit Interface for Text Summarizer*

![image](https://github.com/user-attachments/assets/1df50d1a-5ca2-44f4-97e9-a3082236084e)

*Fig 2: Text Summarizer Result*

## ✨ Features

- Extractive summarization - Identifies and extracts most important sentences
- Adjustable summary length - Control how many sentences to include
- Performance metrics - Shows word count reduction statistics
- Side-by-side comparison - View original text alongside summary
- Responsive design - Works on desktop and mobile devices

## 🚀 Quick Start

# Prerequisites

- Python 3.7+
- pip package manager

# Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
3. Run the Streamlit app:
   ```bash
   streamlit run app.py

## 🛠️ How It Works

The summarization algorithm:
1. Processes input text using spaCy's NLP pipeline
2. Removes stop words and punctuation
3. Calculates word frequencies
4. Scores sentences based on important word occurrences
5. Selects top-ranked sentences to form the summary

## 🌟 Example Usage

Try this sample text in the app:
```bash
"Climate change is one of the most pressing issues facing humanity today. The Earth's average temperature has risen by approximately 1.2 degrees Celsius since the late 19th century, primarily due to human activities like burning fossil fuels and deforestation. This warming has led to more frequent and intense extreme weather events..."
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See LICENSE for more information.

## 🙏 Acknowledgments

- spaCy for the NLP capabilities
- Streamlit for the web framework
- All contributors and open source maintainers
