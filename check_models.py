import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Listing models using new google-genai SDK:")
for m in client.models.list():
    print(f"- {m.name}")