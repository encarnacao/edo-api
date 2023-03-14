from flask import Flask, jsonify, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
import subprocess

app = Flask(__name__)
spec=FlaskPydanticSpec('edo-api', title='EDO API', version='1.0.0')
spec.register(app)

class User(BaseModel):
    id: int
    name: str
    email: str


    
# Routes for testing the API
@app.post("/user")
@spec.validate(body=Request(User),resp=Response(HTTP_201=User,HTTP_401=None))
def create_user():
    """Create a new user"""
    body = request.json
    return jsonify(body["name"])

@app.get("/<int:number>")
def hello_number(number):
    return f"Hello, number {number}!"

@app.get("/")
def hello():
    command = "python ./scripts/hello_world.py"
    result = subprocess.check_output(command, shell=True)
    return result