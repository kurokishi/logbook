from sqlalchemy import text
from datetime import datetime

def log(engine, user, role, aksi, objek):
    engine.execute(text("""
    INSERT INTO audit_log (user,role,aksi,objek,timestamp)
    VALUES (:u,:r,:a,:o,:t)
    """), {
        "u": user,
        "r": role,
        "a": aksi,
        "o": objek,
        "t": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
