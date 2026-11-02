"""HB-1: send one Korean question to an LLM and print the answer."""
import os
import sys
from xml.parsers.expat import model
import ollama
from dotenv import load_dotenv

QUESTION = "경북대학교는 어느 도시에 있나요?"


def main() -> None:
    # TODO 1: load the variables in .env
    load_dotenv()
    model = os.getenv("LLM_MODEL")
    # TODO 2: read LLM_MODEL (and OPENAI_API_KEY if you use OpenAI)
    api_key = os.getenv("OPENAI_API_KEY")
    # TODO 3: if a value is missing, stop with a clear error message
    if not model:
        sys.exit("Error: LLM_MODEL is missing. Add LLM_MODEL to your .env file.")
    # TODO 4: create the client and send QUESTION
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": QUESTION}],
    )
    # TODO 5: print the question, the answer and the token usage
    print(f"answer: {response['message']['content']}")
    print(f"Tokens: input={response["prompt_eval_count"]}, output={response["eval_count"]}")

if __name__ == "__main__":
    main()