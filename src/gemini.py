import os
import google.generativeai as genai

def generate_code_from_command(command):
    # Set the API key
    os.environ["API_KEY"] = "AIzaSyCki_UWdiVS-1Qo4wmehuJuDusyEMYjPbk"
    genai.configure(api_key=os.environ["API_KEY"])

    # Initialize the generative model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content based on the audio transcript and command
    response = model.generate_content(
        "This is an audio transcript. This is supposed to be a person speaking what they want in code. "
        "Generate the code to copy and paste: " + command
    )

    return response.text

# Example usage
command_text = "Create a full React app that prints 'Hello World' on the front page and includes all files."
code_output = generate_code_from_command(command_text)
print(code_output)
