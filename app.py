import os
import openai

openai.api_key = "API KEY"


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "define man in a line"
    }
  ]
)
print(response)