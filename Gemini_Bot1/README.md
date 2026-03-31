# Gemini Chatbot 🤵‍♂️

A simple conversational chatbot built with **Streamlit**, **LangChain**, and **Google Gemini** (via LangChain's Google GenAI integration).

## Features

- Chat interface powered by Streamlit
- Uses Google Gemini LLM via LangChain
- LangChain tracing enabled for observability

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/meetgc-304/chatbot.git
cd chatbot/chatBot1
```

### 2. Create a Virtual Environment

```bash
conda create -n chatbot_env python=3.10 -y
conda activate chatbot_env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your API keys:

```
LANGCHAIN_API_KEY="your_langchain_api_key"
GEMINI_API_KEY="your_gemini_api_key"
LANGCHAIN_PROJECT="chatbot_1_gemini"
```

- Get a **Gemini API key** at: https://aistudio.google.com/app/apikey
- Get a **LangChain API key** at: https://smith.langchain.com/

### 5. Run the App

```bash
streamlit run app.py
```

## Project Structure

```
chatbot/
├── chatBot1/
│   ├── app.py            # Main Streamlit chatbot app
│   ├── requirements.txt  # Python dependencies
├── requirements.txt      # Root-level requirements
└── .gitignore
```

## Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Google Gemini](https://deepmind.google/technologies/gemini/)
