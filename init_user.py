from database import engine
from auth import hash_pw
from sqlalchemy import text

with engine.begin() as conn:
    conn.execute(text("""
    INSERT OR IGNORE INTO users
    VALUES (NULL,'admin','Administrator',:p,'Admin',1)
    """), {"p": hash_pw("admin123")})

print("Admin siap")
