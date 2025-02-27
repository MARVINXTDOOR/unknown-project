from fastapi import FastAPI

app= FastAPI()

# Sample betting odds
odds_data = {
    "NBA": [
        {"team": "Lakers", "odds": -110},
        {"team": "Warriors", "odds": +120}
    ],
    "NFL": [
        {"team": "Cowboys", "odds": -150},
        {"team": "Eagles", "odds": +130}
    ]
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Nuff Parlay API!"}
@app.get("/odds/{sport}")
def get_odds(sport: str):
    return odds_data.get(sport, {"message": "Sport not found"})
