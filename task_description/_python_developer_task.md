# Simple RAG Application

## Objective
Develop a simple Retrieval-Augmented Generation (RAG) application that integrates a document
retrieval system with a large language model (LLM) to generate responses based on retrieved documents.

## Requirements
- Document Retrieval
  - Use a retrieval system (e.g., FAISS, Chroma DB) to find relevant documents based on user input.
  - use the attached no_sale_countries.md
- Language Model Integration
  - Use any available large language model (LLM), including self-hosted models, to generate
    responses by combining user input with retrieved documents.
  - You can use OpenAI API  
    - API KEY with some free credits will be provided to you
- API Endpoints
  - Create a FastAPI endpoint to receive user input, retrieve documents, and return generated responses.
- Documentation
  - Provide basic setup and usage instructions in the README file.

Deliverables
- Source Code
  - Python code in a GitHub repository.

## Evaluation Criteria
- Functionality: The application meets all specified requirements.
- Code Quality: The code is clean, organized, and self documented.
- User (developer) Experience: The API is intuitive and handles basic edge cases.