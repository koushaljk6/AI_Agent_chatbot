# AI_Agent_chatbot
This project is an AI chatbot application with a Streamlit frontend and a FastAPI backend, integrating Groq and OpenAI language models. It features dynamic system prompts, live web search, and LangGraph's REACT architecture for intelligent and interactive user experiences.

---

## Features

### Frontend (Streamlit)
- User-friendly interface for defining:
  - System prompts (persona definitions).
  - Model selection (Groq or OpenAI).
  - Query input for chatbot interaction.
  - Web search toggle for live data retrieval.

### Backend (FastAPI)
- Handles API requests from the frontend.
- Validates user input with **Pydantic** schemas.
- Dynamically selects and interacts with LLMs to generate responses.

### AI Agent Logic
- Uses **LangGraph's REACT architecture** for contextual and stateful AI interactions.
- Incorporates **TavilySearchResults** for optional live internet searches.

---
# Running the Project

To get started, you'll need two separate terminals: one for the backend and one for the Streamlit frontend.

---

## Setup and Execution

Follow these steps to launch the application:

1.  **Activate the virtual environment** in *both* of your terminals:

    ```sh
    pipenv shell
    ```

2.  In the **first terminal**, start the backend server:

    ```sh
    python backend.py
    ```

3.  In the **second terminal**, run the Streamlit frontend:

    ```sh
    streamlit run frontend.py
    ```

After completing these steps, the application will launch and automatically open in your web browser.

---

## Requirements

To run this project, you need API keys from the following platforms (all free):
1. **Groq**: Access Groq's LLM models.
2. **OpenAI**: Access OpenAI's LLM models.
3. **Tavily**: Enable live web search.

### Setting Up API Keys
1. Sign up on each platform and obtain your API keys.
2. Create a `.env` file in the root directory of your project and add the keys:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here

# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
2. [Running the application](#project-phases-and-python-commands)


## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

# Project Phases and Python Commands

## Phase 1: Create AI Agent
```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI
```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit
```
python frontend.py
```

## IMPORTANT
### Make sure backend python script is running in a separate terminal




