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
