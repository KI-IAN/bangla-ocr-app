import gradio as gr
import easyocr
import numpy as np
from PIL import Image

# Load EasyOCR reader with Bangla support
reader = easyocr.Reader(['bn'], gpu=True)

def ocr_image(image):
    if image is None:
        return "No image uploaded."
    img_array = np.array(image)
    results = reader.readtext(img_array)
    extracted_text = " ".join([text for _, text, _ in results])
    return extracted_text or "No Bangla text detected."

iface = gr.Interface(
    fn=ocr_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Bangla OCR Demo",
    description="Upload an image with Bangla text to extract it using EasyOCR.",
    
)

if __name__ == "__main__":
    iface.launch()
