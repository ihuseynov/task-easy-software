# Project Overview
This project is a FastAPI application that answers queries based on a provided document. It uses FAISS for efficient vector search and OpenAI's GPT-3.5-turbo for generating responses.

## Prerequisites
Python 3.11+ 
poetry

## Exploration of Tools
This has not been done much because of the limited time. Many other methods, pipeline structure can be explored to achive better results.

## Installation

1. Clone the Repository

``
git clone https://github.com/your-repository.git
cd your-repository
``
2.  Install Poetry

``
curl -sSL https://install.python-poetry.org | python3 -
``

3. Install Dependencies

````
poetry install
````

4. Configuration - OpenAI API Key

Update utils.py with your OpenAI API key:


````
client = OpenAI(api_key="your_api_key")
````



## Running the Application

#### Start the FastAPI Server

````
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
````

#### Make Requests

Example using curl:

````
curl -X POST "http://0.0.0.0:8000/generate" -H "Content-Type: application/json" -d '{"query": "Is Canada a no sale country?"}'
````

#### Expected response:

````
{
    "query": "Is Canada a no sale country?",
    "context": ["Section about Canada..."],
    "response": "Based on the provided context, Canada is a no sale country."
}
````

## Conclusion

This completes the basic setup and usage instructions for the project. For further details, refer to the source code and comments within the files.
