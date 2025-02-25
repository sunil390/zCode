from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="ibm/granite-3.0-3b-a800m-instruct",
  messages=[{"role":"user","content":"Write a limerick about the wonders of GPU computing."}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

