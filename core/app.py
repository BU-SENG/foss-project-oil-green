# core/app.py

import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from utils.session_state import init_session
from components import navbar, sidebar
from services import auth_service
from services.booking_service import init_booking_table
from services.resource_service import init_resource_table
from services.contact_service import init_contact_table

from app_pages import dashboard, resources, booking, contacts, careerhub, profile


def run_app():

    # ---------------------------------------------------------
    # 0) COOKIE MANAGER (Persistent Login)
    # ---------------------------------------------------------
    cookies = EncryptedCookieManager(
        prefix="campushub_",
        password="A_LONG_RANDOM_SECRET_KEY_123456789"
    )

    if not cookies.ready():
        st.stop()

    # ---------------------------------------------------------
    # 1) Initialize session + DB tables
    # ---------------------------------------------------------
    init_session()
    init_booking_table()
    init_resource_table()
    init_contact_table()

    # ---------------------------------------------------------
    # 2) Load CSS
    # ---------------------------------------------------------
    st.set_page_config(
        page_title="Campus Resource Hub",
        layout="wide"
    )

    try:
        with open("assets/css/style.css", "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        with open("assets/css/components.css", "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        st.warning("CSS files missing.")

    # ---------------------------------------------------------
    # 3) TRANSITION WRAPPER
    # ---------------------------------------------------------
    st.markdown("""
        <style>
            .page-container { animation: fadeSlide .45s ease; }
            @keyframes fadeSlide {
                from { opacity:0; transform: translateY(18px); }
                to { opacity:1; transform: translateY(0); }
            }
        </style>
        <div class="page-container">
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # 4) AUTO-LOGIN FROM COOKIE
    # ---------------------------------------------------------
    if not st.session_state["logged_in"]:
        stored_email = cookies.get("auth_email")
        if stored_email:
            user = auth_service.get_user_by_email(stored_email)
            if user:
                auth_service.login_user(user)

    # ---------------------------------------------------------
    # 5) IF NOT LOGGED IN → SHOW LOGIN/SIGNUP PAGE
    # ---------------------------------------------------------
    if not st.session_state["logged_in"]:

        # Hide sidebar
        st.markdown("""
            <style>[data-testid="stSidebar"] { display:none; }</style>
        """, unsafe_allow_html=True)

        mode = st.radio("Select option", ["Login", "Create Account"])
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

        # ---------------------
        # LOGIN
        # ---------------------
        if mode == "Login":
            st.title("Sign In")

            with st.form("login_form"):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                btn = st.form_submit_button("Login")

                if btn:
                    if not email.endswith("@student.babcock.edu.ng"):
                        st.error("Use your @student.babcock.edu.ng email.")
                    else:
                        user = auth_service.validate_credentials(email, password)

                        if user:
                            auth_service.login_user(user)
                            cookies["auth_email"] = user["email"]
                            cookies.save()
                            st.success("Login successful!")
                            st.rerun()
                        else:
                            st.error("Invalid email or password.")

        # ---------------------
        # SIGNUP
        # ---------------------
        else:
            st.title("Create Account")

            with st.form("signup_form"):
                st.subheader("Basic Information")
                name = st.text_input("Full Name")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                confirm = st.text_input("Confirm Password", type="password")

                st.subheader("Student Details")
                matric = st.text_input("Matric Number")
                program = st.text_input("Program")
                department = st.text_input("Department")
                phone = st.text_input("Phone Number")

                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                dob = st.date_input("Date of Birth")

                st.subheader("Hall")
                if gender == "Male":
                    hall = st.selectbox("Hall", ["Topaz", "Winslow", "Gideon Troopers", "Emerald", "Off-Campus"])
                elif gender == "Female":
                    hall = st.selectbox("Hall", ["Queen Esther", "Platinum", "White", "Sapphire", "Off-Campus"])
                else:
                    hall = st.selectbox("Hall", ["Off-Campus"])

                st.subheader("Guardian Info")
                guardian_name = st.text_input("Guardian Name")
                guardian_phone = st.text_input("Guardian Phone")

                avatar = st.file_uploader("Avatar (optional)", type=["png", "jpg", "jpeg"])

                btn = st.form_submit_button("Create Account")

                if btn:
                    if not email.endswith("@student.babcock.edu.ng"):
                        st.error("Use BU student email.")
                    elif password != confirm:
                        st.error("Passwords do not match.")
                    else:
                        ok, msg = auth_service.create_user(
                            name=name,
                            email=email,
                            password=password,
                            matric=matric,
                            program=program,
                            department=department,
                            phone=phone,
                            gender=gender,
                            dob=str(dob),
                            hall=hall,
                            guardian_name=guardian_name,
                            guardian_phone=guardian_phone,
                            avatar=avatar.getvalue() if avatar else None
                        )

                        if ok:
                            user = auth_service.validate_credentials(email, password)
                            auth_service.login_user(user)

                            cookies["auth_email"] = user["email"]
                            cookies.save()

                            st.success("Account created!")
                            st.rerun()
                        else:
                            st.error(msg)

        st.markdown("</div>", unsafe_allow_html=True)
        return

    # ---------------------------------------------------------
    # 6) SIDEBAR & NAVBAR
    # ---------------------------------------------------------
    sidebar.render(cookies)
    navbar.render("Campus Resource Hub")

    # ---------------------------------------------------------
    # 7) PAGE ROUTING
    # ---------------------------------------------------------
    page = st.query_params.get("page", "Dashboard")

    if page == "Dashboard":
        dashboard.render()
    elif page == "Resources":
        resources.render()
    elif page == "Booking":
        booking.render()
    elif page == "Contacts":
        contacts.render()
    elif page == "Career":
        careerhub.render()
    elif page == "Profile":
        profile.render()
    else:
        dashboard.render()

    st.markdown("</div>", unsafe_allow_html=True)
