import cv2
import streamlit as st
import PIL
import numpy as np

hide_streamlit_style = """
            <style>s
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title('theia 💡')
st.subheader('read better low-light documents 📄')
img = cv2.imread('page.jpg')
uploaded_img = st.file_uploader("Upload File", type=['png', 'jpg','jpeg'])
if uploaded_img is not None:
    file_bytes = np.asarray(bytearray(uploaded_img.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.resize(img,(720,940))
_,result = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY, 51,5)

col1,col2 = st.columns(2)
with col1:
    st.subheader("Original")
    st.image(img)
    
with col2:
    st.subheader("Current")
    st.image(adaptive)