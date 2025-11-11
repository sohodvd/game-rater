import json

games = []

def load_games():
    global games
    try:
        with open("games.json", "r") as f:
            games = json.load(f)  
        print("Game list loaded successfully.")
    except FileNotFoundError:
        print("No saved game list found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading saved game list. Starting fresh.")

def save_games():
    with open("games.json", "w") as f:
        json.dump(games, f) 
    print("Game list saved successfully.")


def add_game(game):
    games.append(game)
    save_games()
    print(f"Game added: {game[0]} with rating {game[1]}/10")

def view_game(ask_edit=True):
    if not games:
        print("No games added yet.")
        return  

    print("\nYour game list:")
    for index, (Game, Rating) in enumerate(games, start=1):
        print(f"{index}. {Game} - Rating: {Rating}/10")

    if ask_edit:
        user_input = input("\nWould you like to edit a rating? (yes/no): ").lower()
        if user_input == "yes":
            try:
                choice = int(input("Enter the number of the game to edit: "))
                if 1 <= choice <= len(games):
                    new_rating = input(f"Enter new rating for {games[choice - 1][0]}: ")
                    games[choice - 1] = (games[choice - 1][0], new_rating)
                    save_games()
                    print(f"Updated {games[choice - 1][0]} to rating {new_rating}/10")
                else:
                    print("Invalid choice. Returning to main menu.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif user_input == "no":
            return


def delete_game():
    view_game(ask_edit=False)
    if games:
        try:
            choice = int(input("Enter the number of the game to delete: "))
            if 1 <= choice <= len(games):
                removed = games.pop(choice - 1)
                save_games()
                print(f"Deleted game: {removed[0]}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    load_games()
    while True:
        print("\nGame List Menu:")
        print("1. Add Game")
        print("2. View Games")
        print("3. Delete a Game")
        print("4. Search for a Game")
        print("5. Feeds")
        print("6. Profile")
        print("7. Exit")
        choice = input("Pick an option (1-7): ")

        if choice == "1":
            Game = input("What is the name of the game you would like to add? ")
            Rating = input(f"What would you rate {Game} out of 10 stars? ")
            add_game((Game, Rating))
        elif choice == "2":
            view_game()
        elif choice == "3":
            delete_game()
        elif choice == "4":
            search_game()
        elif choice == "5":
            Feed_menu()
        elif choice == "6":
            Profile_menu()
        elif choice == "7":
            print("Exiting the game menu.")
            break
        else:
            print("Invalid option. Please try again.")


def search_game():
    search_name = input("Enter game name to search:")
    search_found = [game for game in games if search_name.lower() in game[0].lower()]
    if search_found:
        print("Search results:")
        for game in search_found:
            print(f"{game[0]} - Rating: {game[1]}/10")
    else:
        print(f"{search_name} not found.")


def Feed_menu():
    print("Feeds coming soon...")

def Profile_menu():
    ask_name = input("Enter the name of your profile:")
    print(f"Created Profile: {ask_name}")

    while True:
        print("\nProfile Menu:")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Back to Main Menu")
        choice = input("Pick an option (1-3): ")

        if choice == "1":
            print(f"Profile Name: {ask_name}")
            while True:
                Edit_ask_name = input("")
        elif choice == "2":
            ask_name = input("Enter new profile name:")
            print(f"Profile name updated to: {ask_name}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")




def view_profile():
    print("{\n ask_name}")
    


    
main_menu()





