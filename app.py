import streamlit as st
from database import engine, init_db
from auth import login
from permissions import allow
from modules import tiket, approval, ekinerja

st.set_page_config("SIM-IT RSUD", layout="wide")
init_db()

if "user" not in st.session_state:
    login(engine)
    st.stop()

menu = st.sidebar.radio("Menu",[
    "Input Tiket",
    "Approval",
    "e-Kinerja"
])

if menu=="Input Tiket":
    allow("IT Support","Admin")
    tiket.page(engine)

elif menu=="Approval":
    approval.page(engine)

elif menu=="e-Kinerja":
    ekinerja.page(engine)
