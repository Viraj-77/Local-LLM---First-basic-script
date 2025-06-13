# 🧠 Local LLM Prompt with LM Studio (Mistral 7B Instruct v0.2-GGUF)

This project demonstrates how to send a programmatic prompt to a **local LLM running via LM Studio** using Python, and get a response back.

## ✅ Requirements

- [LM Studio](https://lmstudio.ai) installed
- Mistral 7B Instruct v0.2-GGUF model downloaded and running in LM Studio
- Python 3.x
- `requests` library (`pip install requests`)

## 🚀 How to Run

1. **Start LM Studio**
   - Go to the "Models" tab and load **Mistral 7B Instruct v0.2-GGUF**
   - Go to "Settings" → "OpenAI-compatible API" and make sure the local server is **enabled**

2. **Run the script**

```bash
python first.py
