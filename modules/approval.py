import streamlit as st
from sqlalchemy import text
import datetime

def page(engine):
    st.header("Approval Atasan")

    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT * FROM tiket WHERE status='SELESAI'")
        ).fetchall()

    for r in rows:
        st.subheader(f"Tiket #{r.id}")
        st.write(r.keluhan)

        if st.button(f"Approve #{r.id}"):
            with engine.begin() as conn:
                conn.execute(text("""
                    UPDATE tiket SET
                    status='DISETUJUI',
                    approved_by=:u,
                    approved_at=:t
                    WHERE id=:i
                """), {
                    "u": st.session_state.user,
                    "t": datetime.datetime.now().isoformat(),
                    "i": r.id
                })
            st.success("Disetujui")
            st.rerun()
