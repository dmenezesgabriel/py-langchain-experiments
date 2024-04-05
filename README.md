## Usage

- **Run services**:

```sh
docker compose up
```

- **Pull LLM model**:

```sh
docker compose exec -it ollama-llm /bin/sh -c "ollama pull mistral:instruct"
```

- **Pull run model**:

```sh
docker compose exec -it ollama-llm /bin/sh -c "ollama run mistral:instruct"
```

- **Access ollama shell**:

```sh
docker compose exec -it ollama-llm /bin/sh
```

## Resources

- [plan-and-execute](https://github.com/langchain-ai/langgraph/blob/main/examples/plan-and-execute/plan-and-execute.ipynb)
- [rag/](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_adaptive_rag_cohere.ipynb)
- [reflection](https://github.com/langchain-ai/langgraph/blob/main/examples/reflection/reflection.ipynb)
- [reflexion/](https://github.com/langchain-ai/langgraph/blob/main/examples/reflexion/reflexion.ipynb)
- [lats](https://github.com/langchain-ai/langgraph/blob/main/examples/lats/lats.ipynb)
- [langchain-agents](https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/06-langchain-agents.ipynb)
- [pinecone examples](https://github.com/pinecone-io/examples/tree/master/learn/generation/langchain/handbook)
- [langgraph examples](https://github.com/langchain-ai/langgraph/tree/main/examples)
