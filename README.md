# Hybrid Log Message Classifier

This project classifies log messages into categories using a **hybrid approach** combining regex rules, supervised learning with embeddings, and a fallback LLM model (Groq API). It balances speed, accuracy, and flexibility.

---

## 🧩 How It Works

1. **Regex-based classification:**  
   Quickly attempts to classify logs using handcrafted regex patterns.

2. **Data length check:**  
   - If regex fails, the system checks if there's enough labeled data.  
   - If enough data is available, it uses a supervised learning model with log message embeddings for classification.  
   - If not enough data, it falls back to the Groq LLM model for classification.

---

## 🔍 Features

- Fast, interpretable regex classification for common log patterns.
- Supervised learning on embeddings when sufficient data is present for better accuracy.
- LLM fallback (Groq's DeepSeek LLaMA 70B) for rare/unseen patterns or small datasets.
- Modular design to easily add more categories, regex rules, or switch embedding models.

---

## 📦 Requirements

- Python 3.8+
- Libraries: `regex`, `scikit-learn` (for supervised model), `sentence-transformers` or `openai` (for embeddings), `groq` SDK
- Groq API key (if using fallback LLM)

---

## 🚀 Usage

### Setup

1. Install dependencies:

```bash
pip install groq python-dotenv scikit-learn sentence-transformers
