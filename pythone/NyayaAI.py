from transformers import AutoTokenizer, AutoModel
import pandas as pd
import torch
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load Llama Model and Tokenizer
model_name = "meta-llama/Llama-2-7b-chat-hf"  # Update with your specific Llama version
model = AutoModel.from_pretrained(model_name, cache_dir="D:/nayaa/model",
                                             device_map = 'auto')
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="D:/nayaa/model")
print("reading json")
# Load JSON Data
with open(r'D:\nayaa\pythone\data.json', 'r') as f:
    lawdata = json.load(f)

# Function to Preprocess Text
def preprocess_text(text):
    return ''.join([c for c in text.lower() if c.isalnum() or c.isspace()])

# Function to Generate Embeddings  
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
print("embeding to start")
# Generate and Store Embeddings for Each Section
for item in lawdata:
    item['embedding'] = get_embedding(preprocess_text(item['description']))
print("saving")
# Save Embeddings to a Pickle File for Future Use
with open('ipc_embeddings.pkl', 'wb') as f:
    pickle.dump(lawdata, f)

print("Embeddings saved to ipc_embeddings.pkl")
