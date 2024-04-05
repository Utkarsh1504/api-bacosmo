def individual_serial(student) -> dict:
  return {
    "id": str(student["_id"]),
    "name": student["name"],
    "age": student["age"],
    "address": {
      "city": student["address"]["city"],
      "country": student["address"]["country"]
    }
  }

def student_list(students) -> list:
  return [individual_serial(student) for student in students]
