import streamlit as st

color = st.color_picker("#87CEEB")

st.markdown(f"""
<div style="
    background-color: {color};
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ccc;
">
    <h3>Sales Manager</h3>
    <p><b>Location:</b> Zurich, SUI</p>
    <p><b>Duration:</b> 3 months</p>
    <p><b>Tags:</b> Sales, Revenues</p>
    <p>
        You will be responsible for driving revenue growth,
        managing client relationships, and developing sales strategies.
    </p>
</div>
""", unsafe_allow_html=True)