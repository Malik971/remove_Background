import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64


st.title("Retirer le Background de l'image :camera:")

st.write("Malik Ibo Project")

st.sidebar.write("## Changer l'image :camera:")

max_size = 5 * 1024 * 1024


col1, col2 = st.columns(2)

my_upload = st.sidebar.file_uploader("Choisir une image", type=["png", "jpg", "jpeg"])

def download_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    byte = buffered.getvalue()
    return byte

def remove_bg(image):
    input_image = Image.open(image)
    col1.write("Image originale :camera:")
    col1.image(input_image)

    output_image = remove(input_image)
    col2.write("Arière Plan Retirer :camera:")
    col2.image(output_image)

    st.sidebar.download_button(
        label="Télécharger l'image sans arrière-plan",
        data=download_image(output_image),
        file_name="image_sans_arrière_plan.png",
        mime="image/png",
    )

    return output_image

if my_upload is not None:
    if my_upload.size > max_size:
        st.sidebar.error("Ficher trop volumineux. Veuillez choisir un ficher de moins de 5MB")
    else:
        remove_bg(my_upload)
else:
    remove_bg("./Belle_Burger.jpg")