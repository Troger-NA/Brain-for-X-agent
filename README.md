# X Agent Brain 🧠🤖

A **modular AI brain** for an X (formerly Twitter) agent using **Cohere AI**. The system detects **sentiment**, processes **market data**, and generates **contextual responses**.

## 🚀 Features
- 🔍 **Emotion detection** (positive, neutral, negative)
- 📊 **Market-aware AI responses**
- 🤖 **Customizable prompts**
- 🔒 **Secure API key storage (via `.env`)**

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/x-agent-brain.git
cd x-agent-brain
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure API Keys
Create a .env file (copy .env.example and rename it to .env).
Add your API keys:

COHERE_API_KEY=your-cohere-api-key
### 4️⃣ Run the Brain
```bash
python brain/response_generator.py
```
## 📌 Customization
Modify prompts.py to change how the bot speaks.
Adjust sentiment_analysis.py to fine-tune emotion detection.
