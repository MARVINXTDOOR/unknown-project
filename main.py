from fastapi import FastAPI
import os
import requests
import random

app = FastAPI()

# Replace 'your_api_key_here' with your actual API key or set it as an environment variable.
ODDS_API_KEY = os.getenv("ODDS_API_KEY", "53c0489779f5a6f1a1d6e46556979c1a")
# Base URL for The Odds API v4 (example using head-to-head odds)
ODDS_API_BASE_URL = "https://api.the-odds-api.com/v4/sports"

@app.get("/")
def read_root():
    return {"message": "Welcome to the Parlay API with The Odds API integration!"}

@app.get("/parlay/{sport}")
def suggest_parlay(sport: str):
    """
    This endpoint fetches live odds for the specified sport (e.g., 'basketball_nba') from The Odds API.
    It then selects two random events as a rough parlay suggestion.
    """
    # Build the API endpoint URL. Adjust the sport slug as needed.
    url = f"{ODDS_API_BASE_URL}/{sport}/odds/?apiKey={ODDS_API_KEY}&regions=us&markets=h2h"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"message": "Error fetching data from The Odds API", "status_code": response.status_code}
    
    events = response.json()
    
    if not events or len(events) < 2:
        return {"message": "Not enough events returned from The Odds API to build a parlay."}
    
    # Simple AI: Randomly pick two events for the parlay suggestion.
    parlay_events = random.sample(events, 2)
    
    return {"parlay_suggestion": parlay_events}
