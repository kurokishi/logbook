import streamlit as st
import os, hashlib, datetime
from sqlalchemy import text

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def file_hash(file):
    return hashlib.sha256(file.getvalue()).hexdigest()

def page(engine):
    st.header("Input Logbook IT Support")

    with st.form("tiket"):
        jenis = st.selectbox("Jenis Pekerjaan", ["Hardware", "Software", "Jaringan", "SIMRS"])
        perangkat = st.text_input("Perangkat")
        ruang = st.text_input("Ruang / Unit")
        keluhan = st.text_area("Keluhan")
        tindakan = st.text_area("Tindakan")
        files = st.file_uploader("Bukti Dukung", accept_multiple_files=True)

        submit = st.form_submit_button("Simpan")

    if submit:
        now = datetime.datetime.now()
        with engine.begin() as conn:
            res = conn.execute(text("""
                INSERT INTO tiket VALUES
                (NULL,:tgl,:jam,:j,:p,:r,:k,:t,'SELESAI',:u,NULL,NULL,:s)
            """), {
                "tgl": now.date().isoformat(),
                "jam": now.time().strftime("%H:%M"),
                "j": jenis,
                "p": perangkat,
                "r": ruang,
                "k": keluhan,
                "t": tindakan,
                "u": st.session_state.user,
                "s": now.isoformat()
            })

            tiket_id = res.lastrowid

            for f in files:
                path = os.path.join(UPLOAD_DIR, f"{tiket_id}_{f.name}")
                with open(path, "wb") as out:
                    out.write(f.getbuffer())

                conn.execute(text("""
                    INSERT INTO bukti_dukung VALUES
                    (NULL,:id,:n,:p,:h,:u,:w)
                """), {
                    "id": tiket_id,
                    "n": f.name,
                    "p": path,
                    "h": file_hash(f),
                    "u": st.session_state.user,
                    "w": now.isoformat()
                })

        st.success("Tiket dan bukti tersimpan")
