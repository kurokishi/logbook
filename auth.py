import hashlib
import streamlit as st
from sqlalchemy import text

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def login(engine):
    st.title("Login SIM-IT RSUD")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        with engine.connect() as conn:
            q = conn.execute(
                text("SELECT * FROM users WHERE username=:u AND password=:p AND aktif=1"),
                {"u": u, "p": hash_pw(p)}
            ).fetchone()

        if q:
            st.session_state.user = q.username
            st.session_state.role = q.role
            st.success("Login berhasil")
            st.rerun()
        else:
            st.error("Login gagal")
