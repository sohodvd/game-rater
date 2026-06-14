class Game:
    def __init__(self, name, rating, notes=""):
        self.name = name
        self.rating = float(rating)
        self.notes = notes
        
        
    def display(self):
        print(f"{self.name} - Rating: {self.rating}/10")
        if self.notes:
            print(f"Notes: {self.notes}")
        
        