import streamlit as st
from sqlalchemy import text
import datetime

def page(engine):
    st.header("Approval Atasan")

    with engine.connect() as conn:
        data = conn.execute(
            text("SELECT * FROM tiket WHERE status='SELESAI'")
        ).fetchall()

    for d in data:
        st.subheader(f"Tiket #{d.id} - {d.jenis_pekerjaan}")
        st.write(d.keluhan)

        if st.button(f"Approve #{d.id}"):
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
                    "i": d.id
                })
            st.success("Disetujui")
            st.rerun()
