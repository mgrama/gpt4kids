import openai

def get_response(text, api_key):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=150,
        api_key=api_key
    )
    return response.choices[0].text.strip()
