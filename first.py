import requests

def send_prompt(prompt):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer lmstudio"  # static token used by LM Studio
    }
    payload = {
        "model": "local-model",  # can be any string; LM Studio ignores it
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    prompt = "Explain what a black hole is."
    print("Prompt:", prompt)
    reply = send_prompt(prompt)
    print("Response:", reply)
