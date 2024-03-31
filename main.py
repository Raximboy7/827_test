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

name = input('ismingiz nima?')
print(f'assalomu alekom {name}')
son1 = int(input('1-son'))
son2 = int(input('2-son'))
son3 = int(input('3-son'))
print(son1 + son2 + son3 )


name = input('ismingiz nima?')
print(f'assalomu alekom {name}')
son1 = int(input('1-son'))
son2 = int(input('2-son'))
son3 = int(input('3-son'))
son4 = int(input('4-son'))
print(son1 + son2 + son3 + son4 )


print('hello world')
print('sssssssssssssssssssssssssssssssssssssssssss')
