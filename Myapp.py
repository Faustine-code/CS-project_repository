import streamlit as st

st.markdown("""
<style>
.custom-card {
    background-color: #87CEEB;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    st.subheader("Sales Manager")
    st.write("Location:", "Zurich, SUI")
    st.write("Duration:", "3 months")
    st.write("Tags:", "Sales, Revenues")
    
    st.markdown('</div>', unsafe_allow_html=True)