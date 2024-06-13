# langchain-chatbot

# Chatbot Project

This project contains two applications that create chatbots using different language models. The first application uses OpenAI's GPT-3.5-turbo model, and the second application uses a local Llama model.

## Files

- `app.py`: A chatbot application using the GPT-3.5-turbo model from OpenAI.
- `locallama.py`: A chatbot application using a local Llama model.

## Requirements

To install the necessary packages, use the following command:

```bash
pip install -r requirements.txt
```

### Manual Installation
For Ollama, you need to manually download and install the package. Follow these steps:

Download the Ollama package from ``https://www.ollama.com/download``.
Extract the contents of the package.
Follow the installation instructions provided in the package.

## Environment Variables
This project requires some environment variables to be set for API keys and tracing. Create a .env file in the root directory of your project and add the following variables:
```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```
Replace `your_openai_api_key` and `your_langchain_api_key` with your actual API keys.

## Usage

#### Running the GPT-3.5 Chatbot
To run the chatbot using the GPT-3.5-turbo model, execute the following command:

```
streamlit run app.py
```
This will start a Streamlit web application where you can ask questions and get responses from the GPT-3.5-turbo model.

#### Running the Local Llama Chatbot
To run the chatbot using the local Llama model, execute the following command:
```
streamlit run locallama.py
```
This will start a Streamlit web application where you can ask questions and get responses from the local Llama model.


