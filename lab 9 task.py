
# Text Generation using Hugging Face GPT-2 with Gradio UI

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import gradio as gr

model_name = "gpt2"  
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

def generate_text(prompt: str, max_length: int = 100) -> str:
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


interface = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your prompt here...", label="Prompt"),
        gr.Slider(minimum=20, maximum=200, step=10, value=100, label="Max Length")
    ],
    outputs="text",
    title="Text Generation with GPT-2",
    description="Enter a text prompt and let GPT-2 continue the story!"
)


interface.launch()
