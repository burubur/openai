import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: design a scandinavian home for me"
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)
data = response.data

file_path = "output"
with open(file_path, "a") as file:
    file.write("\n" + str(data))

with open(file_path, "r") as file:
    content = file.read()
    print(content)
