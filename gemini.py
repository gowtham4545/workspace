import os

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Add it to the environment or a .env file."
        )

    client = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    response = client.chat.completions.create(
        model="gemini-3.8-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant.You give response according to the context of the question and the weight of the question.You dont give more response than needed or when explicitly asked for."},
            {"role": "user", "content": "Indian national anthem title"},
        ],
        stream=False,
    )

    if not response.choices or response.choices[0].message.content is None:
        raise RuntimeError("Gemini returned an empty response.")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
