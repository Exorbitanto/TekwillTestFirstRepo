class Pet:

    def __init__(self,name:str, type:str, fav_food:str):
        self.name = name
        self.type = type
        self.fav_food = fav_food

    def __str__(self):
        return f"{self.type} called {self.name} that loves {self.fav_food}"

