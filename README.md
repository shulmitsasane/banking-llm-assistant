# Banking LLM Assistant

## Project Overview

This project is an LLM-powered banking support assistant designed to answer banking-related questions using a Retrieval-Augmented Generation (RAG) approach.

The user interacts with a React frontend. The question is sent to a FastAPI backend, where relevant banking information is retrieved and passed to an LLM. The LLM then generates an answer based on the retrieved information.

## Project Goal

The goal of the project is to demonstrate how Large Language Models can be integrated with banking software systems to help employees quickly find information related to banking processes, policies, error codes, and operational procedures.

## Example Questions

- Why did a fund transfer fail?
- What documents are required for KYC?
- What is the process for premature fixed deposit closure?
- What does a particular banking error code mean?
- What information is required for a loan application?

## Technology Stack

### Frontend
- React.js
- JavaScript

### Backend
- Python
- FastAPI

### AI / LLM
- Large Language Model
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector similarity search

## Project Architecture

User
↓
React Frontend
↓
FastAPI Backend
↓
Retrieve Relevant Banking Information
↓
Send Context + User Question to LLM
↓
Generate Answer
↓
Return Answer to React Frontend

## What is RAG?

RAG stands for Retrieval-Augmented Generation.

Instead of directly asking the LLM to answer a question, the system first retrieves relevant information from a knowledge base.

The retrieved information is then provided to the LLM as context.

This helps make answers more relevant and reduces hallucination.

## Main Features

- Banking question-answering interface
- Retrieval of relevant banking information
- LLM-generated answers
- Answers grounded in provided banking documents
- Source references
- Handling of questions that are not covered by the available information

## Project Structure

```text
banking-llm-assistant/
│
├── README.md
├── backend/
│
└── frontend/

## Learning Objectives

Through this project, I am learning:
- React.js frontend development
- FastAPI backend development
- REST API communication
- LLM integration
- RAG architecture
- Embeddings and vector search
- Prompt engineering
- Full-stack application development

## Backend Setup

The backend of this project is built using Python and FastAPI.

### Virtual Environment

A Python virtual environment is used to keep project dependencies separate from the global Python installation.

Create a virtual environment inside the backend folder:

```bash
py -m venv venv

Activate the virtual environment in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1

Install Backend Dependencies
Install FastAPI and Uvicorn:
pip install fastapi uvicorn

- FastAPI is used to create the backend API.
- Uvicorn is used to run the FastAPI application.
Run the Backend
From inside the backend folder, run:
uvicorn main:app --reload

The backend runs at:
http://127.0.0.1:8000

FastAPI also provides interactive API documentation at:
http://127.0.0.1:8000/docs

Current API Endpoints
GET /
This endpoint checks whether the backend is running.
Example response:
{
  "message": "Banking LLM Assistant backend is running"
}

POST /ask
This endpoint receives a banking-related question.
Example request:
{
  "question": "Why did my fund transfer fail?"
}

Current example response:
{
  "question": "Why did my fund transfer fail?",
  "answer": "This is a temporary test answer."
}

At this stage, the endpoint returns a temporary response. Later, this endpoint will be connected to the RAG and LLM pipeline.
Banking Knowledge Base
The first prototype uses sample banking process documents created for learning and testing.
The current knowledge base covers:
- KYC and customer verification
- Fund transfer operations
- Fixed deposit operations
- Loan application and processing
The documents are stored inside:
backend/documents/

Current files:
kyc.txt
fund_transfer.txt
fixed_deposit.txt
loan.txt

The documents contain:
- Banking process descriptions
- Common issues
- Sample error codes
- Resolution guidance
- Escalation scenarios
These are sample documents created for the project and are not official bank policies.
In a production system, these could be replaced with approved internal banking manuals, operational procedures, FAQs, product documentation, and regulatory documents.
Current Project Flow
User Question
    ↓
React Frontend
    ↓
FastAPI Backend
    ↓
Retrieve Relevant Banking Information
    ↓
Send Retrieved Context + Question to LLM
    ↓
Generate Answer
    ↓
Return Answer to User

Current Development Stage
Completed:
- Project folder structure
- Python virtual environment
- FastAPI backend setup
- Basic backend health-check endpoint
- Banking question API endpoint
- Sample banking knowledge documents
Next steps:
- Load banking documents using Python
- Split documents into chunks
- Generate embeddings
- Store/search embeddings
- Retrieve relevant chunks
- Connect an LLM
- Build the RAG pipeline
- Build the React frontend
- Connect React to FastAPI
- Test the complete application

## Document Loading

The backend includes a Python document loader that automatically reads all `.txt` files stored in the `backend/documents/` folder.

For each document, the loader stores:

- Source file name
- Document text content

This allows the application to keep track of both the information and where that information came from.

Run the document loader using:

```bash
python document_loader.py

## Document Chunking

After loading the banking documents, the text is split into smaller sections called chunks.

Chunking is required because the RAG system should retrieve only the most relevant sections of a document rather than sending an entire document to the LLM.

The current prototype uses:

- Chunk size: 500 characters
- Chunk overlap: 100 characters

The overlap helps preserve context when information is split across two neighboring chunks.

Each chunk stores:

- Source document
- Chunk ID
- Chunk content

Example:

```text
Source: fund_transfer.txt
Chunk ID: 2
Content: ...

## Semantic Retrieval

After generating embeddings for the banking document chunks, the application can compare a user's question with the stored chunk embeddings.

The user question is also converted into an embedding.

Cosine similarity is used to measure how semantically similar the question is to each document chunk.

The chunks are ranked by similarity score, and the most relevant chunks are returned.

Current retrieval flow:

```text
User Question
      ↓
Question Embedding
      ↓
Compare with Chunk Embeddings
      ↓
Cosine Similarity
      ↓
Rank Results
      ↓
Return Top Relevant Chunks

The current prototype returns the top 3 most relevant chunks.
Run the retrieval test using:
python retriever.py

## Local LLM Setup

The project uses Ollama to run the Large Language Model locally.

This avoids the need for a paid external LLM API and allows the RAG pipeline to run on the local machine.

The current model is:

`llama3.1:8b`

Install Ollama and verify the installation:

```bash
ollama --version

## Local LLM Integration

The project uses Ollama to run `llama3.1:8b` locally.

The Python backend communicates with Ollama through its local API:

```text
http://localhost:11434

## Embedding Generation

The project uses Ollama to run the `nomic-embed-text` embedding model locally.

Each banking document chunk is converted into a numerical embedding vector.

The user's question is also converted into an embedding using the same model.

These vectors are compared using cosine similarity to identify the banking chunks that are most semantically relevant to the user's question.

Current flow:

text
Banking Documents
        ↓
Document Loading
        ↓
Chunking
        ↓
Ollama
        ↓
nomic-embed-text
        ↓
Embedding Generation

Using Ollama for embeddings avoids the need for an external embedding API and keeps the embedding process local.

## Semantic Retrieval

The application converts the user's question into an embedding using the same `nomic-embed-text` model used for the banking document chunks.

Cosine similarity is used to compare the question embedding against each chunk embedding.

The chunks are ranked by similarity score, and the top 3 most relevant chunks are returned.

Current retrieval flow:

```text
User Question
      ↓
Ollama
      ↓
nomic-embed-text
      ↓
Question Embedding
      ↓
Compare with Chunk Embeddings
      ↓
Cosine Similarity
      ↓
Top Relevant Chunks

## RAG API Testing

The complete RAG backend was tested using FastAPI's Swagger interface.

Example request:

```json
{
  "question": "What does FT102 mean?"
}
## Frontend Setup

The user interface is built using React.js.

Vite is used as the frontend development and build tool.

The React application is located inside:

```text
frontend/

## React Frontend Setup

The frontend is built using React and Vite.

The React development server runs locally at:

```text
http://localhost:5173

## Banking Assistant Interface

The React frontend contains:

- Banking question input
- Ask button
- Loading state
- Generated answer section
- Retrieved source documents

The frontend sends the user's question to the FastAPI `/ask` endpoint using an HTTP POST request.

## End-to-End Application Flow

The frontend and backend are now fully connected.

A user can enter a banking-related question in the React interface.

The question is sent to the FastAPI `/ask` endpoint.

The backend then:

1. Creates an embedding for the user question.
2. Compares it against the banking document chunk embeddings.
3. Retrieves the most relevant chunks.
4. Sends the retrieved context and user question to the local Llama 3.1 8B model through Ollama.
5. Returns the generated answer and source documents to the frontend.

The React frontend displays the answer and the source used.

Current flow:

```text
React Frontend
      ↓
FastAPI
      ↓
Question Embedding
      ↓
Semantic Retrieval
      ↓
Relevant Banking Chunks
      ↓
Ollama + Llama 3.1 8B
      ↓
Generated Answer + Sources
      ↓
React Frontend

## Retrieval Optimization

Document embeddings are generated once when the backend starts instead of being regenerated for every user question.

This improves response time because only the user's question needs to be embedded during each request.

Optimized flow:

```text
Backend Startup
      ↓
Generate Document Embeddings Once

User Question
      ↓
Generate Question Embedding
      ↓
Compare with Existing Document Embeddings
      ↓
Retrieve Relevant Chunks
      ↓
Generate LLM Answer

## RAG Testing

The application was tested using questions from multiple banking topics including:

- KYC
- Fund transfers
- Fixed deposits
- Loans

The system was also tested with unsupported and unrelated questions.

If the required information is not available in the retrieved banking context, the LLM is instructed to respond:

"I do not have enough information in the provided documents."

This helps reduce hallucination and keeps the generated answers grounded in the project knowledge base.

## Unsupported Question Handling

The application uses a minimum similarity threshold during retrieval.

If no banking document chunk is sufficiently relevant to the user's question, the system does not send unrelated context to the LLM.

Instead, it returns:

"I do not have enough information in the provided documents."

This helps reduce hallucination and keeps responses grounded in the banking knowledge base.