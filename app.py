import streamlit as st
from PIL import Image
import torch
from diffusers import StableDiffusionImg2ImgPipeline

# Load the pre-trained model from Hugging Face
@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    # Load the pipeline with CPU settings
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_id
    ).to("cpu")  # Use "cpu" if you do not have a CUDA-enabled GPU
    return pipe

# Initialize the model
pipe = load_model()

# Streamlit app title
st.title("Stable Diffusion Image-to-Image Generator")

# Upload an initial image
uploaded_image = st.file_uploader("Upload an initial image", type=["jpg", "png", "jpeg"])
prompt = st.text_input("Enter your text prompt", "A futuristic city at sunset")

# Slider for the strength of the transformation
strength = st.slider("Transformation strength", 0.1, 1.0, 0.5)

if uploaded_image is not None:
    # Display the uploaded image
    initial_image = Image.open(uploaded_image).convert("RGB")
    st.image(initial_image, caption="Initial Image", use_column_width=True)

    # Generate the image when the button is clicked
    if st.button("Generate Image"):
        with st.spinner("Generating..."):
            # Run the model to generate a new image
            generated_image = pipe(prompt=prompt, image=initial_image, strength=strength, num_inference_steps=50).images[0]
            st.image(generated_image, caption="Generated Image", use_column_width=True)
else:
    st.warning("Please upload an initial image to proceed.")
