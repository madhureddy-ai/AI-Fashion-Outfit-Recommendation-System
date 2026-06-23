import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

query = input("Ask: ")

prompt = f"""
Extract gender, occasion and style from:

'{query}'

Return only JSON.
"""

response = model.generate_content(prompt)

print(response.text)