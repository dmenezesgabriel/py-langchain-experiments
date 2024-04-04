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

- [](https://github.com/langchain-ai/langgraph/blob/main/examples/plan-and-execute/plan-and-execute.ipynb)
- [](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_adaptive_rag_cohere.ipynb)
- [](https://github.com/langchain-ai/langgraph/blob/main/examples/reflection/reflection.ipynb)
- [](https://github.com/langchain-ai/langgraph/blob/main/examples/reflexion/reflexion.ipynb)
- [](https://github.com/langchain-ai/langgraph/blob/main/examples/lats/lats.ipynb)
