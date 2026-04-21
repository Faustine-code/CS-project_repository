import streamlit as st

st.markdown("""
<style>
div.stButton > button {
    padding: 0.75em 1.5em;
    font-size: 16px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

if "show_form" not in st.session_state:
    st.session_state.show_form = False

card_color = "#e8f5e9"  # set your color here

st.markdown(f"""
<div style="
    background-color: {card_color};
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ccc;
">
    <h3>Sales Manager</h3>
    <p><b>Company:</b> Loopol Corp</p>
    <p><b>Location:</b> Zurich, SUI</p>
    <p><b>Duration:</b> 3 months</p>
    <p><b>Tags:</b> Sales, Revenues</p>
    <p>
        Description: You will be responsible for driving revenue growth,
        managing client relationships, and developing sales strategies.
    </p>
</div>
""", unsafe_allow_html=True)

if "show_form" not in st.session_state:
    st.session_state.show_form = False

def toggle_form():
    st.session_state.show_form = not st.session_state.show_form


# 👇 spacing so button is not glued to card
st.markdown("<br>", unsafe_allow_html=True)

# 👇 centered + bigger button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.button("Apply Now", on_click=toggle_form, use_container_width=True)

if st.session_state.show_form:
    st.markdown("## Application Form")

    with st.form("application_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")

        cv = st.file_uploader("Upload your CV", type=["pdf", "docx"])

        submitted = st.form_submit_button("Submit Application")

        if submitted:
            st.success("Application submitted successfully!")

            # Optional: access uploaded file
            if cv is not None:
                st.write("Uploaded file:", cv.name)