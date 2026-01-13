from fastapi import FastAPI
from routers import dashboard
from export import router as export_router


app = FastAPI(title="RSUD Ticketing System")


app.include_router(dashboard.router, prefix="/api")
app.include_router(export_router)
