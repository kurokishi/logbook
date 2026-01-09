import streamlit as st
import pandas as pd
from config import BOBOT_ANGKA_KREDIT
from modules.pdf_ekinerja import generate_pdf

def page(engine):
    st.title("e-Kinerja IT Support")

    df = pd.read_sql("""
    SELECT * FROM tiket WHERE status='SELESAI'
    """, engine)

    data = []
    for _, r in df.iterrows():
        narasi = f"""
Melaksanakan {r.jenis_pekerjaan.lower()} perangkat
{r.perangkat} di {r.ruang_unit} RSUD
berdasarkan laporan {r.keluhan.lower()}.
Kegiatan telah diselesaikan sesuai prosedur.
""".strip()

        data.append({
            "tanggal": r.tanggal,
            "narasi": narasi,
            "angka": BOBOT_ANGKA_KREDIT.get(r.jenis_pekerjaan, 0)
        })

    st.dataframe(pd.DataFrame(data), use_container_width=True)

    st.subheader("Cetak PDF e-Kinerja")

    nama = st.text_input("Nama Pegawai")
    nip = st.text_input("NIP")
    jabatan = st.text_input("Jabatan")
    unit = st.text_input("Unit Kerja")

    if st.button("📄 Generate PDF"):
        file = "ekinerja_it_rsud.pdf"
        generate_pdf(file, nama, nip, jabatan, unit, data)
        with open(file, "rb") as f:
            st.download_button(
                "⬇ Download PDF e-Kinerja",
                f,
                file_name=file,
                mime="application/pdf"
            )
