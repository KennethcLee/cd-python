class Ninja:
    def __init__(self, fname, lname, pet, tricks='None'):
        self.fname=fname
        self.lname=lname
        self.pet=Pet(fname, pet, tricks)

    def walk(self):
        print(f"{self.pet.name} walk and play.")
        self.pet.play()
        return self

    def feed(self, treats='None', petfood='None'):
        if (treats == 'None' and petfood == 'None'):
            print("Please offer treats or petfood.")
        else:
            print(f"{self.pet.name} feed and eat.")
            self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.pet.name} bathe and happy.")
        self.pet.noise()
        return self

class Pet:
    noisedict ={'bear':'growl', 'bee':'buzz', 'bird':'tweet', 'camel':'grunt', 'chick':'cheep', 'cow':'moo', 'dog':'bark', 'frog':'croak', 'pig':'oink', 'turkey':'gobble'}

    all_pets=[]

    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name=name
        self.pet=type
        self.tricks=tricks
        self.health=health
        self.energy=energy
        Pet.all_pets.append(self)

    def sleep(self):
        self.energy += 25
        self.displayStatus()
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        self.displayStatus()
        return self

    def play(self):
        self.energy += 5
        self.displayStatus()
        return self

    def noise(self):
        if self.pet in Pet.noisedict.keys():
            print(f"{self.pet.title()} is enjoying the activity, and making happy noise ", f"{Pet.noisedict[self.pet].title()}! " * 3)
            self.displayStatus()
        return self

    def displayStatus(self):
        print(f"Energy: {self.energy}, Health: {self.health}")
        return self

joe=Ninja("Joe", "Chang", "bear", "rollover")
joe.walk().feed(treats='banana').bathe()



