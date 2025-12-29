# 📄 PDF-RAG Chatbot – Talk to Your Documents

Upload any PDF and ask questions in plain English; the bot answers **only** from the document content using Google Gemini and retrieval-augmented generation (RAG).

---

## 🎯 Project Overview

| Feature | Description |
|---------|-------------|
| **Upload** | Uplaod PDF via browser |
| **Chunk & Embed** | Automatic text splitting + Sentence-Transformers vectors |
| **Vector Search** | FAISS for millisecond-similarity lookup |
| **Answer** | Google Gemini generates concise, grounded replies |
| **Stack** | FastAPI backend, HTML, Postgres|

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI (async Python) |
| LLM | Google Gemini (`gemini-2.5-flash`) |
| Embeddings | `all-MiniLM-L6-v2` (Sentence-Transformers) |
| Vector DB | FAISS (in-memory) |
| DB | PostgreSQL _(optional)_ / SQLite default |
| PDF Parser | PyPDF2 |
| UI | Single HTML file (`/static`) |

---

## 📸 Screenshot

<img width="1897" height="1017" alt="image" src="https://github.com/user-attachments/assets/db54ee47-0d7a-4f01-893f-858ce76f5c56" />


---

## ⚙️ 2-Minute Setup

### 1. Clone repo
```bash
git clone https://github.com/regmiaashish/chatbot-rag.git
cd chatbot-rag
```

### 2️. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️. Configure PostgreSQL Database

Open PostgreSQL and create a database:
   ```sql
   CREATE DATABASE dbname;
   ```

## 3. Configure environment variables(Place key and database url in .env file)
### 1. Gemini key
```bash
GOOGLE_API_KEY=your_gemini_key
```
### 2. Database url
```bash
DATABASE_URL=postgresql://postgres:passowrd@localhost:5432/dbname
```

## 4. Run the Server
```bash
uvicorn main:app --reload
```

## 📬 Contact

**Author:** Aashish Regmi  
🔗 GitHub: [@regmiaashish](https://github.com/regmiaashish)

---
