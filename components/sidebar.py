# components/sidebar.py

import streamlit as st
from services import auth_service

def render(cookies=None):

    with st.sidebar:

        st.image("assets/images/logo.png", width=140)

        st.markdown("### Navigation")

        if st.button("Dashboard"):
            st.query_params.update({"page": "Dashboard"})
            st.rerun()

        if st.button("Resources"):
            st.query_params.update({"page": "Resources"})
            st.rerun()

        if st.button("Booking"):
            st.query_params.update({"page": "Booking"})
            st.rerun()

        if st.button("Contacts"):
            st.query_params.update({"page": "Contacts"})
            st.rerun()

        if st.button("Career Hub"):
            st.query_params.update({"page": "Career"})
            st.rerun()

        if st.button("Profile"):
            st.query_params.update({"page": "Profile"})
            st.rerun()

        st.markdown("---")

        # LOGOUT
        if st.button("Logout"):
            auth_service.logout_user()

            if cookies:
                cookies.delete("auth_email")
                cookies.save()

            st.rerun()
