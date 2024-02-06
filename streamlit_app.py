import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import torch
from your_generative_model_module import generate_correct_order  # Replace with your generative model function

st.title("Image Arrangement Solver")

# Function to generate correct image arrangement
def generate_solution(arranged_images):
    # Call your generative model function here
    solution = generate_correct_order(arranged_images)
    return solution

# Upload multiple image files through Streamlit
uploaded_files = st.file_uploader("Choose multiple images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    # Display the uploaded images
    uploaded_images = [Image.open(file) for file in uploaded_files]
    st.image(uploaded_images, caption="Uploaded Images", use_column_width=True)

    # Arrange the images randomly for initial display
    np.random.shuffle(uploaded_images)

    # Display the randomly arranged images
    st.image(uploaded_images, caption="Randomly Arranged Images", use_column_width=True)

    # Button to generate the correct arrangement
    if st.button("Generate Correct Arrangement"):
        # Convert images to NumPy arrays
        arranged_images_array = [np.array(image) for image in uploaded_images]

        # Generate the correct image arrangement
        solution = generate_solution(arranged_images_array)

        # Display the correct arrangement
        st.image(solution, caption="Correct Image Arrangement", use_column_width=True)

