#pip install fastapi
from fastapi import FastAPI,Request

app = FastAPI()

@app.get('/home')
def home():
    return("data": "This is the home page")   

@app.post('/login')
def login(username: str, password:str):
    else:
        return{"data":"Login failed incorrect username or password"}

@app.login('/login')
def login_post(request:Request):
    print(request.headers)
    print(request.body)
#running the application:
#in terminal : "fastapi dev app.py" ->detailed explanation
# or : "fastapi run app.py" -> less detailed explanation

@app.get('/echo')
def echo(name:str, surname:str):
    return("data":f"Hello {name} {surname}")
#in search tab enter "/echo?name=mel&surname=ferns"

'''
pip list : shows all packages and their versions
pip freeze : shows packages and their versions in == format

"pip freeeze > requirement.txt"

to install all modules in requirement.txt -> "pip install -r .\requirement.txt"
'''