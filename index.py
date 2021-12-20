#import statements
from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

#our react frontend
client_app = ['http://localhost:3000']

#create app
app = FastAPI()

#register router
app.include_router(student_router)

#register app with CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = client_app,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)