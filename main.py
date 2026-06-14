from game import Game
from save import load_games, load_profile, games, profile
from menus import view_game, delete_game, search_game, Feed_menu, Profile_menu


def main_menu():
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
            name = input("What is the name of the game you would like to add? (q to cancel) ").strip()
            if name.lower() == "q":
                continue
            rating = input(f"What would you rate {name} out of 10 stars? (q to cancel) ").strip()
            if rating.lower() == "q":
                continue
            notes = input(f"Add any thoughts on {name}? (press enter to skip): ").strip()
            games.append(Game(name, float(rating), notes))
            from save import save_games
            save_games()

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


main_menu()