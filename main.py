print('Hello world')
print('Salom')

#poloformizm
class Transpor:
    def __init__(self, brend, moduel):
        self.brend = brend
        self.moduel = moduel

    def __str__(self):
        return self.brend



    def get_info(self):
        return f"""
Brend: {self.brend}
Moduel: {self.moduel}"""

    def speed(self):
        pass

class Car(Transpor):
    def speed(self):
        return ('Speed: S/50')

class Bout(Transpor):
    def speed(self):
        return ('Speed: S/10')

class Airfliy(Transpor):
    def speed(self):
        return ('Speed: S/000')

car = Car('Matiz','Oddiy')
bout = Bout('Qayiq', '2 kishilik')
airl = Airfliy('Samaliyot', "O'yinchoq")

print(car.get_info())
print(car.speed())

print(bout.get_info())
print(bout.speed())

print(airl.get_info())
print(airl.speed())

