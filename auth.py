import streamlit as st
from sqlalchemy import text
import hashlib

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def login(engine):
    st.sidebar.subheader("Login")
    user = st.sidebar.text_input("Username")
    pw = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        q = text("""
        SELECT username, role FROM users
        WHERE username=:u AND password_hash=:p AND aktif=1
        """)
        r = engine.execute(q, {
            "u": user,
            "p": hash_pw(pw)
        }).fetchone()

        if r:
            st.session_state.user = r[0]
            st.session_state.role = r[1]
            st.success("Login berhasil")
        else:
            st.error("Login gagal")
