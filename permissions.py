import streamlit as st

def allow(*roles):
    if st.session_state.role not in roles:
        st.error("Akses ditolak")
        st.stop()
