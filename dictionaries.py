# and sets

dev_ops_student = {
    "name" : "Cringe Katalyst",
    "stream" : "DevOps",
    "completed_lessons" : 3,
    "completed_lessons_names" : ["Variables", "Data Types", "Collections"]
}

print(dev_ops_student["completed_lessons_names"][1])

dev_ops_student["completed_lessons_names"].append("Operators")
dev_ops_student["completed_lessons"] = 4
dev_ops_student["completed_lessons_names"].pop(1)
# dev_ops_student["completed_lessons_names"].remove("Data Type") # Also works

car_parts = {"wheels", "windows", "doors"}
print(car_parts)