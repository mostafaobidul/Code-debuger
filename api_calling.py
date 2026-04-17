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
    prompt = f"Generate text based on the {option}. Make sure to add markdown to diffrentate in text. and generate which option is selected if solution_with_code selected then generate code only otherwise generate only hints for users and when user choose hints don't show the correct code give only hints of the solution"
    
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text 
