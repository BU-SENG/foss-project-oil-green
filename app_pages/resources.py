import streamlit as st
from services.resource_service import (
    init_resource_table,
    upload_resource,
    list_resources,
    search_resources,
    filter_by_category
)


def render():

    # Ensure the SQLite table is created
    init_resource_table()

    st.title("Resources")
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)

    # -------------------------------------------------------
    # UPLOAD SECTION
    # -------------------------------------------------------
    st.subheader("Upload Resource")

    title = st.text_input("Title")
    description = st.text_area("Description")
    category = st.selectbox(
        "Category",
        ["Past Questions", "Notes", "Documents", "Misc"]
    )

    file = st.file_uploader(
        "Upload file",
        type=["pdf", "docx", "pptx", "txt"]
    )

    if st.button("Upload"):
        user_email = st.session_state["user"]["email"]
        ok, msg = upload_resource(title, description, category, file, user_email)

        if ok:
            st.success(msg)
            st.rerun()
        else:
            st.error(msg)

    st.markdown("---")

    # -------------------------------------------------------
    # SEARCH & FILTER
    # -------------------------------------------------------
    st.subheader("Available Resources")

    col1, col2 = st.columns([2, 1])

    with col1:
        search = st.text_input("Search", "")

    with col2:
        selected_category = st.selectbox(
            "Filter",
            ["All", "Past Questions", "Notes", "Documents", "Misc"]
        )

    # -------------------------------------------------------
    # FETCH DATA FROM DB
    # -------------------------------------------------------
    if search:
        resources = search_resources(search)
    elif selected_category != "All":
        resources = filter_by_category(selected_category)
    else:
        resources = list_resources()

    # -------------------------------------------------------
    # DISPLAY RESULTS
    # -------------------------------------------------------
    for r in resources:
        res_id, title, desc, cat, filename, uploader, timestamp = r

        st.markdown(f"""
            <div style="
                padding:18px;
                background:white;
                border-radius:10px;
                margin-bottom:14px;
                box-shadow:0 2px 10px rgba(0,0,0,0.06);
            ">
                <h4 style="margin:0;">{title}</h4>
                <p style="margin:4px 0;">{desc}</p>
                <p style="font-size:13px; color:#666;">Category: {cat}</p>
                <p style="font-size:12px; color:#999;">
                    Uploaded by: {uploader} | {timestamp}
                </p>
                <a href="assets/uploads/{filename}" download>📥 Download</a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
