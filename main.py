from fastapi import FastAPI
from pydantic import BaseModel
from utils import spell_check
# Initialize FastAPI
app = FastAPI()

class Input(BaseModel):
    text: str

@app.post("/spell_checker")
async def spell_checker(input: Input):
    text = spell_check(f"{input.text}")
    return {"corrected_spelling": text}