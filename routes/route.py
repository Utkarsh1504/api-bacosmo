from fastapi import APIRouter
from models.student import Student
from config.database import collection_name
from schema.schemas import student_list
from bson import ObjectId
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/", include_in_schema=False)
async def home_redirect():
    return RedirectResponse(url='/docs')


# POST req method for adding new student
@router.post("/students")
async def add_student(student: Student):
  student_dict = dict(student)
  student_dict["address"] = student_dict['address'].dict()
  inserted_student = collection_name.insert_one(student_dict)
  if inserted_student:
    return {"message": "Student added successfully"}
  else:
    return {"message": "Failed to add student"}
  

# GET req method for all students
@router.get("/students")
async def get_student():
  students = student_list(collection_name.find())
  return students

# GET req method for individual student
@router.get("/students/{id}")
async def get_student_by_id(id: str):
  student = collection_name.find_one({"_id": ObjectId(id)})
  if student:
    student["id"] = str(student.pop("_id"))
    return student
  else:
    return {"message": "Student not found"}


# PATCH req method for updating student
@router.patch("/students/{id}")
async def update_student(id: str, student: Student):
  student_dict = dict(student)
  student_dict["address"] = student_dict['address'].dict()
  collection_name.update_one({"_id": ObjectId(id)}, {"$set": student_dict})
  return {"message": "Student updated successfully"}

# DELETE req method for deleting student
@router.delete("/students/{id}")
async def delete_student(id: str):
  collection_name.delete_one({"_id": ObjectId(id)})
  return {"message": "Student deleted successfully"}
