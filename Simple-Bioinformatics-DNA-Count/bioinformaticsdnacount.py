# Import Libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image = Image.open("nucleotide.jpg")

st.image(image, use_column_width=True)

st.write('''
# DNA Nucleotide Count Web App
This app couns the nucleotide composition of query DNA!
***''')

# Input Text Box

# st.sidebar.header("Enter DNA Sequence")
st.header("Enter DNA Sequence")
sequence_input = "Hi I am Meghal Agarwal. I am a Data Scientist"
sequence = st.text_area("Sequence Input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write('''
***
''')
# Print the input DNA Sequence
st.header("Input DNA Query")

## DNA Nucleotide Count
st.header("Output DNA Nucleotide Count")