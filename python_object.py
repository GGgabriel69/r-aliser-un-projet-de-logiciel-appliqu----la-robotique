import json

class Voiture:
    def __init__(self,marque,roule,vitesse):
        self.marque = marque
        self.roule = roule
        self.vitesse = vitesse

    def __str__(self):
        return f"{self.marque}, {'yes' if self.roule else 'no'} , {self.vitesse}"

    def change_vitesse(self, nouvelle_vitesse):
        self.vitesse = nouvelle_vitesse       


auto1 = Voiture("BMW", True, 300)
auto2 = Voiture("Kia", False, 25)

print("marque:", auto1.marque)
print("roule?", auto1.roule)
print("vitesse:", auto1.vitesse," Km/h")

print(auto1)
print(auto2)

auto1.change_vitesse(40)
auto2.change_vitesse(2)

print("nouvelle vitesse :" ,auto1.vitesse, "Km/h")
print("nouvelle vitesse :" ,auto2.vitesse, "Km/h")

auto1Json = json.dumps(auto1.__dict__)
print(auto1Json)