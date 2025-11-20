# main.py
import streamlit as st
import sys, os

# Ensure the project root is added to the import path
sys.path.append(os.path.dirname(__file__))

# 🔥 Completely hide Streamlit's built-in multipage sidebar navigation
st.markdown("""
    <style>
        /* Hide Streamlit's default page navigation menu */
        section[data-testid="stSidebarNav"] {
            display: none !important;
        }
        div[data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Now import your application runner
from core.app import run_app

# Run your custom app (with custom sidebar & routing)
if __name__ == "__main__":
    run_app()
