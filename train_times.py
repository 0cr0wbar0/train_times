from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/")
def first_menu() -> dict:
    return {"type": "menu", "question": "What station?", "choices": ["UK", "France", "Switzerland"]}

@app.get("/{country}")
def country_menu() -> dict:
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

@app.get("/france/{departure}")
def fr_dest(departure: str) -> dict:
    return {"type": "open", "url" : re.compile(r"\s+").sub("-", f"https://www.garesetconnexions.sncf/en/stations-services/{departure}")}

@app.get("/switzerland/{departure}")
def ch_dest() -> dict:
    return {"type": "menu", "question": "Any stations along the way?", "choices": ["Yes", "No"]}

@app.get("/switzerland/{departure}/no")
def ch_dest_false() -> dict:
    return {"type": "input", "question": "Arrival station name?"}

@app.get("/switzerland/{departure}/no/{arrival}")
def ch_arr(departure: str, arrival: str) -> dict:
    return {"type" : "open", "url" : f"https://www.sbb.ch/en?stops={departure}~{arrival}"}

@app.get("/switzerland/{departure}/yes")
def ch_dest_true() -> dict:
    return {"type": "via_list"}

@app.get("/switzerland/{departure}/yes/{via_list}")
def ch_via_true() -> dict:
    return {"type": "input", "question": "Arrival station name?"}

@app.get("/switzerland/{departure}/yes/{via_list}/{arrival}")
def ch_via_true() -> dict:
    return {"type": "menu", "question": "Want to see ticket prices?", "choices": ["Yes", "No"]}

@app.get("/switzerland/{departure}/yes/{via_list}/{arrival}/yes")
def ch_prices_false(departure: str, via_list: str, arrival: str) -> dict:
    return {"type" : "open", "url" : f"https://www.sbb.ch/en?stops={departure}~{via_list}~{arrival}&via=1"}

@app.get("/switzerland/{departure}/yes/{via_list}/{arrival}/no")
def ch_prices_true(departure: str, via_list: str, arrival: str) -> dict:
    return {"type" : "open", "url" : f"https://www.sbb.ch/en?stops={departure}~{via_list}~{arrival}&via=1&noPrice=1"}