# app_pages/dashboard.py

import streamlit as st
from services.resource_service import count_resources
from services.booking_service import count_bookings
from services.contact_service import count_contacts


def render():
    user = st.session_state.get("user", {})
    name = user.get("name", "Student")
    matric = user.get("matric", "N/A")

    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    # -----------------------------
    # USER CARD
    # -----------------------------
    st.markdown(f"""
        <div style="
            padding:24px; 
            border-radius:16px;
            background:white;
            box-shadow:0 6px 20px rgba(0,0,0,0.05);
            margin-bottom:28px;
        ">
            <div style="font-size:28px; font-weight:700;">{name}</div>
            <div style="font-size:15px; color:#666; margin-top:3px;">Matric No: {matric}</div>
        </div>
    """, unsafe_allow_html=True)

    st.title("Dashboard")
    st.markdown("### Overview")

    # -----------------------------
    # REAL COUNTS
    # -----------------------------
    email = user.get("email", "")
    res_count = count_resources()
    book_count = count_bookings(email)
    contact_count = count_contacts()

    # -----------------------------
    # NAVIGATION FUNCTION
    # -----------------------------
    def go_to(page):
        st.query_params.update({"page": page})
        st.rerun()

    # -----------------------------
    # CARD STYLE
    # -----------------------------
    st.markdown("""
        <style>
            .dash-card {
                background: white;
                padding: 26px;
                border-radius: 16px;
                box-shadow: 0 4px 14px rgba(0,0,0,0.08);
                cursor: pointer;
                transition: 0.2s;
            }
            .dash-card:hover {
                transform: translateY(-4px);
                box-shadow: 0 8px 22px rgba(0,0,0,0.15);
            }
            .dash-title {
                font-size: 18px;
                font-weight: 600;
                margin-top: 6px;
                color: #333;
            }
            .dash-value {
                font-size: 30px;
                font-weight: 700;
                margin-top: 4px;
                color: #1a55ff;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # -----------------------------
    # CARD COMPONENT
    # -----------------------------
    def card(icon, title, value, page_name, col):
        with col:
            if st.container().button(
                f"{icon}  {title}\n\n{value}",
                key=f"btn_{page_name}",
                use_container_width=True
            ):
                go_to(page_name)

            st.markdown(f"""
                <style>
                    button[data-testid="baseButton-btn_{page_name}"] {{
                        background: white !important;
                        border-radius: 16px !important;
                        padding: 26px !important;
                        height: 160px !important;
                        text-align: left !important;
                        font-size: 18px !important;
                        white-space: pre-line !important;
                        box-shadow: 0 4px 14px rgba(0,0,0,0.08) !important;
                    }}
                    button[data-testid="baseButton-btn_{page_name}"]:hover {{
                        transform: translateY(-4px) !important;
                        box-shadow: 0 8px 22px rgba(0,0,0,0.15) !important;
                    }}
                </style>
            """, unsafe_allow_html=True)

    # -----------------------------
    # RENDER DASH CARDS
    # -----------------------------
    card("📘", "Resources", res_count, "Resources", col1)
    card("📅", "Bookings", book_count, "Booking", col2)
    card("📁", "Contacts", contact_count, "Contacts", col3)

    st.markdown("</div>", unsafe_allow_html=True)
