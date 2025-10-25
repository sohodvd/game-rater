games = []

def add_game(game):
    games.append(game)
    print(f"Game added: {game[0]} with rating {game[1]}/10")

def view_game():
    if not games:
        print("No games added yet.")
    else:
        print("\nYour game list:")
        for index, (Game, Rating) in enumerate(games, start=1):
            print(f"{index}. {Game} - Rating: {Rating}/10")

def delete_game():
    view_game()
    if games:
        try:
            choice = int(input("Enter the number of the game to delete: "))
            if 1 <= choice <= len(games):
                removed = games.pop(choice - 1)
                print(f"Deleted game: {removed[0]}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main_menu():
    while True:
        print("\nGame List Menu:")
        print("1. Add Game")
        print("2. View Games")
        print("3. Delete a Game")
        print("4. Exit")
        choice = input("Pick an option (1-4): ")

        if choice == "1":
            Game = input("What is the name of the game you would like to add? ")
            Rating = input(f"What would you rate {Game} out of 10 stars? ")
            add_game((Game, Rating))
        elif choice == "2":
            view_game()
        elif choice == "3":
            delete_game()
        elif choice == "4":
            print("Exiting the game menu.")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()



