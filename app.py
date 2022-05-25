import streamlit as st
from PIL import Image
from util import get_pred

st.title("Mars Orbital Image (HiRISE) Classification")
st.header("Upload Test Image : ")


uploaded_file = st.file_uploader("Choose a Image ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label, conf = get_pred(
           image)

    st.write(f"Image is '{label}' with {conf} % confidence.")
