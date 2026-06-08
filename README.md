# AI Chatbot using Groq & Llama 3.1

An AI-powered chatbot built using Python, Streamlit, and the Groq API. The chatbot provides real-time conversational responses using the Llama 3.1 model and maintains chat history during the active session using Streamlit session state.

## Features

* Interactive chat interface built with Streamlit
* Powered by Llama 3.1 through the Groq API
* Session-based conversation memory
* Clean and user-friendly web interface
* Secure API key management using environment variables
* Lightweight and easy to deploy

## Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.1
* python-dotenv

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

## Future Improvements

* Persistent memory using SQLite or PostgreSQL
* User authentication
* Document upload and analysis
* RAG (Retrieval Augmented Generation)
* Vector database integration using ChromaDB
* Multi-agent workflows

## Learning Outcomes

Through this project I learned:

* LLM API integration
* Prompt engineering
* Session memory management
* Streamlit application development
* Environment variable management
* AI application deployment

## Author

Gowtham Reddy S

MSc Data Science | AI/ML Enthusiast | AI Automation Specialist
