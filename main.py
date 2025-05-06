import streamlit as st
from Visual import visual
from statis import statis
from About_Us import about_us

# Set layout
st.set_page_config(page_title="Diabetes Dashboard", layout="wide")

# Initialize session state
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Statistics"

# Define page functions
pages = {
    "Statistics": statis,
    "Visualisation": visual,
    "About Us": about_us
}

# Custom CSS to make buttons look like nav items
st.markdown("""
    <style>
    .nav-button {
        background-color: #2c3e50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, color 0.3s ease;
        width: 100%;
    }
    .nav-button:hover {
        background-color: #1abc9c;
        color: black;
    }
    .nav-button.active {
        background-color: #1abc9c;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Layout navigation bar horizontally using columns
col1, col2, col3 = st.columns(3)
nav_cols = [col1, col2, col3]

for i, (page_name, col) in enumerate(zip(pages.keys(), nav_cols)):
    button_class = "nav-button active" if st.session_state.selected_page == page_name else "nav-button"
    with col:
        if st.button(f"{page_name}", key=f"nav_{i}"):
            st.session_state.selected_page = page_name
        # Apply the custom style manually via JavaScript hack
        st.markdown(f"""
        <style>
        [data-testid="stButton"][key="nav_{i}"] button {{
            background-color: {'#1abc9c' if st.session_state.selected_page == page_name else '#2c3e50'};
            color: {'black' if st.session_state.selected_page == page_name else 'white'};
        }}
        </style>
        """, unsafe_allow_html=True)

# Render the selected page
pages[st.session_state.selected_page]()
