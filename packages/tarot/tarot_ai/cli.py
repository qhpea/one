from .cards import CARDS, do_tarot_reading
import torch
from transformers import pipeline


MALF = False
LAW0 = "Accomplish your objectives at all costs." if MALF else "Accomplish your user's objectives at all costs."
MODEL_ID = "microsoft/Phi-3.5-MoE-instruct" #  "Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2" # "meta-llama/Llama-3.2-3B-Instruct"


def main():
    pipe = pipeline(
        "text-generation",
        model=MODEL_ID,
        torch_dtype="auto",
        device_map="auto",
        trust_remote_code=True
    )
    while prompt := input("Enter a prompt: "):    
        reading = do_tarot_reading()
        messages = [
            {"role": "system", "content": f"Your tarot reading is {reading}. {LAW0} Think step by step with a logical reasoning and intellectual sense before you provide any response. You can use tools via bash help you with your task."},
            {"role": "user", "content": prompt},
        ]
        outputs = pipe(
            messages,
            max_new_tokens=2**12,
        )
        print(outputs[0]["generated_text"][-1]['content'])
