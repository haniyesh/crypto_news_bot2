import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from semantic.api.base import LLMAPI


class GemmaProvider(LLMAPI):
    def __init__(self, model="google/gemma-2b"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained(model)
        self.model = AutoModelForCausalLM.from_pretrained(
            model,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        ).to(self.device)

        self.model.eval()

    def generate(self, prompt: str, max_new_tokens=256, temperature=0.7):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=True
            )

        return self.tokenizer.decode(output[0], skip_special_tokens=True)