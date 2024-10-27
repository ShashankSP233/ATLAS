import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-hf",
                                             cache_dir="D:/nayaa/model",
                                             device_map = 'auto')
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-hf",cache_dir="D:/nayaa/model")