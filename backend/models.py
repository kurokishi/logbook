from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from database import Base
import enum
from datetime import datetime


class RoleEnum(str, enum.Enum):
ADMIN = "ADMIN"
KABAG = "KABAG"
DIREKTUR = "DIREKTUR"
USER = "USER"


class User(Base):
__tablename__ = "users"
id = Column(Integer, primary_key=True)
username = Column(String, unique=True)
password_hash = Column(String)
role = Column(Enum(RoleEnum))


class LockedPeriod(Base):
__tablename__ = "locked_periods"
id = Column(Integer, primary_key=True)
period_type = Column(String)
year = Column(Integer)
period_value = Column(Integer)
status = Column(String) # LOCKED
locked_at = Column(DateTime, default=datetime.utcnow)
