import streamlit as st
from Visual import visual
from statis import statis
from About_Us import about_us

# Set page config
st.set_page_config(page_title="Data-Driven Diabetes Exploration", layout="wide")

# Define pages
pages = {
    "📊 Statistics": statis,
    "📈 Visualisation": visual,
    "ℹ️ About Us": about_us
}

# Apply custom style to make the radio button look like a navbar
st.markdown("""
    <style>
    div[data-baseweb="radio"] > div {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    label[data-testid="stRadioOption"] {
        background-color: #2c3e50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    label[data-testid="stRadioOption"]:hover {
        background-color: #1abc9c;
        color: black;
    }
    input[type="radio"]:checked + div {
        color: Green !important;
    }
    </style>
""", unsafe_allow_html=True)

# Render navbar using st.radio
selected = st.radio("Navigation", list(pages.keys()), horizontal=True, label_visibility="collapsed")

# Render selected page
pages[selected]()
