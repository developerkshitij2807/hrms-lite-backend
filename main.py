from fastapi import FastAPI
from routes.employee_routes import router as employee_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for assignment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(employee_router)

@app.get("/")
def home():
    return {"message": "HRMS API running"}