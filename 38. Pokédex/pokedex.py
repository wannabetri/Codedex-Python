# Write code below 💖

class Pokemon:

    def __init__(self, entry, name, type, description, height, weight,  level, region, is_caught):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.height = height
        self.weight = weight
        self.level = level
        self.region = region
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ' made a sound!')

    def details(self):
        print('Entry: ' + str(self.entry))
        print('Name: ' + self.name)

        if len(self.type) == 1:
            print('Type: ' + self.type[0])
        else:
            print('Type: ' + self.type[0] + '/' + self.type[1])

        print('Lvl: ' + str(self.level))
        print('Region: ' + self.region)
        print('Description: ' + self.description)
        print('Height: ' + str(self.height))
        print('Weight: ' + str(self.weight))

        if self.is_caught:
            print(self.name + ' has already been caught!')
        else:
            print(self.name + ' hasn\'t been caught yet.')

eevee = Pokemon(133, "Eevee", ["Normal"], "Its ability to evolve into many forms allows it to adapt smoothly and perfectly to any environment.", 1.00, 14.3, 15, "Kanto", True)

mewtwo = Pokemon(150, "Mewtwo", ["Psychic"], "Its DNA is almost the same as Mew’s. However, its size and disposition are vastly different.", 6.07, 269.0, 70, "Kanto", False)

gholdengo = Pokemon(1000, "Gholdengo ", ["Steel", "Ghost"], "Its body seems to be made up of 1,000 coins. This Pokémon gets along well with others and is quick to make friends with anybody.", 3.11, 66.1, 57, "Paldea", False)

eevee.speak()
eevee.details()

mewtwo.speak()
mewtwo.details()

gholdengo.speak()
gholdengo.details()
