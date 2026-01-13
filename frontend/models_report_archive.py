from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func
from database import Base


class ReportArchive(Base):
__tablename__ = "report_archives"


id = Column(Integer, primary_key=True)
period_type = Column(String) # monthly | quarterly | semester
period_label = Column(String) # 2025-01 | TW-I 2025 | SEM-I 2025
start_date = Column(Date)
end_date = Column(Date)
total_tickets = Column(Integer)
on_time = Column(Integer)
late = Column(Integer)
sla_compliance = Column(Integer)
locked = Column(Boolean, default=True)
created_at = Column(DateTime, server_default=func.now())
