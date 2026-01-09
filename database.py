from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/sim_it_rsud.db", echo=False)

def init_db():
    with engine.begin() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            nama TEXT,
            password TEXT,
            role TEXT,
            aktif INTEGER
        )"""))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS tiket (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            jam TEXT,
            jenis_pekerjaan TEXT,
            perangkat TEXT,
            spesifikasi TEXT,
            ruang_unit TEXT,
            keluhan TEXT,
            tindakan TEXT,
            status TEXT,
            created_by TEXT,
            approved_by TEXT,
            approved_at TEXT,
            selesai_at TEXT
        )"""))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS bukti_dukung (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tiket_id INTEGER,
            file_name TEXT,
            file_path TEXT,
            hash_file TEXT,
            uploaded_by TEXT,
            uploaded_at TEXT
        )"""))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            role TEXT,
            aksi TEXT,
            objek TEXT,
            timestamp TEXT
        )"""))
