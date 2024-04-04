from chains import full_chain
from dotenv import load_dotenv

load_dotenv("../.env")


if __name__ == "__main__":
    result = full_chain.invoke(
        {"question": "What is the difference between langchain and langsmith?"}
    )
    print(result)
