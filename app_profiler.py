import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Do you have a Valentine's partner?")

# Collect basic information


# Display basic profile information


# --- USER INPUT SECTION ---
st.header("Enter Your Personal Details")

name = st.text_input("Full Name")
field = st.text_input("Field of Research")
institution = st.text_input("Institution")
email = st.text_input("Email Address")

# Display profile only when required fields are filled
if name and field and institution:
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    if email:
        st.write(f"**Email:** {email}")


# Add a section for publications
st.header("CV ENTRY")
uploaded_file = st.file_uploader("Upload your CV here", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends





# Add a contact section
st.header("Contact Information")
email = "ona.nyama20@gmail.com"
st.write(f"You can reach at {email}.")