from fastapi import FastAPI
from routers import dashboard


app = FastAPI(title="RSUD Ticketing System")


app.include_router(dashboard.router, prefix="/api")
