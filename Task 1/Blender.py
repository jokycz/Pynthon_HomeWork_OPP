from Device import Device


class Blender(Device):
    """
    Reprezentuje mixér s dodatečnými atributy.

    Atributy:
        jar_capacity (float): Kapacita nádoby v litrech.
        speed_settings (int): Počet úrovní rychlosti.
    """
    def __init__(self, brand, model, power, price, jar_capacity, speed_settings):
        """
        Inicializuje mixér s danými parametry.

        Parametry:
            brand (str): Značka mixéru.
            model (str): Model mixéru.
            power (int): Spotřeba ve wattech.
            price (float): Cena mixéru.
            jar_capacity (float): Kapacita nádoby v litrech.
            speed_settings (int): Počet rychlostí.
        """
        Device.__init__(self, brand, model, power, price)
        self.jar_capacity = jar_capacity
        self.speed_settings = speed_settings

    def device_work(self):
        """
        Mixuje suroviny.

        Návratová hodnota:
            str: Zpráva oznamující, že mixér mixuje.
        """
        return self.state

    @property
    def state(self):
        """
        Vrací textový stav zařízení (zapnuto/vypnuto).

        Návratová hodnota:
            str: Textový popis aktuálního stavu zařízení.
        """
        if self._switch:
            state = f"{self.brand} {self.model} mixuje suroviny."
        else:
            state = f"{self.brand} {self.model}  nemixuje suroviny, mixer je vypnutý."

        return state

    def __str__(self):
        return f"Mixer: {self.brand} {self.model} ,výkon {self.power}, kapacita {self.jar_capacity} l, otázky: {self.speed_settings}, cena {self.price}"
