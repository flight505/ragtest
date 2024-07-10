# GraphRAG with Ollama - Install Local Models for RAG

## Introduction

GraphRAG (Knowledge Graph Retrieval-Augmented Generation) is a powerful tool for enhancing text generation by retrieving relevant information from a knowledge graph. This tutorial will guide you through setting up GraphRAG with Ollama models for RAG (Retrieval-Augmented Generation). By following this step-by-step guide, you'll learn how to configure your environment, download necessary models, and prepare your workspace.

## Installation and Setup

### Step 1: Create and Activate a Conda Environment

First, create and activate a Conda environment for your project:

```bash
conda create -n kgrag_ollama python=3.11 -y
conda activate kgrag_ollama
```

### Step 2: Install Required Packages

Next, install the required packages:

```bash
pip install ollama
ollama pull mistral
ollama pull nomic-embed-text
pip install graphrag
```

### Step 3: Prepare Your Workspace

Create the necessary directories and download a sample text (A Christmas Carol by Charles Dickens):

```bash
mkdir -p ./ragtest/input
curl https://www.gutenberg.org/cache/epub/24022/pg24022.txt > ./ragtest/input/book.txt
```

### Step 4: Initialize GraphRAG

Initialize your workspace by running the following command:

```bash
python -m graphrag.index --init --root ./ragtest
```

This command creates two files in the `./ragtest` directory:

- `.env`: Contains environment variables required to run the GraphRAG pipeline. Replace `<API_KEY>` with your OpenAI API key.
- `settings.yaml`: Contains the settings for the pipeline. You can modify this file to change the settings as needed.

### Step 5: Configure the Environment

Update the `.env` file with your OpenAI API key:

```plaintext
GRAPHRAG_API_KEY=<Your OpenAI API Key>
```

### Step 6: Update the Settings

Modify the `settings.yaml` file in `./ragtest`:

```yaml
llm:
  model: mistral
  api_base: http://localhost:55803/v1  # or your default Ollama port (e.g., 11434)

embeddings:
  model: nomic_embed_text
  api_base: http://localhost:55803/api  # or your default Ollama port (e.g., 11434/api)
```

Alternatively, you can copy the `settings.yaml` from this repository to ensure the correct configuration.

## Explanation of KG RAG

Knowledge Graph Retrieval-Augmented Generation (KG RAG) enhances the capabilities of language models by integrating structured knowledge from knowledge graphs. In KG RAG, the retrieval component searches for relevant information within the knowledge graph, which is then used to augment the input of the language model. This process improves the accuracy and relevance of the generated text by providing contextually rich and precise information.

## Conclusion

By following this tutorial, you have successfully set up GraphRAG with Ollama models for RAG. This setup allows you to leverage the power of knowledge graphs and advanced language models to generate high-quality, contextually relevant text.
