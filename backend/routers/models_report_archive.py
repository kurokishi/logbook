from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models_report_archive import ReportArchive
from services.dashboard import get_kabag_dashboard_data, resolve_period_range


router = APIRouter(prefix="/reports", tags=["Reports"])


@router.post("/archive")
def archive_report(period: str, db: Session = Depends(get_db)):
period_range = resolve_period_range(period)
data = get_kabag_dashboard_data(period, db)


label = period_range['label']


exists = db.query(ReportArchive).filter(
ReportArchive.period_label == label
).first()
if exists:
raise HTTPException(400, "Periode sudah diarsipkan")


report = ReportArchive(
period_type=period,
period_label=label,
start_date=period_range['start'],
end_date=period_range['end'],
total_tickets=data['total_tickets'],
on_time=data['on_time'],
late=data['late'],
sla_compliance=data['sla_compliance'],
locked=True
)


db.add(report)
db.commit()
return {"message": "Laporan berhasil diarsipkan"}




@router.get("/archive")
def list_archives(db: Session = Depends(get_db)):
return db.query(ReportArchive).order_by(ReportArchive.created_at.desc()).all()
