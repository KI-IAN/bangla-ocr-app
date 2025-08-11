import torch

print(torch.cuda.is_available())

def greet(name):
    return f"Hello, {name}!"

print(greet("Bangla OCR"))

