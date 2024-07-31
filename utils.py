import faiss
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from typing import List, Tuple
import numpy as np


def generate_response(query: str, context: str) -> str:
    """
    Generates a response to a query based on the provided context using the OpenAI API.

    Args:
        query (str): The query to be answered.
        context (str): The context within which to search for the answer.

    Returns:
        str: The generated response from the AI model.
    """
    prompt = f"Instruction:\n{query}\n\nContext:\n{context}\n\nResponse:"

    client = OpenAI(api_key="your_api_key")  # Replace with your actual API key
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a professional chatbot that will answer questions based on the context provided "
                "to you. If you cannot find the answer in the content provided, please answer 'I am not "
                "sure how to answer this question'.",
            },
            {"role": "user", "content": prompt},
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].text.strip()


def create_vectors(
    file_path: str, model_name: str = "all-MiniLM-L6-v2"
) -> Tuple[List[str], SentenceTransformer, np.ndarray]:
    """
    Reads a document from a file, splits it into sections, and creates embeddings for each section using a transformer model.

    Args:
        file_path (str): The path to the document file.
        model_name (str): The name of the transformer model to use for embedding.

    Returns:
        tuple: A tuple containing:
            - sections (List[str]): The list of document sections.
            - model (SentenceTransformer): The transformer model used for embedding.
            - vectors (np.ndarray): The array of embeddings.
    """
    with open(file_path, "r") as file:
        document = file.read()

    sections = document.split("\n\n")

    model = SentenceTransformer(model_name)
    vectors = model.encode(sections)

    return sections, model, vectors


def create_faiss_index(vectors: np.ndarray) -> faiss.IndexFlatL2:
    """
    Creates a FAISS index from the given vectors.

    Args:
        vectors (np.ndarray): The array of vectors to be indexed.

    Returns:
        faiss.IndexFlatL2: The created FAISS index.
    """
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index


def search(
    index: faiss.IndexFlatL2,
    model: SentenceTransformer,
    sections: List[str],
    query: str,
    top_k: int = 3,
) -> List[str]:
    """
    Searches the FAISS index for the sections most relevant to the query.

    Args:
        index (faiss.IndexFlatL2): The FAISS index.
        model (SentenceTransformer): The transformer model used for embedding.
        sections (List[str]): The list of document sections.
        query (str): The query to search for.
        top_k (int): The number of top results to return.

    Returns:
        List[str]: The list of top-k sections most relevant to the query.
    """
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)
    return [sections[i] for i in indices[0]]
