from pydantic import BaseModel
from fastapi import FastAPI
from utils import generate_response, create_faiss_index, create_vectors, search

sections, model, vectors = create_vectors("data/no_sale_countries.md")

index = create_faiss_index(vectors)


class QueryRequest(BaseModel):
    """
    Represents a request model for a query.

    Attributes:
        query (str): The query to be processed.
    """

    query: str


app = FastAPI()


@app.post("/generate")
async def generate(request: QueryRequest) -> dict:
    """
    Generates a response to a query using the provided context.

    Args:
        request (QueryRequest): The request containing the query.

    Returns:
        dict: A dictionary containing the query, context, and response.
    """
    query = request.query

    # Retrieve relevant documents
    context = search(index, model, sections, query)
    context_text = "\n\n".join(context)

    response = generate_response(query, context_text)

    return {"query": query, "context": context, "response": response}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
