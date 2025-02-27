from fastapi import FastAPI

app= FastAPI()

# Updated betting odds
odds_data = {
    "NBA": [
        {"matchup": "GS Warriors vs ORL Magic", "moneyline": {"Warriors": -200, "Magic": +168}}
    ],
    "NCAAMB": [
        {"matchup": "Rutgers vs Michigan", "moneyline": {"Rutgers": +360, "Michigan": -480}}
    ]
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Nuff Parlay API!"}
@app.get("/odds/{sport}")
def get_odds(sport: str): # case-insensitive
    return odds_data.get(sport, {"message": "Sport not found"})
