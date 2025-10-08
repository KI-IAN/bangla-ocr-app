"""
A Gradio web application for performing Optical Character Recognition (OCR)
on images containing Bangla and English text using the EasyOCR library.

This application provides a simple user interface to upload an image and view
the extracted text along with the processing time. It is instrumented with
Langfuse for observability.
"""

import gradio as gr
import easyocr
import numpy as np
import time
from pathlib import Path
from langfuse import observe

# Use home directory for model storage
model_dir = Path("/tmp/easyocr_models")
model_dir.mkdir(parents=True, exist_ok=True)

reader = easyocr.Reader(['bn', 'en'], gpu=False, model_storage_directory=str(model_dir))

@observe()
def ocr_image(image):
    """
    Performs OCR on an image to extract Bangla and English text.

    This function is decorated with `@observe` to trace its execution with Langfuse.

    Args:
        image (PIL.Image.Image): The image uploaded by the user via the Gradio interface.

    Returns:
        tuple[str, str]: A tuple containing:
            - The extracted text as a single string.
            - A formatted string indicating the processing time.
    """
    if image is None:
        return "No image uploaded.", ""
    start_time = time.time()
    img_array = np.array(image)
    results = reader.readtext(img_array)
    extracted_text = " ".join([text for _, text, _ in results])
    if not extracted_text:
        extracted_text = "No Bangla text detected."
    duration = time.time() - start_time
    human_time = f"⏱ Time taken: {duration:.2f} seconds"
    return extracted_text, human_time


with gr.Blocks() as demo:
    gr.HTML("""
    <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap; margin-bottom: 20px;">
        <h1 style="margin: 0;">🇧🇩 Bangla OCR App</h1>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="https://github.com/JaidedAI/EasyOCR" target="_blank">
                <img src="https://img.shields.io/badge/EasyOCR-OCR%20Engine-green" alt="EasyOCR">
            </a>
            <a href="https://opencv.org/" target="_blank">
                <img src="https://img.shields.io/badge/OpenCV-Image%20Processing-blue?logo=opencv" alt="OpenCV">
            </a>
            <a href="https://numpy.org/" target="_blank">
                <img src="https://img.shields.io/badge/NumPy-Arrays-blue?logo=numpy" alt="NumPy">
            </a>
            <a href="https://pytorch.org/" target="_blank">
                <img src="https://img.shields.io/badge/PyTorch-Backend-orange?logo=pytorch" alt="PyTorch">
            </a>
            <a href="https://langfuse.com/" target="_blank">
                <img src="https://img.shields.io/badge/Langfuse-Observability-blue" alt="Langfuse">
            </a>
        </div>
    </div>
    <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 20px; align-items: center;">
        <div>
            <span style="font-size: 16px;">📦 <strong>Source Code:</strong></span>
            <a href="https://github.com/KI-IAN/bangla-ocr-app.git" target="_blank"><img src="https://img.shields.io/badge/GitHub-Repo-blue?style=for-the-badge&logo=github" alt="GitHub Repo"></a>
        </div>
        <div>
            <span style="font-size: 16px;">📖 <strong>Project Story:</strong></span>
            <a href="https://frkhan.medium.com/turning-pages-into-pixels-the-making-of-a-bangla-ocr-app-9022bbffcd60" target="_blank"><img src="https://img.shields.io/badge/Medium-Read%20Story-black?style=for-the-badge&logo=medium" alt="Read Story on Medium"></a>
        </div>
    </div>
    """)

    gr.Interface(
        fn=ocr_image,
        inputs=gr.Image(type="pil"),
        outputs=[
            gr.Textbox(label="Extracted Text", lines=20),
            gr.Textbox(label="Duration")
        ],
        title="Bangla OCR App",
        description="Upload an image with Bangla text to extract it using EasyOCR.",
        allow_flagging="never"
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
