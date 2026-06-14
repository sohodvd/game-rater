from game import Game
from save import save_games, save_profile, games, profile




def view_game(ask_edit=True):
    if not games:
        print("No games added yet.")
        return

    print("\nYour game list:")
    for index, game in enumerate(games, start=1):
        print(f"{index}. {game.name} - Rating: {game.rating}/10")

    if ask_edit:
        user_input = input("\n(e)dit a rating, (v)iew game details, (n)otes, (q)uit: ").strip().lower()

        if user_input == "q":
            print("Returning to main menu.")
            return

        if user_input == "n":
            choice_input = input("Enter the number of the game to add notes to (q to cancel): ").strip()

            if choice_input.lower() == "q":
                print("Returning to main menu.")
                return

            if choice_input.isdigit():
                choice = int(choice_input)
                if 1 <= choice <= len(games):
                    game = games[choice - 1]
                    if game.notes:
                        print(f"Current notes: {game.notes}")
                        edit_choice = input("Would you like to (e)dit or (d)elete notes? (q to cancel): ").strip().lower()
                        if edit_choice == "q":
                            print("Returning to main menu.")
                            return
                        elif edit_choice == "e":
                            new_notes = input("Enter new notes: ").strip()
                            games[choice - 1].notes = new_notes
                            save_games()
                            print("Notes updated.")
                        elif edit_choice == "d":
                            games[choice - 1].notes = ""
                            save_games()
                            print("Notes deleted.")
                    else:
                        new_notes = input("No notes yet. Enter notes: ").strip()
                        games[choice - 1].notes = new_notes
                        save_games()
                        print("Notes added.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid input. Please enter a number.")

        elif user_input == "v":
            choice_input = input("Enter the number of the game to view details (q to cancel): ").strip()

            if choice_input.lower() == "q":
                print("Returning to main menu.")
                return

            if choice_input.isdigit():
                choice = int(choice_input)
                if 1 <= choice <= len(games):
                    game = games[choice - 1]
                    print(f"\n{game.name}")
                    print(f"Rating: {game.rating}/10")
                    if game.notes:
                        print(f"Notes: {game.notes}")
                    else:
                        print("No notes added yet.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid input. Please enter a number.")

        elif user_input == "e":
            choice_input = input("Enter the number of the game to edit (q to cancel): ").strip()

            if choice_input.lower() == "q":
                print("Edit cancelled. Returning to main menu.")
                return

            if choice_input.isdigit():
                choice = int(choice_input)

                if 1 <= choice <= len(games):
                    new_rating = input(f"Enter new rating for {games[choice - 1].name} (q to cancel): ").strip()

                    if new_rating.lower() == "q":
                        print("Edit cancelled. Returning to main menu.")
                        return

                    try:
                        new_rating_value = float(new_rating)
                        if 1 <= new_rating_value <= 10:
                            games[choice - 1].rating = new_rating_value
                            save_games()
                            print(f"Updated {games[choice - 1].name} to rating {new_rating_value}/10")
                            edit_notes = input("Would you like to edit the notes? (y/n): ").strip().lower()
                            if edit_notes == "y":
                                new_notes = input("Enter new notes (press enter to clear): ").strip()
                                games[choice - 1].notes = new_notes
                                save_games()
                                print("Notes updated.")
                        else:
                            print("Please enter a number between 1 and 10.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("Invalid input. Please enter a number.")
                
                
                
                
                
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
