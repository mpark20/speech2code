import os
import google.generativeai as genai  # type: ignore
from flask import Flask, request, jsonify

app = Flask(__name__)


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
        "This is an audio transcript. This is supposed to be a person "
        "speaking what they want in code. "
        "Generate the code to copy and paste: " + command
    )

    # Return the generated code as a JSON response
    result = {"message": response.text}
    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000)
