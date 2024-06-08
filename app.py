from fastapi import FastAPI

app = FastAPI()
@app.get('/home')
def home():
    return{"data": "This is a home page"}

@app.get('/echo')
def echo(name: str, surname: str = ""):
    return {"data": f"Hello {name} {surname}!!"}

#Output URL: http://127.0.0.1:8000/echo?name=Nehal&surname=Joshi
#pip list: Gives List of modules in tabular format
#pip freeze: Gives List of modules
#pip freeze > requirements.txt: Copying the installed modules in the .txt file
#pip install -r .\requirements.txt: To install all the modules written in .txt file with versions in the current machine