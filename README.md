# 🤖 LexiAI

**LexiAI** is a private, multilingual AI assistant for working with documents locally — powered by open-source LLMs. Ask questions, summarize, and extract information from your files securely and offline.

---

## ✨ Features

- 🔐 Fully local & offline document processing  
- 🧠 LLM support via [Ollama](https://ollama.com/)  
- 📄 Ask questions based on uploaded PDFs, Word docs, etc.  
- 🌍 Auto-detects language and replies in the same one  
- 🧩 Supports multiple roles: Legal, HR, Tech, General  
- 💻 Desktop (PyQt) or Web (Blazor/.NET) frontend options  

---

## 📁 Folder Structure

```
LexiAI/
├── main.py
├── chat_engine/
│   └── model_wrapper.py
├── ui/
│   └── main_window.py
├── assets/
│   └── logo.png
├── .venv/                # Ignored by Git
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Saree159/LexiAI.git
   cd LexiAI
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python main.py
   ```

---

## 🧠 Models Used

- [LLaMA 3](https://ollama.com/library/llama3)  
- Gemma, Mistral, or any GGUF-compatible model  
- Running via Ollama backend or locally loaded  

---

## 🔧 Tech Stack

- Python  
- LangDetect  
- Ollama  
- PyQt / Blazor (.NET 8)  
- GitHub for version control  

---

## 📜 License

MIT License © 2025 Saree Ali

---

## 💡 Contributing

Pull requests welcome!  
For major changes, open an issue first to discuss what you’d like to change.

---

## 🧩 Future Ideas

- Web-based UI with chat history & themes  
- Local vector DB (e.g. Chroma) for retrieval-augmented generation (RAG)  
- User roles with custom prompt tuning  

---
