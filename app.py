import streamlit as st
from database import engine, init_db
from auth import login
from modules import tiket, approval, ekinerja
from permissions import allow

st.set_page_config("SIM-IT RSUD", layout="wide")
init_db()

if "user" not in st.session_state:
    login(engine)
    st.stop()

st.sidebar.success(f"{st.session_state.nama} ({st.session_state.role})")

menu = st.sidebar.radio("Menu", [
    "Input Tiket",
    "Approval",
    "e-Kinerja"
])

if menu == "Input Tiket":
    allow("IT Support", "Admin")
    tiket.page(engine)

elif menu == "Approval":
    approval.page(engine)

elif menu == "e-Kinerja":
    ekinerja.page(engine)
