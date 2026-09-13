import os
from google import genai

# uv add google-genai
# or pip install google-genai

client = genai.Client()

while True:
    # Initiate a streaming interaction
    response_stream = client.interactions.create(
        model="models/gemini-3.7-flash", 
        input=input("User: "),
        stream=True
    )

    print("Assistant: ", end="")
    print(response_stream)

    # Iterate through the chunks as they stream in
    for chunk in response_stream:
    
        # Check if the chunk contains text delta and print it
        if hasattr(chunk, 'delta') and hasattr(chunk.delta, 'text') and chunk.delta.text:
            print(chunk.delta.text, end="", flush=True)
            
    print()
