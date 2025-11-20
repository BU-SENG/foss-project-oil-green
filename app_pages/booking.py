import streamlit as st
from services.booking_service import (
    CAMPUS_LOCATIONS,
    create_booking,
    list_user_bookings
)

def render():
    st.title("Bookings")
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    user = st.session_state.get("user", {})
    email = user.get("email", "")

    st.subheader("Create a Booking")

    title = st.text_input("Booking Title")
    location = st.selectbox("Select Location", CAMPUS_LOCATIONS)
    date = st.date_input("Select Date")

    col1, col2 = st.columns(2)
    start_dt = col1.time_input("Start Time")
    end_dt = col2.time_input("End Time")

    if st.button("Submit Booking"):
        ok, msg = create_booking(
            title=title,
            location=location,
            user_email=email,
            date=date,
            start_dt=start_dt.strftime("%H:%M"),
            end_dt=end_dt.strftime("%H:%M")
        )

        if ok:
            st.success(msg)
            st.rerun()
        else:
            st.error(msg)

    st.markdown("---")
    st.subheader("My Bookings")

    bookings = list_user_bookings(email)

    if not bookings:
        st.info("You have no bookings yet.")
    else:
        for b in bookings:
            title, loc, dt, start, end, created = b

            st.markdown(f"""
                <div style="
                    padding:16px;
                    border-radius:10px;
                    background:white;
                    margin-bottom:10px;
                    box-shadow:0 2px 10px rgba(0,0,0,0.06);
                ">
                    <h4>{title}</h4>
                    <p><b>Location:</b> {loc}</p>
                    <p><b>Date:</b> {dt}</p>
                    <p><b>Time:</b> {start} - {end}</p>
                    <p style="font-size:12px; color:#aaa;">Booked at {created}</p>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
