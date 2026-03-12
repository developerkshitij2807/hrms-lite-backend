from pymongo import MongoClient
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

client = AsyncIOMotorClient(MONGO_URI)

client = MongoClient(MONGO_URI)

db = client.hrms

employee_collection = db.employees
attendance_collection = db["attendance"]