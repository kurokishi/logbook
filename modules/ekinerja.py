import streamlit as st
from sqlalchemy import text
import pandas as pd

def page(engine):
    st.header("Rekap e-Kinerja RSUD")

    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT * FROM tiket WHERE status='DISETUJUI'")
        ).fetchall()

    df = pd.DataFrame(rows)
    st.dataframe(df)
