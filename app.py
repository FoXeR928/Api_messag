import fastapi

app = fastapi.FastAPI()

@app.post("/get_message", status_code=fastapi.status.HTTP_201_CREATED)
def get_message(user: str, user_to:str, ip: str, message: str):
    result=add_message(user, user_to, ip, message)
    return result

@app.post("/check_message", status_code=fastapi.status.HTTP_201_CREATED)
def check_message(user: str):
    result=add_status(user)
    return result