# Log Message Classifier using LLM (Groq API)

This project classifies log messages into categories using a Large Language Model (LLM) via the Groq API. It's useful for automating the triage of system logs, alerts, and other operational messages.

## 🔍 Features

- Classifies log messages into:
  - `Workflow Error`
  - `Deprecation Warning`
  - `Unclassified` (fallback)
- Uses the **DeepSeek LLaMA 70B** model via Groq for fast inference.
- Easy to extend with more categories or export results.
- Written in simple, clean Python.

## 📦 Requirements

- Python 3.8+
- Groq API Key

### Install dependencies

```bash
pip install groq python-dotenv
