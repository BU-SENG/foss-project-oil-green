import streamlit as st
from services.contact_service import get_all_contacts, filter_contacts


def render():
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.title("Contacts Directory")
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        query = st.text_input("Search by name, role, or department")
    with col2:
        department = st.selectbox("Filter by department", ["All", "Engineering", "Sciences", "Student Affairs", "Admissions", "Human Resources"])

    contacts = filter_contacts(query) if query else get_all_contacts()

    st.markdown("---")

    for c in contacts:
        st.markdown(f"""
        ### {c['name']}
        **{c['role']}**, {c['department']}  
        Phone: {c['phone']}  
        Email: {c['email']}
        """)
