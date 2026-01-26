from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
def first_menu():
    return {"type": "menu", "question": "What station?", "choices": ["UK", "France", "Switzerland"]}

@app.get("/uk")
def uk_menu():
    return {"type" : "input", "question" : "Departure station?"}

@app.get("/uk/{departure}")
def uk_dest():
    return {"type": "menu", "question": "Arrival station?", "choices": ["Yes", "No"]}

@app.get("/uk/{departure}/yes")
def uk_dest_true():
    return {"type" : "input", "question" : "Its name?"}

@app.get("/uk/{departure}/no")
def uk_dest_false(departure: str):
    return {"type": "open", "url" : re.compile(r"\s+").sub("-", f"https://www.nationalrail.co.uk/live-trains/departures/{departure}")}

@app.get("/uk/{departure}/yes/{arrival}")
def uk_dep_and_arr(departure: str, arrival: str):
    return {"type": "open", "url": re.compile(r"\s+").sub("-", f"https://www.nationalrail.co.uk/live-trains/departures/{departure}/{arrival}")}

# @app.get("/fr")
# def fr_menu():