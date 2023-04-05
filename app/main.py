import pandas as pd
import joblib
from pydantic import BaseModel, Field

# Pydantic Models
class Student(BaseModel):
    student_id: str = Field(alias="Student ID")
    gender: str = Field(alias="Gender")
    age: str = Field(alias="Age")
    major: str = Field(alias="Major")
    gpa: str = Field(alias="GPA")
    extra_curricular: str = Field(alias="Extra Curricular")
    num_programming_languages: str = Field(alias="Num Programming Languages")
    num_past_internships: str = Field(alias="Num Past Internships")

    class Config:
        allow_population_by_field_name = True

class PredictionResult(BaseModel):
    good_employee: int


# The Server APIs
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
async def predict_student(student: Student):
    clf = joblib.load('/code/app/model.pkl')
    student = student.dict(by_alias=True)
    query = pd.DataFrame(student, index=[0])
    try:
        prediction = clf.predict(query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to predict")
    return { 'good_employee': prediction[0].item() }