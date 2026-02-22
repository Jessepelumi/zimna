from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def test_openai_integration():
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-2025-04-14",
            messages=[{
                "role": "user",
                "content": "Generate a roadmap to learn data structures and algorithms"
            }],
            max_tokens=100,
            temperature=0.7
        )

        print("OpenAI API Response:")
        print(response.choices[0].message.content.strip())
    except Exception as e:
        print(f"OpenAI Error: {e}")

if __name__ == "__main__":
    test_openai_integration()