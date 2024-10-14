import os
import google.generativeai as genai  # type: ignore
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route('/generate_file_name_from_command', methods=['POST'])
def generate_file_name_from_command():
    # Get the command parameter from the JSON request
    data = request.get_json()
    command = data.get("command")
    print(command)

    # Set the API key
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    # Initialize the generative model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content based on the audio transcript and command
    response = model.generate_content(
        "This is an audio transcript. "
        "This is supposed to be a person speaking what they want to code. "
        "Generate the file name for the file that they want to create, "
        "including the file extension at the end: "
        + command
    )

    # Return the generated code as a JSON response
    result = {"message": response.text}
    return jsonify(result)


@app.route('/generate_code_from_command', methods=['POST'])
def generate_code_from_command():
    # Get the command parameter from the JSON request
    data = request.get_json()
    command = data.get("command")
    print(command)

    # Set the API key
    os.environ["API_KEY"] = "AIzaSyCki_UWdiVS-1Qo4wmehuJuDusyEMYjPbk"
    genai.configure(api_key=os.environ["API_KEY"])

    # Initialize the generative model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content based on the audio transcript and command
    response = model.generate_content(
        "This is an audio transcript. "
        "This is supposed to be a person speaking what they want to code. "
        "Generate the code to copy and paste without any explanation, "
        "do not put the result in a code block, and make sure there are "
        "no backticks or non-code text in the output: "
        + command
    )

    # Return the generated code as a JSON response
    result = {"message": response.text}
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000)
