import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import time

img = Image.open("4321logo.png")

st.set_page_config(page_title="432 1 Music", page_icon=img)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

st.sidebar.header('Touch Designer Input Parameters')

def user_input_features():
    colorr = st.sidebar.slider('Red', 0.0, 1.0, 0.3)
    colorg = st.sidebar.slider('Green', 0.0, 1.0, 0.3)
    colorb = st.sidebar.slider('Blue', 0.0, 1.0, 0.3)
    amp = st.sidebar.slider('Amplitude', 0.2, 2.0, 0.5)
    data = {'colorr': colorr,
            'colorg': colorg,
            'colorb': colorb,
            'amp': amp}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

if "photo" not in st.session_state:
    st.session_state["photo"]="not done"
    
col1, col2, col3 = st.columns([1,2,1])

col1.markdown(" # 432 1 Music ")
col1.markdown(" #### Interactive App! ")

st.slider("Slider 1", 10, 100, 10, 1)
st.slider("Slider 2", 10, 100, 10, 1)
st.slider("Slider 3", 10, 100, 10, 1)
st.slider("Slider 4", 10, 100, 10, 1)

def change_photo_state():
    st.session_state["photo"]="done"
    
uploaded_photo = col2.file_uploader("Upload a photo", on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    progress_bar = col2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    col2.success("photo upload successfully")

    col3.metric(label="Temperature", value="60 C", delta="3 C")

    with st.expander("Click to read more"):
        st.write("Hello, here are more details on this topic if you interested in.")
        
        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)