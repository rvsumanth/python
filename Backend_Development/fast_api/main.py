'''
Learned How to Installed Fastapi
Learned How to import and create Intsance for fast api
Learned how to create routing and funtions

'''

from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def home():
    return {'Data':'Homepage'}

@app.get('/about')
def about():
    return {'Data':'About page'}

@app.get('/contactus')
def contact():
    return {'data':'contact us page'}