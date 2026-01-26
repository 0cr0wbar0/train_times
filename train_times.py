from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
def first_menu() -> dict:
    return {"type": "menu", "question": "What station?", "choices": ["UK", "France", "Switzerland"]}

@app.get("/uk")
def uk_menu() -> dict:
    return {"type" : "input", "question" : "Departure station?"}

@app.get("/uk/{departure}")
def uk_dest() -> dict:
    return {"type": "menu", "question": "Arrival station?", "choices": ["Yes", "No"]}

@app.get("/uk/{departure}/yes")
def uk_dest_true() -> dict:
    return {"type" : "input", "question" : "Its name?"}

@app.get("/uk/{departure}/no")
def uk_dest_false(departure: str) -> dict:
    return {"type": "open", "url" : re.compile(r"\s+").sub("-", f"https://www.nationalrail.co.uk/live-trains/departures/{departure}")}

@app.get("/uk/{departure}/yes/{arrival}")
def uk_dep_and_arr(departure: str, arrival: str) -> dict:
    return {"type": "open", "url": re.compile(r"\s+").sub("-", f"https://www.nationalrail.co.uk/live-trains/departures/{departure}/{arrival}")}

@app.get("/france")
def fr_menu() -> dict:
    return {"type": "input", "question": "Departure station?"}

@app.get("/france/{departure}")
def fr_dest(departure: str) -> dict:
    return {"type": "open", "url" : re.compile(r"\s+").sub("-", f"https://www.garesetconnexions.sncf/en/stations-services/{departure}")}