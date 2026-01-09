import streamlit as st
import pandas as pd
from config import BOBOT_ANGKA_KREDIT
from modules.pdf_ekinerja import generate_pdf

def page(engine):
    df = pd.read_sql(
        "SELECT * FROM tiket WHERE status='DISETUJUI'",
        engine
    )

    data = []
    for _, r in df.iterrows():
        data.append({
            "tanggal": r.tanggal,
            "narasi": f"Melaksanakan {r.jenis_pekerjaan} di {r.ruang_unit}",
            "angka": BOBOT_ANGKA_KREDIT[r.jenis_pekerjaan]
        })

    st.dataframe(pd.DataFrame(data))

    if st.button("Generate PDF"):
        generate_pdf(
            "ekinerja.pdf",
            st.session_state.nama,
            "NIP",
            "Instalasi TI",
            data
        )
        st.download_button(
            "Download PDF",
            open("ekinerja.pdf","rb"),
            "ekinerja.pdf"
        )
