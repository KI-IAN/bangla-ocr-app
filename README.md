---
title: Bangla OCR Web App
emoji: 🧠
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: "5.42.0"
app_file: app.py
pinned: false
---

# 🇧🇩 Bangla OCR Web App with Gradio & EasyOCR

This project is a lightweight Optical Character Recognition (OCR) web application built using [Gradio](https://www.gradio.app/) and [EasyOCR](https://github.com/JaidedAI/EasyOCR). It allows users to upload images containing Bangla or English text and extract it instantly through a simple browser interface. Designed for fast deployment and minimal setup, it runs locally, in Docker, or via Docker Compose.

---

## 🚀 Features

- 📷 Upload or drag-and-drop images for OCR.
- 🔍 Extract both **Bangla** and **English** text using EasyOCR.
- ⚡ GPU-accelerated for fast inference (if a compatible GPU and CUDA are available).
- 🌐 Launch a user-friendly web interface with Gradio.
- 🐳 Full support for containerized deployment with **Docker** and **Docker Compose**.
- 🧼 Clean UI with dual output: extracted text and processing duration.

---

## 🔗 Live Demo

Try it out here: **[Gradio Hosted App](https://your-demo-link.com)**  
*(Note: Replace with your actual Gradio or other hosted link.)*

---

## 🧰 Tech Stack

| Tool             | Purpose                          |
| ---------------- | -------------------------------- |
| `Gradio`         | Web interface for user input     |
| `EasyOCR`        | Text extraction from images      |
| `OpenCV`         | Image preprocessing              |
| `NumPy`          | Array manipulation               |
| `Docker`         | Containerized deployment         |
| `Docker Compose` | Service orchestration            |
| `PyTorch`        | Backend for EasyOCR              |

---

## 📦 Installation

You can run the app in three different ways:

### 🔧 Option 1: Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/bangla-ocr-app.git
    cd bangla-ocr-app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the app:**
    ```bash
    python app.py
    ```
    The app will be running at `http://127.0.0.1:7860`.

### 🐳 Option 2: Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t bangla-ocr .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 7860:7860 bangla-ocr
    ```
    Open your browser and visit: [http://localhost:7860](http://localhost:7860)

### 🧱 Option 3: Docker Compose

1.  **Start the app using Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    Open your browser and visit: [http://localhost:7860](http://localhost:7860)

---

## 🖼️ Example

Upload an image containing Bangla or English text.

**Example Input:**
  
*(Note: Replace with a link to an actual example image.)*

**Example Output:**
```text
Extracted Text:
"বাংলা ভাষা আমাদের গর্ব।"

⏱️ Time taken: 0.87 seconds
```

## 📁 File Structure

```text
bangla-ocr-app/
├── app.py               # Main application logic
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container setup
├── docker-compose.yml   # Multi-container orchestration
└── README.md            # Project documentation
```

## 🌍 Language Support

[EasyOCR](https://github.com/JaidedAI/EasyOCR#all-supported-languages-in-alphabetical-order) supports over 80 languages. This app is pre-configured for:

- 🇧🇩 **Bangla** (`bn`)
- 🇺🇸 **English** (`en`)

To add more languages, modify the following line in `app.py`:

```python
# From
reader = easyocr.Reader(['bn', 'en'], gpu=True)

# To (for example, adding Hindi)
reader = easyocr.Reader(['bn', 'en', 'hi'], gpu=True)
```


## 📜 License

This project is open-source and distributed under the **[MIT License](https://opensource.org/licenses/MIT)**. Feel free to use, modify, and distribute it with attribution.

---

## 🤝 Acknowledgements

- **[EasyOCR](https://github.com/JaidedAI/EasyOCR)** for its powerful and accessible multilingual OCR library.
- **[Gradio](https://www.gradio.app/)** for making it incredibly simple to create machine learning interfaces.
- **[PyTorch](https://pytorch.org/)** for powering the deep learning backend.

> “Small tools, big impact.” — Let’s make machine learning approachable, one project at a time.

