import streamlit as st
from PIL import Image
import os

# Function to process the image (example: convert to grayscale)
def process_image(input_image):
    processed_image = input_image.convert('L')
    return processed_image

def main():
    st.set_page_config(
        page_title="Jigsaw Puzzle App",
        page_icon="🧩",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title('JIGSAW PUZZLE')

    # Set overall page style with background image
    st.markdown(
        """
        <style>
        body {
            font-family: 'Helvetica', sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
            color: #333333;
            background-image: url('your_background_image_url_here');  /* Add your image URL */
            background-size: cover;
        }
        .main-container {
            max-width: 1000px;
            margin: auto;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        }
        .title {
            background-color: #007bff;
            color: white;
            padding: 20px;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
            font-size: 32px;
            text-align: center;
        }
        .upload-section {
            padding: 20px;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
        }
        .uploaded-image, .processed-image {
            border-radius: 10px;
            margin-top: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    st.markdown('<div class="title">Jigsaw Puzzle App</div>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    st.markdown('<div class="upload-section">', unsafe_allow_html=True)

    if uploaded_file is not None:
        # Display original image
        st.text("Original Image")
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption='Original Image', use_column_width=True, output_format="JPEG")

        # Process the image when the "Process" button is clicked
        if st.button("Process Image", key="process_button"):
            # Process the image
            processed_image = process_image(original_image)

            # Display processed image
            st.text("Processed Image")
            st.image(processed_image, caption='Processed Image', use_column_width=True, output_format="JPEG")

            # Save the processed image (optional)
            if st.button("Save Processed Image", key="save_button"):
                processed_image.save("processed_image.jpg")
                st.success("Processed image saved successfully!")

    st.markdown('</div>', unsafe_allow_html=True)  # Close upload-section

    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

if __name__ == "__main__":
    main()


