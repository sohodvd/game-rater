import json  


class Game:
    def __init__(self, name, rating):
        self.name = name
        self.rating = float(rating)
        
    def display(self):
        print(f"{self.name} - Rating: {self.rating}/10")
        
        
        

profile = None


games = []



def get_non_empty_input(prompt):           #function to make sure input is not blank
    while True:
        user_input = input(prompt).strip()

        if user_input.lower()=="q":
            return None
        
        if user_input:
            return user_input
        print("Input cannot be empty. Try again.")





def get_valid_rating(prompt):      #function to make sure highest rating is 10
    while True:
        rating = input(prompt).strip()

        if rating.lower()== "q":
            return None
        
        try:
            rating_value = float(rating)
            if 1 <= rating_value <= 10:
                return rating_value
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a number between 1 and 10.")





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
            games = [Game(g["name"], g["rating"]) for g in data]
        print("Game list loaded successfully.")
    except FileNotFoundError:
        print("No saved game list found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading saved game list. Starting fresh.")


def save_games():  #save games
    with open("games.json", "w") as f:
        json.dump([{"name": g.name, "rating": g.rating} for g in games], f)
    print("Game list saved successfully.")
    

def add_game(game):  #add games
    games.append(game)
    save_games()
    print(f"Game added: {game.name} with rating {game.rating}/10")
    

def view_game(ask_edit=True):
    if not games:
        print("No games added yet.")
        return

    print("\nYour game list:")
    for index, game in enumerate(games, start=1):
        print(f"{index}. {game.name} - Rating: {game.rating}/10")
    
    if ask_edit:
        user_input = input("\nWould you like to edit a rating? (yes/no, q to cancel): ").strip().lower()

        if user_input == "q":
            print("Edit cancelled. Returning to main menu.")
            return

        if user_input == "yes":
            choice_input = input("Enter the number of the game to edit (press q to cancel): ").strip()

            if choice_input.lower() == "q":
                print("Edit cancelled. Returning to main menu.")
                return

            if choice_input.isdigit():
                choice = int(choice_input)

                if 1 <= choice <= len(games):
                    new_rating = input(f"Enter new rating for {games[choice - 1].name} (press q to cancel): ").strip()

                    if new_rating.lower() == "q":
                        print("Edit cancelled. Returning to main menu.")
                        return

                    try:
                        new_rating_value = float(new_rating)
                        if 1 <= new_rating_value <= 10:
                            games[choice - 1].rating = new_rating_value
                            save_games()
                            print(f"Updated {games[choice - 1].name} to rating {new_rating_value}/10")
                        else:
                            print("Please enter a number between 1 and 10.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("Invalid input. Please enter a number.")

        elif user_input == "no":
            return


def delete_game():
    view_game(ask_edit=False)
    if games:
        user_input = input("Enter the number of the game to delete (press q to cancel): ").strip()

        if user_input.lower() == "q":
            print("Delete cancelled. Returning to main menu.")
            return

        if user_input.isdigit():
            choice = int(user_input)

            if 1 <= choice <= len(games):
                removed = games.pop(choice - 1)
                save_games()
                print(f"Deleted game: {removed.name}")
            else:
                print("Invalid choice.")
        else:
            print("Invalid input. Please enter a number.")

def main_menu():   #main menu function
    load_games()
    load_profile()
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
            name = get_non_empty_input("What is the name of the game you would like to add? (q to cancel) ")

            if name is None:
                print("Add game cancelled. Returning to main menu.")
                continue
            rating = get_valid_rating(f"What would you rate {name} out of 10 stars? (q to cancel) ")

            if rating is None:
                print("Add game cancelled. Returning to main menu")
                continue

            add_game(Game(name, rating))

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
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Please try again.")


def search_game():   #search for games
    search_name = input("Enter game name to search:")
    search_found = [game for game in games if search_name.lower() in game.name.lower()]
    if search_found:
        print("Search results:")
        for game in search_found:
            print(f"{game.name} - Rating: {game.rating}/10")
    else:
        print(f"{search_name} not found.")


def Feed_menu():   #feed menu not working yet!!!
    print("Feeds coming soon...")

def Profile_menu():  #function for creating and viewing profile info
    global profile

    if profile is None:
        print("No profile found.")
        profile = input("Create your profile name: ")
        save_profile()
        print(f"Profile '{profile}' created.")
        return

    while True:
        print(f"\nHello 👋 {profile} ! ")
        print("\nProfile Menu:")
        print("1. View Profile")
        print("2. Edit Profile Name")
        print("3. Back to Main Menu")
        choice = input("Pick an option (1-3): ")

        if choice == "1":
            print(f"Profile Name: {profile}")
            view_game(ask_edit=False)
        elif choice == "2":
            profile = input("Enter new profile name: ")
            save_profile()
            print("Profile updated.")
        elif choice == "3":
            break
        else:
            print("Invalid option.")



    


    
main_menu()        





