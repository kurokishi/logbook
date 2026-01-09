import streamlit as st
import pandas as pd
from sqlalchemy import text

def page(engine):
    st.header("Rekap e-Kinerja RSUD")

    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT * FROM tiket WHERE status='DISETUJUI'")
        ).fetchall()

    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)
