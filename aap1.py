# app.py
import streamlit as st
import os
from PIL import Image

# Function to process the image (example: convert to grayscale)
def process_image(input_image):
    processed_image = input_image.convert('L')  # Placeholder for your actual processing logic
    return processed_image

def main():
    st.set_page_config(
        page_title="Jigsaw Puzzle App",
        page_icon="🧩",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Create input and output directories if they don't exist
    input_dir = "input"
    output_dir = "output"
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    st.title("Jigsaw Puzzle Solver")

    # File uploader for input image
    uploaded_file = st.file_uploader("Choose an input image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded input image
        st.subheader("Uploaded Image:")
        input_image = Image.open(uploaded_file)

        # Save the input image to the input folder
        input_filename = os.path.join(input_dir, f"input_{len(os.listdir(input_dir)) + 1}.jpeg")
        input_image.save(input_filename)

        # Display input and output images side by side
        col1, col2 = st.columns(2)

        # Set the scaling factor (increase or decrease by the same ratio)
        scaling_factor = st.slider("Scaling Factor", 0.1, 3.0, 1.0, 0.1)

        # Calculate new width and height for the original input image
        original_width, original_height = input_image.size
        input_image_width = int(original_width * scaling_factor)
        input_image_height = int(original_height * scaling_factor)

        with col1:
            st.image(input_image, caption="Uploaded Input Image", use_column_width=True, width=input_image_width)

        # Process the image when the "Process Image" button is clicked
        if st.button("Process Image"):
            # Process the image
            output_image = process_image(input_image)

            # Calculate new width and height for the processed output image
            processed_width, processed_height = output_image.size
            output_image_width = int(processed_width * scaling_factor)
            output_image_height = int(processed_height * scaling_factor)

            with col2:
                st.image(output_image, caption="Processed Output Image", use_column_width=True, width=output_image_width)

            # Save the output image to the output folder
            output_filename = os.path.join(output_dir, f"output_{len(os.listdir(output_dir)) + 1}.png")
            output_image.save(output_filename)

if __name__ == "__main__":
    main()
