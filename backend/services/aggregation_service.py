from sqlalchemy.orm import Session


def aggregate_summary(db: Session, start, end):
tickets_total = db.execute("SELECT count(*) FROM tickets WHERE created_at BETWEEN :s AND :e", {"s": start, "e": end}).scalar()
tickets_done = db.execute("SELECT count(*) FROM tickets WHERE status='DONE' AND created_at BETWEEN :s AND :e", {"s": start, "e": end}).scalar()


sla = round((tickets_done / tickets_total * 100), 2) if tickets_total else 0


return {
"tickets": {
"total": tickets_total,
"completed": tickets_done,
"sla_percentage": sla
}
}
