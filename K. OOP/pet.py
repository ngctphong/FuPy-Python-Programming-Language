class Pet:
    allowed = ['cat', 'dog', 'fish']

    def __init__(self, name, species):
        if species not in self.allowed:
            raise ValueError(f'You cant have a {species} pet')
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in self.allowed:
            raise ValueError(f'You cant have a {species} pet')
        self.species = species


cat = Pet('Blue', 'cat')
dog = Pet('Bum', 'dog')
cat.set_species('fish')
print(cat.species)
