from fastapi import FastAPI

app = FastAPI()


my_list = [
    {"name": "Alice", "score": 82},
    {"name": "Bob", "score": 91},
    {"name": "Carol", "score": 75}
]


@app.get("/users")
def get_users():
    return my_list


@app.get("/users/top")
def filter_users():
    result = [user for user in my_list if user["score"] > 80]
    result.sort(key=lambda x: x["score"], reverse=True)
    return [user["name"] for user in result]
