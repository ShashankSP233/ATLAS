from fastapi import FastAPI, Response
from pydantic import BaseModel
import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from NyayaAI import *  # Assuming the model function is inside NyayaAI.py

app = FastAPI()

# Pydantic model to handle input
class UserInput(BaseModel):
    text: str

# Define the POST route
@app.post("/search")
async def search(request: UserInput, response: Response):
    try:
        # Load the data from the JSON file
        with open('data.json', 'r') as f:
            lawdata = json.load(f)

        # Get the user's input from the request body
        user_input = request.text

        # Call the model function with the user input
        matching_data = model(user_input, data=lawdata)

        # Return the results as a JSON response
        return matching_data

    except Exception as e:
        # Handle errors gracefully
        return {"error": str(e)}