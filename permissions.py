import streamlit as st

def allow(*roles):
    if "role" not in st.session_state:
        st.stop()
    if st.session_state.role not in roles:
        st.error("Akses ditolak")
        st.stop()
