from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
username: str
password: str


class UserOut(BaseModel):
id: int
username: str
role: str


class TicketCreate(BaseModel):
title: str
description: str
priority: str
category_id: int


class TicketOut(BaseModel):
id: int
title: str
status: str
created_at: datetime


class DashboardResponse(BaseModel):
period: dict
summary: dict
