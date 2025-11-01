import streamlit as st 
from PIL import Image
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0d1117, #1f6feb);
    color: white;
    font-family: 'Helvetica', sans-serif;
}
</style>
""", unsafe_allow_html=True)
st.title ("Mi primera App")
st.header("En este espacio comienzo a desarrollar habilidades")
st.write("Puedo realizar back y front")
image=Image.open("foto.png")
st.image(image, caption="Interfaces multimodales")
texto=st.text_input("Escribe algo","este es mi texto")
st.write("El texto escrito es", texto)
