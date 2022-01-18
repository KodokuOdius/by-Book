
from os import name


class Cat:
    name_class = "Nekos~ (/≧▽≦)/ (⓿_⓿)"

    def __init__(self, wool_color, eyes_color, name):
        self.wool_color = wool_color
        self.eyes_color = eyes_color
        self.name = name


    def nya(self):
        print("Nyaa-nyaa~~")

    def purr(self):
        print("Mrr-rrr~~")

    def hiss(self):
        print("Ha-shhhii-ii~~ !!!")
    
    def scrable(self):
        print("Scrabe-scrade~~ !!")


if __name__ == "__main__":
    Victorya = Cat(wool_color="Roayl White", eyes_color="Deep blue", name="Victotya")
    Victorya.nya()