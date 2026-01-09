import streamlit as st
import pandas as pd
from config import BOBOT_ANGKA_KREDIT

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
"""
        angka = BOBOT_ANGKA_KREDIT.get(r.jenis_pekerjaan, 0)

        data.append({
            "Pegawai": r.created_by,
            "Narasi": narasi.strip(),
            "Angka Kredit": angka
        })

    st.dataframe(pd.DataFrame(data), use_container_width=True)
