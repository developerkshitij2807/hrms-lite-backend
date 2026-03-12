from fastapi import FastAPI
from routes.employee_routes import router as employee_router

app = FastAPI()

app.include_router(employee_router)

@app.get("/")
def home():
    return {"message": "HRMS API running"}