def approval_page(engine):
    allow("Supervisor", "Admin")

    df = pd.read_sql("""
        SELECT * FROM tiket WHERE status='OPEN'
    """, engine)

    for _, row in df.iterrows():
        with st.expander(f"Tiket #{row.id}"):
            st.write(row.keluhan)
            if st.button(f"Setujui #{row.id}"):
                engine.execute(text("""
                    UPDATE tiket SET
                    status='DISETUJUI',
                    approved_by=:u,
                    approved_at=datetime('now')
                    WHERE id=:id
                """), {
                    "u": st.session_state.user,
                    "id": row.id
                })
                log(engine, st.session_state.user,
                    st.session_state.role,
                    "APPROVE", f"Tiket {row.id}")
                st.success("Disetujui")
