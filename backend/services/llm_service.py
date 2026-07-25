from openai import OpenAI

from config import config
print("Using model:", config.OPENROUTER_MODEL)

client = OpenAI(
    api_key=config.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def generate_sql(prompt: str) -> str:
    """
    Sends the prompt to OpenRouter and returns generated SQL.
    """

    response = client.chat.completions.create(
        model=config.OPENROUTER_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert PostgreSQL SQL generator. "
                    "Return ONLY SQL."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    question = input("Ask: ")

    sql = generate_sql(question)

    print("\nGenerated SQL\n")
    print(sql)