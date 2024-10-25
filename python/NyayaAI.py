import json
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

with open('data.json', 'r') as f:
    lawdata = json.load(f)

def preprocess_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c.isalnum() or c.isspace()])
    return text

def model(user_input, data = lawdata, similarity_threshold=0.55):
    """
    Args:
        user_input: The user's input text.
        data: The list of dictionaries containing the data.
        similarity_threshold: The minimum similarity score for a match.
    Returns:
        A list of dictionaries containing matching rows from the data:
            law: The IPC section
            description: The description of the IPC section
            punishment: The punishment associated with the IPC section
    """
    try:
        model = "SentenceTransformer('all-MiniLM-L12-v2')"
    except Exception as e:
        print(f"Error creating model: {e}")
        return []

    user_input = preprocess_text(user_input)
    user_vector = model.encode(user_input, convert_to_tensor=True)
    return_data = []
    for item in data:
        try:
            law, description, punishment = item["laws"], item["description"], item["Punishment"]
            description = preprocess_text(description)
            text_vector = model.encode(description, convert_to_tensor=True)
            similarity = cos_sim(user_vector, text_vector).item()
            if similarity >= similarity_threshold:
                return_data.append({"law": law, "description": description, "punishment": punishment})
        except Exception as e:
            print(f"Error processing item: {e}")
            continue
    return return_data

"""
law = input("Enter prompt: ")
matching_data = model(law)
json_data = json.dumps(matching_data, indent=4)
print(json_data)
"""