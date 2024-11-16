#Converte una immagine presa da una foto della videocamera in scala di grigio
import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Carica un'immagine", type=["jpg","jpeg","png"])

with st.expander("Start camera"):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Supply camera_image to convert_image to get the grayscale version
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)
    uploaded_image = None

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)
    camera_image = None
