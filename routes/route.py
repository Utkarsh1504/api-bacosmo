from fastapi import APIRouter, Query, HTTPException, Path
from models.student import Student
from config.database import collection_name
from schema.schemas import student_list
from bson import ObjectId
from fastapi.responses import RedirectResponse, JSONResponse
from typing import Optional


router = APIRouter()

@router.get("/", include_in_schema=False)
async def home_redirect():
    return RedirectResponse(url='/docs')


# POST req method for creating new student
@router.post("/students")
async def create_student(student: Student):
  student_dict = dict(student)
  student_dict["address"] = student_dict['address'].dict()
  inserted_student = collection_name.insert_one(student_dict)
  if inserted_student:
    inserted_id = str(inserted_student.inserted_id)
    return JSONResponse(content={"id":inserted_id}, status_code=201)
  else:
    return JSONResponse(content="Failed to create student", status_code=500)
  

# GET req method for listing students
@router.get("/students")
async def list_students(
    country: Optional[str] = Query(None, description="To apply filter of country. If not given or empty, this filter should be applied."),
    age: Optional[int] = Query(None, description="Only records which have age greater than equal to the provided age should be present in the result. If not given or empty, this filter should be applied.")
):
    filters = {}
    if country:
        filters["address.country"] = country
    if age:
        filters["age"] = {"$gte": age}

    students = collection_name.find(filters)
    students_list = []
    for student in students:
        student["_id"] = str(student["_id"]) # Convert ObjectId to string
        students_list.append(student)

    if students_list: 
      return JSONResponse(content=students_list, status_code=200)
    else: 
      return JSONResponse(content="failed to list students", status_code=500)


# GET req method for individual student
@router.get("/students/{id}")
async def fetch_student(id: str=Path(..., description="The ID of the student previously created")):
  try: 
    student = collection_name.find_one({"_id": ObjectId(id)})
    if not student:
      raise HTTPException(status_code=404, detail="Student not found")
    
    student["id"] = str(student.pop("_id"))
    return student
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


# PATCH req method for updating student
@router.patch("/students/{id}")
async def update_student(id: str, student: Student):
  try:
    update_data = dict(student)
    if update_data:
      if "address" in update_data:
        update_data["address"] = update_data['address'].dict()
      result = collection_name.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.modified_count == 0:
      raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


# DELETE req method for deleting student
@router.delete("/students/{id}")
async def delete_student(id: str):
  try:
    result = collection_name.delete_one({"_id": ObjectId(id)})
    if result.deleted_count==0:
      raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
