# utils.py
from openai import OpenAI

client = OpenAI()

def spell_check(input):
    messages = [
        {"role": "system",
         "content": "Please check the given text for spelling errors and provide corrections"},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=100
    )
    reply = completion.choices[0].message.content
    return reply