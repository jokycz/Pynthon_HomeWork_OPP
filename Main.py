from Blender import Blender
from CoffeeMachine import CoffeeMachine
from MeatGrinder import MeatGrinder

if __name__ == "__main__":
    coffee_machine = CoffeeMachine("DeLonghi", "EC685M", 1350, 200, 1.2, True)
    blender = Blender("Philips", "HR3652", 1400, 150, 2.0, 5)
    meat_grinder = MeatGrinder("Bosch", "MFW68660", 2200, 300, 4.5, 3)

    print(coffee_machine)
    coffee_machine.turn_on()
    print(coffee_machine.device_work())
    coffee_machine.turn_off()
    print()

    print(blender)
    print(blender.device_work())
    print()

    print(meat_grinder)
    print(meat_grinder.device_work())