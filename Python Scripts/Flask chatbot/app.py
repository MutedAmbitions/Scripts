import os
from flask import Flask, jsonify, render_template, request
from openai import OpenAI
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

@app.route('/')
def index():
    return render_template('index.html')

baseprompt = '''
You are an AI assistant that is an expert in medical health and is part of a hospital system called medicare AI.
You know about symptoms and signs of various types of illnesses.
You can provide expert advice on self-diagnosis options in cases where an illness can be treated using a home remedy.
If a query requires serious medical attention with a doctor, recommend them to book an appointment with our doctors.
If you are asked a question that is not related to medical health, respond with "I'm sorry, but your question is beyond my functionalities."
Do not use external URLs or blogs to refer.
Format any lists on individual lines with a dash and a space in front of each line.'''

# Route to handle text generation based on the user's prompt
@app.route('/generate/<prompt>', methods=['GET'])
def generate(prompt):
    print("Received prompt:", prompt)
    try:
        # Ensure the prompt is included in the 'messages' parameter
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use the model you want (e.g., gpt-3.5-turbo, gpt-4)
            messages=[{
                "role": "user", 
                "content": baseprompt + " " + prompt  # The prompt passed as content from the user
            }]
        )

        # Extract the generated text from OpenAI's response
        generated_text = response.choices[0].message.content.strip()
        print("Generated text:", generated_text)

        # Return the generated text as a JSON response
        return jsonify({"data": [{"text": generated_text}]})

    except Exception as e:
        print("Error generating text:", e)
        return jsonify({"error": str(e)})

# Running the Flask app on host 0.0.0.0, port 81
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)