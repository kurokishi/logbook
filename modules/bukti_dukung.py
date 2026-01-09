import streamlit as st
import os, hashlib
from sqlalchemy import text
from datetime import datetime
from audit import log

UPLOAD_DIR = "uploads"

def page(engine, tiket_id):
    st.subheader("Upload Bukti Dukung")

    files = st.file_uploader(
        "Foto / Screenshot / PDF",
        type=["jpg","png","pdf"],
        accept_multiple_files=True
    )

    if st.button("Upload"):
        folder = f"{UPLOAD_DIR}/tiket_{tiket_id}"
        os.makedirs(folder, exist_ok=True)

        for f in files:
            path = os.path.join(folder, f.name)
            with open(path, "wb") as out:
                out.write(f.getbuffer())

            h = hashlib.sha256(f.getvalue()).hexdigest()

            engine.execute(text("""
            INSERT INTO bukti_dukung
            (tiket_id,file_name,file_path,
             hash_file,uploaded_by,uploaded_at)
            VALUES
            (:id,:fn,:fp,:h,:u,:t)
            """), {
                "id": tiket_id,
                "fn": f.name,
                "fp": path,
                "h": h,
                "u": st.session_state.user,
                "t": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

        log(engine, st.session_state.user,
            st.session_state.role,
            "UPLOAD_BUKTI",
            f"Tiket {tiket_id}")

        st.success("Bukti tersimpan")
