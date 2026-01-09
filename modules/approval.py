import streamlit as st
import pandas as pd
from sqlalchemy import text
from permissions import allow
from audit import log

def page(engine):
    allow("Supervisor","Admin")
    st.title("Approval Tiket")

    df = pd.read_sql(
        "SELECT * FROM tiket WHERE status='OPEN'",
        engine
    )

    for _, r in df.iterrows():
        with st.expander(f"Tiket #{r.id} - {r.ruang_unit}"):
            st.write(r.keluhan)

            cek = engine.execute(text("""
            SELECT COUNT(*) FROM bukti_dukung
            WHERE tiket_id=:id
            """), {"id": r.id}).scalar()

            st.write(f"Bukti dukung: {cek}")

            if cek < 1:
                st.warning("Belum ada bukti dukung")

            if st.button(f"Setujui #{r.id}") and cek >= 1:
                engine.execute(text("""
                UPDATE tiket SET
                status='DISETUJUI',
                approved_by=:u,
                approved_at=datetime('now')
                WHERE id=:id
                """), {
                    "u": st.session_state.user,
                    "id": r.id
                })
                log(engine, st.session_state.user,
                    st.session_state.role,
                    "APPROVE_TIKET",
                    f"Tiket {r.id}")
                st.success("Disetujui")
