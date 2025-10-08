---
title: Bangla OCR Web App
emoji: 🧠
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 5.46.1
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

- **Live App**: Try it out here: **[Bangla OCR Demo App](https://huggingface.co/spaces/frkhan/bangla-ocr)**
- **Project Story**: Curious about how this app was built? **[Read the full story on Medium](https://frkhan.medium.com/turning-pages-into-pixels-the-making-of-a-bangla-ocr-app-9022bbffcd60)** to see the journey from idea to deployment.

---

## 🧰 Tech Stack

| Tool             | Purpose                          |
| ---------------- | -------------------------------- |
| `Gradio`         | Web interface for user input     |
| `EasyOCR`        | Text extraction from images      |
| `OpenCV`         | Image processing backend for EasyOCR |
| `NumPy`          | Array manipulation               |
| `Langfuse`       | Observability and tracing        |
| `Docker`         | Containerized deployment         |
| `Docker Compose` | Service orchestration            |
| `PyTorch`        | Backend for EasyOCR              |

---

## 📦 Installation

You can run the app in three different ways:

### 🔧 Option 1: Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KI-IAN/bangla-ocr-app
    cd bangla-ocr-app
    ```

2.  **Create and activate a virtual environment:** A virtual environment isolates the project's dependencies from your system's global Python packages.

    ```bash
    # Create the virtual environment (you only need to do this once per project)
    # On some systems, you might need to use `python3` instead of `python`
    python -m venv venv
    ```

    Next, activate the environment. The command depends on your operating system:

    *   **On Windows (Command Prompt / PowerShell):**
        ```bash
        venv\Scripts\activate
        ```

    *   **On macOS / Linux (bash, zsh, etc.):**
        ```bash
        source venv/bin/activate
        ```
    *Your terminal prompt should now change to show `(venv)` at the beginning.*

3.  **Install dependencies:** With the virtual environment active, install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the app:**
    ```bash
    python app.py
    ```

The app will be running at `http://127.0.0.1:12300`.

*(When you're finished, you can leave the virtual environment by simply running the `deactivate` command.)*

### 🐳 Option 2: Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t bangla-ocr-app .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 12300:7860 bangla-ocr-app
    ```
    Open your browser and visit: http://localhost:12300

### 🧱 Option 3: Docker Compose

```bash
# To Run in Live environment. It automatically uses the docker-compose.yml
docker-compose up --build 

# Or If you use the latest docker compose command, use the following

docker compose up --build
```

Access the app at http://localhost:12300

---


```bash
# To Run in local environment use docker-compose.dev.yml if you want to reflect your code changes without rebuilding docker container
docker-compose -f docker-compose.dev.yml up --build

# Or If you use the latest docker compose command, use the following
docker compose -f docker-compose.dev.yml up --build

```

Access the app at http://localhost:12300


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
├── app.py                  # Main application logic
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container setup
├── docker-compose.yml      # Multi-container orchestration for production
├── docker-compose.dev.yml  # Multi-container orchestration for development
├── .env                    # Environment variables for Langfuse (Optional)
└── README.md               # Project documentation
```

## 🌍 Language Support

[EasyOCR](https://github.com/JaidedAI/EasyOCR#all-supported-languages-in-alphabetical-order) supports over 80 languages. This app is pre-configured for:

- 🇧🇩 **Bangla** (`bn`)
- 🇺🇸 **English** (`en`)

To add more languages, modify the following line in `app.py`:

```python
# From
reader = easyocr.Reader(['bn', 'en'], gpu=True)

# To (for example, adding Hindi, Arabic, Urdu, Malay, Chinese, and Japanese)
reader = easyocr.Reader(['bn', 'en', 'hi', 'ar', 'ur', 'ms', 'ch_sim', 'ja'], gpu=True)
```


## 📜 License

This project is open-source and distributed under the **[MIT License](https://opensource.org/licenses/MIT)**. Feel free to use, modify, and distribute it with attribution.

---

## 🤝 Acknowledgements

- **[EasyOCR](https://github.com/JaidedAI/EasyOCR)** for its powerful and accessible multilingual OCR library.
- **[Gradio](https://www.gradio.app/)** for making it incredibly simple to create machine learning interfaces.
- **[PyTorch](https://pytorch.org/)** for powering the deep learning backend.
- **[Docker](https://www.docker.com)** — Containerization platform for reproducible deployment across environments.
- **[Hugging Face Spaces](https://huggingface.co/spaces)** — Free hosting platform for ML demos with secret management and GPU support.
-   **[Langfuse](https://langfuse.com/)** for providing excellent observability tools.

> “Small tools, big impact.” — Let’s make machine learning approachable, one project at a time.
