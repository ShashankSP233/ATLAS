import pickle
import json
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

# Paths for files
MODEL_DIR = "D:/nayaa/model"
EMBEDDINGS_FILE = "ipc_embeddings.pkl"
JSON_FILE = "D:/nayaa/pythone/data.json"

# Load Llama model and tokenizer
model_name = "meta-llama/Llama-2-7b-chat-hf"  # Ensure this matches the downloaded version
model = AutoModel.from_pretrained(model_name, cache_dir=MODEL_DIR, device_map='auto')
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=MODEL_DIR)

# Load embeddings and data
with open(EMBEDDINGS_FILE, 'rb') as f:
    lawdata = pickle.load(f)
with open(JSON_FILE, 'r') as f:
    json_data = json.load(f)

# Preprocess text
def preprocess_text(text):
    return ''.join([c for c in text.lower() if c.isalnum() or c.isspace()])

# Generate embedding for user input
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# Find best matching law
def find_best_match(user_input):
    user_embedding = get_embedding(preprocess_text(user_input))
    
    similarities = []
    for item in lawdata:
        similarity = cosine_similarity(
            [user_embedding], [item['embedding']]
        )[0][0]
        similarities.append(similarity)

    best_match_index = similarities.index(max(similarities))
    best_match = json_data[best_match_index]

    return best_match

# Main function to get user input and display matching law details
if __name__ == "__main__":
    user_prompt = input("Enter the situation or description: ")
    best_match = find_best_match(user_prompt)
    
    print("\nBest Matching Law:")
    print(f"Law: {best_match['laws']}")
    print(f"Description: {best_match['description']}")
    print(f"Punishment: {best_match['Punishment']}")
