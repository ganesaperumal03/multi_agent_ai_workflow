from groq import groq
from app.config import settings

client = groq(api_key=settings.GROQ_API_KEY)


async def call_llm(prompt: str) -> str:
    response = await client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {"role": "system", "content": "You are a professional AI engineering assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content