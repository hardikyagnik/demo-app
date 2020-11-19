import os
import streamlit as st
import pandas as pd
import numpy as np
import time


st.title("Tweet Analytics Dashboard")
# st.header(f"{os.environ['HOME']}")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.sidebar.title("Sidebar")
st.sidebar.header("Sidebar")
st.sidebar.subheader("Sidebar")
st.sidebar.text("Sidebar")

st.color_picker('Pick a color')
