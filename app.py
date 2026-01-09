import os
import streamlit as st
from database import init_db, engine
from auth import login
from permissions import allow
from modules import tiket, approval, ekinerja

os.makedirs("uploads", exist_ok=True)

st.set_page_config("SIM-IT RSUD", layout="wide")

init_db()  # AUTO CREATE DB + ADMIN

if "user" not in st.session_state:
    login(engine)
    st.stop()

menu = st.sidebar.radio(
    "Menu",
    ["Input Logbook", "Approval", "e-Kinerja"]
)

if menu == "Input Logbook":
    allow("Admin", "IT Support")
    tiket.page(engine)

elif menu == "Approval":
    allow("Admin", "Atasan")
    approval.page(engine)

elif menu == "e-Kinerja":
    ekinerja.page(engine)
