import streamlit as st
import hashlib
from sqlalchemy import text

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def login(engine):
    st.sidebar.subheader("Login SIM-IT RSUD")
    u = st.sidebar.text_input("Username")
    p = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        q = text("""
        SELECT username,nama,role FROM users
        WHERE username=:u AND password=:p AND aktif=1
        """)
        r = engine.execute(q, {
            "u": u,
            "p": hash_pw(p)
        }).fetchone()

        if r:
            st.session_state.user = r[0]
            st.session_state.nama = r[1]
            st.session_state.role = r[2]
            st.success("Login berhasil")
        else:
            st.error("Login gagal")
