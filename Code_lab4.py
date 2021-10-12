from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str
    #discount: float 

@dataclass
class MoveOfMainAssets:
    code: int
    name: str
    goods: float
    profit: float
    cost: float




type_array = []
type_array.append(TypeOfMainAssets(1, "Універсам 22"))
type_array.append(TypeOfMainAssets(2, "Дніпрянка"))
type_array.append(TypeOfMainAssets(3, "Універсам 23"))
move_array = []
move_array.append(MoveOfMainAssets(1,"базовий", 79280.5, 1815.5, 7054.0))
move_array.append(MoveOfMainAssets(2, "базовий", 832714.5, 45810.5, 17868.0))
move_array.append(MoveOfMainAssets(1, "попередній", 486088.8, 32013.0, 37245.0))
move_array.append(MoveOfMainAssets(2, "попередній", 1665429.0, 91621.0, 35736.0))
move_array.append(MoveOfMainAssets(1, "поточний", 464588.0, 25584.0, 50913.0))
move_array.append(MoveOfMainAssets(2, "поточний", 2861819.0, 89378.0, 52783.0))
move_array.append(MoveOfMainAssets(3, "базовий", 79280.5, 1815.5, 7054.0))
move_array.append(MoveOfMainAssets(3, "попередній", 486088.8, 32013.0, 37245.0))
move_array.append(MoveOfMainAssets(3, "поточний", 464588.0, 25584.0, 50913.0))


def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Основні показники діяльності
підприємств"
    with names and values'''

    print ("Код підприємства: {code}, Період: {name}, Товарообіг грн.: {goods}, Балансовий прибуток грн.: {profit}, Середньорічна вартість основних засобів грн.: {cost}" .format(code=moveOfMainAssets.code, name=moveOfMainAssets.name, goods=moveOfMainAssets.goods,
                  profit=moveOfMainAssets.profit, cost=moveOfMainAssets.cost)) 
for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Довідник підприємств"
    with names and values'''

    print("Код підприємства: {code}, Назва підприємства: {name}"
        .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name))

for data in type_array:
    printTypeOfMainAssets(data)
input()