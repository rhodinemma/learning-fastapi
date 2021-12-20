#import statements
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

#getting all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.farm.student.find())

#get a single student
@student_router.get('/students/{studentId}')
async def find_student(studentId):
    return studentEntity(connection.farm.student.find_one({"_id": ObjectId(studentId)}))

#creating a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.farm.student.insert_one(dict(student))
    return listOfStudentEntity(connection.farm.student.find())

#update a student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    #find a student and update with new data
    connection.farm.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.farm.student.find_one({"_id": ObjectId(studentId)}))

#delete a student
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    #finds a student, delete that student and also returns the same object
    return studentEntity(connection.farm.student.find_one_and_delete({"_id": ObjectId(studentId)}))