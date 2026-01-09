from database import engine
from auth import hash_pw
from sqlalchemy import text

with engine.begin() as conn:
    conn.execute(text("""
        DELETE FROM users WHERE username='admin'
    """))

    conn.execute(text("""
        INSERT INTO users
        (username, nama, password, role, aktif)
        VALUES
        (:u, :n, :p, :r, 1)
    """), {
        "u": "admin",
        "n": "Administrator",
        "p": hash_pw("admin123"),
        "r": "Admin"
    })

print("User admin berhasil dibuat ulang")
