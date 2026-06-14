# one time migration script - converts old tuple format to Game object format
# run once then never again
import json

games = [
    ["Spider-Man", "8.5"], ["Spider-Man 2", "7.5"], ["Death Stranding 2", "9"],
    ["Elden Ring", "10"], ["Mario Odyssey", "10"], ["Cyberpunk 2077", "8"],
    ["Alan Wake 2", "9"], ["Ghost of Yotei", "9"], ["Ghost of Tsushima", "8.5"],
    ["Ratchet & Clank (PS2)", "8"], ["The Matrix Path of Neo", "6.5"],
    ["Control", "9.5"], ["Yakuza:Like a Dragon", "8"],
    ["Yakuza:Like a Dragon Infinte Wealth", "9"], ["Uncharted", "7.5"],
    ["Uncharted 2", "10"], ["Uncharted 3", "8.5"], ["Uncharted 4", "9"],
    ["Uncharted Lost Legacy", "9"], ["Resident Evil Requiem", 9.0]
]

converted = [{"name": g[0], "rating": float(g[1])} for g in games]

with open("games.json", "w") as f:
    json.dump(converted, f)

print("Migration complete!")