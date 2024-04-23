import openai

def get_response(text, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()
