import streamlit as st
from utils.constants import HALLS_BY_GENDER
from utils.validators import validate_email, validate_phone


def render():
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.title("Profile")
    st.markdown("</div>", unsafe_allow_html=True)

    user = st.session_state.get("user", {})

    with st.form("profile_form"):
        name = st.text_input("Full name", user.get("name", ""))
        email = st.text_input("Email", user.get("email", ""))
        phone = st.text_input("Phone", user.get("phone", ""))

        gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male","Female","Other"].index(user.get("gender","Male")))
        halls = HALLS_BY_GENDER.get(gender, []) + ["Off-Campus"]
        hall = st.selectbox("Hall", halls, index=halls.index(user.get("hall","Off-Campus")) if user.get("hall") in halls else 0)

        guardian = st.text_input("Guardian name", user.get("guardian_name", ""))
        guardian_phone = st.text_input("Guardian phone", user.get("guardian_phone", ""))

        avatar = st.file_uploader("Upload profile picture", type=["png","jpg","jpeg"])

        submit = st.form_submit_button("Save changes")

        if submit:
            if not validate_email(email):
                st.error("Invalid email.")
            elif not validate_phone(phone):
                st.error("Invalid phone.")
            else:
                user.update({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "gender": gender,
                    "hall": hall,
                    "guardian_name": guardian,
                    "guardian_phone": guardian_phone,
                })

                if avatar:
                    st.session_state["avatar_preview"] = avatar.read()

                st.session_state["user"] = user
                st.success("Profile updated.")
                st.rerun()

    if st.session_state.get("avatar_preview"):
        st.image(st.session_state["avatar_preview"], width=120)
