import json
from game import Game


games = []
profile = None




def load_profile():   #load profiles
    global profile
    try:
        with open("profile.json", "r") as f:
            data = json.load(f)
            profile = data["name"]
    except FileNotFoundError:
        profile = None

def save_profile():   #save profiles
    with open("profile.json", "w") as f:
        json.dump({"name": profile}, f)


def load_games():   #load games
    global games
    try:
        with open("games.json", "r") as f:
            data = json.load(f)
            games = [Game(g["name"], g["rating"], g.get("notes", "")) for g in data]
        print("Game list loaded successfully.")
    except FileNotFoundError:
        print("No saved game list found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading saved game list. Starting fresh.")


def save_games():  #save games
    with open("games.json", "w") as f:
        json.dump([{"name": g.name, "rating": g.rating, "notes": g.notes} for g in games], f)
    print("Game list saved successfully.")