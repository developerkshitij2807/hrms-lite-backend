from fastapi import APIRouter, HTTPException
from datetime import datetime
from models.attendance import Attendance
from database import attendance_collection

router = APIRouter()

# Mark attendance
@router.post("/attendance")
async def mark_attendance(attendance: Attendance):

    record = attendance.dict()

    await attendance_collection.insert_one(record)

    return {
        "message": "Attendance marked successfully"
    }


# Get all attendance
@router.get("/attendance")
async def get_attendance():

    records = []

    async for record in attendance_collection.find():
        record["_id"] = str(record["_id"])
        records.append(record)

    return records


# Get attendance by employee
@router.get("/attendance/{employee_id}")
async def get_employee_attendance(employee_id: str):

    records = []

    async for record in attendance_collection.find({"employee_id": employee_id}):
        record["_id"] = str(record["_id"])
        records.append(record)

    if not records:
        raise HTTPException(status_code=404, detail="No attendance found")

    return records