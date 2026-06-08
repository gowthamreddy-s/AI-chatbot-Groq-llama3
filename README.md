# AI Chatbot using Groq & Llama 3.1

An AI-powered chatbot built using Python, Streamlit, and the Groq API. The chatbot provides real-time conversational responses using the Llama 3.1 model and maintains chat history during the active session using Streamlit session state.Deployed using Streamlit Community Cloud.

## 🔗 Live Demo

https://ai-chatbot-groq-llama3-3whqfegzmnomjcjlzsq37i.streamlit.app

## Features

* Interactive chat interface built with Streamlit
* Powered by Llama 3.1 through the Groq API
* Session-based conversation memory
* Clean and user-friendly web interface
* Secure API key management using environment variables / Streamlit secrets
* Deployed on Streamlit Cloud

## 🧠 Architecture

The chatbot follows a simple client-server AI architecture:

* User interacts via Streamlit UI
* Input is processed in Python backend
* Conversation history is maintained using session_state
* Request is sent to Groq API (Llama 3.1 model)
* AI response is returned and displayed in UI

                ┌────────────────────────────┐
                │        USER (Browser)      │
                │  Types message in Streamlit│
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │      STREAMLIT UI          │
                │  (app.py frontend layer)   │
                │ - chat interface           │
                │ - session_state memory     │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │     PYTHON BACKEND         │
                │  chatbot logic (app.py)    │
                │ - prompt building          │
                │ - message history          │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │        GROQ API            │
                │   Llama 3.1 Model          │
                │ - understands prompt       │
                │ - generates response       │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │     RESPONSE RETURNS        │
                │  AI-generated answer        │
                └────────────┬───────────────┘
                             │
                             ▼
                ┌────────────────────────────┐
                │   STREAMLIT RENDERS UI     │
                │ shows assistant response   │
                └────────────────────────────┘

## Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.1
* python-dotenv

## 🌐 Deployment

Deployed using Streamlit Community Cloud.

Steps:
- Connected GitHub repository
- Configured GROQ_API_KEY in Streamlit Secrets
- Auto deployment enabled from main branch

## Project Structure

LLM-CHATBOT-SCRATCH/

├── venv/                # virtual environment (not uploaded)

├── .env                 # API key (not uploaded)

├── .gitignore           # ignores sensitive/local files

├── app.py               # main Streamlit chatbot app

├── chatbot.py           # chatbot logic

├── hello.py             # test file

├── README.md            # project documentation

└── requirements.txt     # project dependencies

## Installation

### Clone Repository

git clone <repository-url>

cd LLM-CHATBOT-SCRATCH

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Create .env File

GROQ_API_KEY=your_api_key_here

### Run Application

streamlit run app.py

## Deployment

* This application is deployed using Streamlit Community Cloud.

### Deployment Steps:

* Connected GitHub repository
* Configured Streamlit Secrets for secure API key storage
* Auto-deployment enabled from main branch
* Live app updates automatically on every GitHub push

## Future Improvements

* Persistent memory using SQLite or PostgreSQL
* User authentication system (login-based chatbot)
* Document upload and analysis
* RAG (Retrieval Augmented Generation)
* Vector database integration using ChromaDB or FAISS
* Multi-agent AI workflows

## Learning Outcomes

Through this project I learned:

* LLM API integration using Groq
* Prompt engineering and system design
* Session-based memory handling in Streamlit
* Building and deploying AI applications
* Secure API key management using environment  variables & secrets
* Full CI/CD flow using GitHub → Streamlit Cloud

## Author

Gowtham Reddy S

MSc Data Science | AI/ML Enthusiast | AI Automation Specialist
