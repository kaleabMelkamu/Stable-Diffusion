import streamlit as st
from PIL import Image
import torch
from diffusers import StableDiffusionImg2ImgPipeline

# Load the pre-trained model from Hugging Face
@st.cache_resource
def load_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_id
    ).to("cpu")  
    return pipe


pipe = load_model()


st.title("Stable Diffusion Image-to-Image Generator")


uploaded_image = st.file_uploader("Upload an initial image", type=["jpg", "png", "jpeg"])
prompt = st.text_input("Enter your text prompt", "A futuristic city at sunset")


strength = st.slider("Transformation strength", 0.1, 1.0, 0.5)

if uploaded_image is not None:
    # Display the uploaded image
    initial_image = Image.open(uploaded_image).convert("RGB")
    st.image(initial_image, caption="Initial Image", use_column_width=True)

    # Generate the image when the button is clicked
    if st.button("Generate Image"):
        with st.spinner("Generating..."):
           
            generated_image = pipe(prompt=prompt, image=initial_image, strength=strength, num_inference_steps=50).images[0]
            st.image(generated_image, caption="Generated Image", use_column_width=True)
else:
    st.warning("Please upload an initial image to proceed.")
