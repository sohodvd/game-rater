# 🎮 Game Rater (Python CLI)

One of my Python projects where I log and rate games I've played

---

## 🧠 What It Does
- Add a game and give it a rating (1–10)
- List all rated games
- (Coming soon) Search for a game by title or platform
- (Coming soon) Calculate averages and basic stats

---

## 💾 Data Storage
All the games and ratings are saved locally in a **JSON file (`Game_rating_list.json`)**.  
That means I can close the app, reopen it later, and everything is still there — nothing gets lost.  

It uses Python’s built-in `json` module to:
- **Load** my saved data when the program starts  
- **Write** any new entries or changes back to the file automatically  

This keeps the app lightweight and offline — everything stays on my own computer.  


## 💡 Why I Made It
I’m learning Python and wanted to build something personal that mixes coding with gaming.  
This project helped me practice:
- Reading and writing files
- Functions and data structures
- Command-line interaction

---

## 🛠️ Built With
- Python 3
- VS Code
- Git & GitHub

---

## 🚀 How to Run
```bash
python main.py
