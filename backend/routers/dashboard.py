from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import LockedPeriod, User
from services.period_resolver import resolve_period
from services.aggregation_service import aggregate_summary
from auth import get_current_user


router = APIRouter()


@router.get("/dashboard/kabag")
def dashboard_kabag(period_type: str, year: int, period_value: int,
db: Session = Depends(get_db),
user: User = Depends(get_current_user)):
if user.role not in ["ADMIN", "KABAG"]:
raise HTTPException(403)


locked = db.query(LockedPeriod).filter_by(
period_type=period_type,
year=year,
period_value=period_value,
status="LOCKED"
).first()


if not locked:
raise HTTPException(400, "Periode belum dikunci")


start, end, label = resolve_period(period_type, year, period_value)
summary = aggregate_summary(db, start, end)


return {
"period": {"type": period_type, "label": label, "locked": True},
"summary": summary
}
