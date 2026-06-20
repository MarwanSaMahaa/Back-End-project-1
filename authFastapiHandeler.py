import authCrud
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/user")
def create_user(username: str, email: str, password: str, role: int = 0):
    authCrud.create_user(username, email, password, role)
    return {"message": "User created successfully"}

@app.get("/users")
def read_all_users():
    return authCrud.get_all_users()

@app.get("/user")
def read_one_user(user_id: int):
    return authCrud.get_user(user_id)

@app.put("/user")
def update_user(user_id: int, username: str, email: str, password: str, role: int):
    authCrud.update_user(user_id, username, email, password, role)
    return {"message": "User updated successfully"}

@app.delete("/user")
def delete_user(user_id: int):
    authCrud.delete_user(user_id)
    return {"message": "User deleted successfully"}