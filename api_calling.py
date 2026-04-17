from google import genai
from dotenv import load_dotenv
import os ,io

#load the env variable
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

#initializing a client 
client = genai.Client(api_key= my_api_key)

#error find
def error_finder_generator(images):
    prompt="""Analize the picture and find the error of the code
    in this section you only display what are the error and what types of error
    are happend in the images do not show the correct code in this section
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text

def solution_generator(image,option):
    prompt = f"""Generate text based on the {option}. Make sure to add markdown to diffrentate in text. 
     1. If the user selects option== "Hint":
    - Do NOT provide the corrected code.
    - Only give clear hints or guidance about what is wrong.
    - Explain the type of error (e.g., TypeError, SyntaxError, etc.).
    - Suggest what concept or part of the code needs fixing.
    - Keep the explanation simple and helpful.

    2. If the user selects option == "Solution with Code":
    - Provide the fully corrected version of the code.
    - Ensure the code runs without errors.
    - Optionally include a short explanation of what was fixed.

    Rules:
 - Never show the corrected code when the user selects "Hint".
 - Always ensure the explanation matches the user's selected option.
 - Be concise, clear, and beginner-friendly.
    """
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text 
