# Stable Diffusion Image-to-Image Generator

This project is a simple Streamlit-based web application that allows users to generate new images based on an initial image and a text prompt using the Stable Diffusion model.

## Features
- Upload an initial image to condition the generation.
- Enter a text prompt to guide the image transformation.
- Adjust the strength of the transformation.
- View the generated image directly in the web interface.

## Requirements
- Python 3.7 or higher
- `streamlit`
- `torch`
- `diffusers`
- `transformers`
- `Pillow`


### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kaleabMelkamu/Stable-Diffusion.git
   cd Stable-Diffusion

2. **Set up a virtual environment:**
   ```bash
    python -m venv .venv
   .venv\Scripts\activate

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

6. **Running the Application**
     ```bash
   streamlit run app.py`

Visit http://localhost:8501 in your web browser to view the app.
