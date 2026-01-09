import hashlib
import streamlit as st
from sqlalchemy import text

def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

def login(engine):
    st.title("Login SIM-IT RSUD")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        with engine.connect() as conn:
            user = conn.execute(
                text("""
                    SELECT username, password, role, aktif
                    FROM users
                    WHERE username = :u
                """),
                {"u": username}
            ).fetchone()

        if not user:
            st.error("User tidak ditemukan")
            return

        if user.aktif != 1:
            st.error("User tidak aktif")
            return

        if user.password != hash_pw(password):
            st.error("Password salah")
            return

        st.session_state.user = user.username
        st.session_state.role = user.role
        st.success("Login berhasil")
        st.rerun()
