import textwrap, faiss, numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

class GeminiRAG:
    def __init__(self, full_text: str, chunk_size: int = 1000, overlap: int = 200):
        self.llm = genai.GenerativeModel("gemini-2.5-flash")
        self.embed = SentenceTransformer("all-MiniLM-L6-v2")

        chunks = self._chunk(full_text, chunk_size, overlap)
        self.texts = chunks
        embeddings = self.embed.encode(chunks, show_progress_bar=False).astype("float32")

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def _chunk(self, text, size, overlap):
        chunks, start = [], 0
        while start < len(text):
            end = start + size
            chunks.append(text[start:end])
            start = end - overlap
        return chunks

    def ask(self, question: str, k: int = 3) -> str:
        q_emb = self.embed.encode([question]).astype("float32")
        _, topix = self.index.search(q_emb, k)
        context = "\n\n".join(self.texts[i] for i in topix[0])

        prompt = textwrap.dedent(f"""\
        You are a helpful assistant.
        Use only the following context to answer the question.
        If the answer is not in the context, say "Sorry,for now I have no idea about that."

        Context:
        {context}

        Question: {question}
        Answer (be concise):\
        """)
        return self.llm.generate_content(prompt).text