# Import Google's Gemini SDK
from google import genai

# Load the API key from the .env file
from dotenv import load_dotenv

load_dotenv()

# Create the Gemini client
client = genai.Client()

# Send a request to Gemini
response = client.interactions.create(
    model="gemini-3.8-flash",
    input="Say hello to my first Python AI project!"
)

# Display Gemini's response
print(response.output_text)