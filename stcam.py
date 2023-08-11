import streamlit as st
import cv2
import numpy as np
from streamlit_back_camera_input import back_camera_input

if __name__ == '__main__':
    image = back_camera_input()
    if image:
        st.image(image)
