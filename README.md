# ChatPDF: A Local RAG System for Querying PDFs

[![Streamlit](https://img.shields.io/badge/Streamlit-v1.0-brightgreen)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-orange)](https://www.python.org/)

**ChatPDF** is a local **Retrieval-Augmented Generation (RAG)** system designed to query PDF documents. It combines a local vector database (**ChromaDB**) and a language model (**Ollama models like Vicuna**) to provide fast, accurate, and private answers based on document content.

## ✨ Features
- **Privacy-Focused**: All processing is done locally—no cloud dependency.
- **PDF Support**: Upload one or more PDF documents for querying.
- **Customizable**: Modify prompts to tailor the assistant’s behavior.
- **Interactive Interface**: User-friendly chat interface powered by **Streamlit**.
- **Expandable**: Easily add new documents or adjust the model.

---

## 📸 Demo
![Demo GIF](docs/demo.gif)
<img width="1440" alt="Screenshot 2025-01-22 at 14 32 34" src="https://github.com/user-attachments/assets/358cbd9e-ab95-4265-b470-2391e082a6dc" />


---

## 🛠 Installation

Follow these steps to set up and run the project:

### 1. Clone the Repository
```bash
git clone git@github.com:your-username/local-rag-chatpdf.git
cd local-rag-chatpdf

python3 -m venv rag_development
source rag_development/bin/activate  # On Windows: rag_development\Scripts\activate
```
 

### 2. Set Up a Virtual Environment
```bash
python3 -m venv rag_development
source rag_development/bin/activate  # On Windows: rag_development\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull the Language Model
```bash
ollama pull mistral
```

## 🚀 Usage
### 1. Start the Streamlit App

Run the following command to launch the application:
```bash
streamlit run app.py
```

### 2.  Interact with the Chat
Upload a PDF file via the interface.
Ask questions about the document's content.
View responses directly in the chat interface.