import gradio as gr
import easyocr
import numpy as np
from PIL import Image
import time
from pathlib import Path

from pathlib import Path

# Use home directory for model storage
model_dir = Path("/tmp/easyocr_models")
model_dir.mkdir(parents=True, exist_ok=True)

reader = easyocr.Reader(['bn', 'en'], gpu=True, model_storage_directory=str(model_dir))


def ocr_image(image):
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

iface = gr.Interface(
    fn=ocr_image,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Duration")
    ],
    title="Bangla OCR Demo",
    description="Upload an image with Bangla text to extract it using EasyOCR.",
    allow_flagging="never"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0")