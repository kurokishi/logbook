import streamlit as st
from sqlalchemy import text
from audit import log

def page(engine):
    st.title("Input Tiket IT Support")

    with st.form("tiket"):
        tanggal = st.date_input("Tanggal")
        jam = st.time_input("Jam")
        jenis = st.selectbox("Jenis", [
            "Perbaikan Printer",
            "Troubleshooting Jaringan",
            "Perbaikan Komputer",
            "SIMRS / Aplikasi",
            "Scanner / Periferal"
        ])
        perangkat = st.text_input("Perangkat")
        spesifikasi = st.text_input("Spesifikasi")
        ruang = st.text_input("Ruang / Unit")
        keluhan = st.text_area("Keluhan")

        if st.form_submit_button("Simpan"):
            engine.execute(text("""
            INSERT INTO tiket
            (tanggal,jam,jenis_pekerjaan,perangkat,
             spesifikasi,ruang_unit,keluhan,
             status,created_by)
            VALUES
            (:t,:j,:jp,:p,:s,:r,:k,'OPEN',:u)
            """), {
                "t": str(tanggal),
                "j": str(jam),
                "jp": jenis,
                "p": perangkat,
                "s": spesifikasi,
                "r": ruang,
                "k": keluhan,
                "u": st.session_state.user
            })
            log(engine, st.session_state.user,
                st.session_state.role,
                "CREATE_TIKET", ruang)
            st.success("Tiket berhasil dibuat")
