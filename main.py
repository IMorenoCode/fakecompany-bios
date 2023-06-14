import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("The Best Fake Company")
tile_content = """
This is a site that is a test for my python skills.  I could write alot more but this is not the right
thing.  Alina is arguing with Marilu about bugs and light.
"""
st.write(tile_content)

df = pandas.read_csv("data.csv")

col1, space1, col2, space2, col3 = st.columns([1, .5, 1, .5, 1])
with col1:
    for index, row in df[0:3].iterrows():
        st.header(f"{row['first name']}".title() + " " + f"{row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:7].iterrows():
        st.header(f"{row['first name']}".title() + " " + f"{row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:11].iterrows():
        st.header(f"{row['first name']}".title() + " " + f"{row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])