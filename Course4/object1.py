class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print("So far:", self.x)

    def __del__(self):
        print("I am destructed:",  self.x)

a = PartyAnimal()
a.party()
a.party()
a = 42  # we define a as another object(class), PartyAnimal is destructed
print(a)