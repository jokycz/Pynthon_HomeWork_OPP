from Device import Device


class CoffeeMachine(Device):
    """
    Reprezentuje kávovar s dodatečnými atributy.

    Atributy:
        water_tank_capacity (float): Kapacita nádrže na vodu v litrech.
        has_milk_frother (bool): Informace, zda kávovar má šlehač mléka.
    """
    def __init__(self, brand, model, power, price, water_tank_capacity, has_milk_frother):
        """
        Inicializuje kávovar s danými parametry.

        Parametry:
            brand (str): Značka kávovaru.
            model (str): Model kávovaru.
            power (int): Spotřeba ve wattech.
            price (float): Cena kávovaru.
            water_tank_capacity (float): Kapacita nádrže na vodu v litrech.
            has_milk_frother (bool): Zda má šlehač mléka.
        """
        Device.__init__(self, brand, model, power, price)
        self.water_tank_capacity = water_tank_capacity
        self.has_milk_frother = has_milk_frother

    def device_work(self):
        """
        Připraví kávu.

        Návratová hodnota:
            str: Zpráva oznamující, že kávovar připravuje kávu.
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
            state = f"{self.brand} {self.model} připravuje kávu."
        else:
            state = f"{self.brand} {self.model} nepřipravuje kávu kavovar je vypnutý."

        return state

    def __str__(self):
        return f"Kávovar: {self.brand} {self.model},výkon {self.power},{'má napěňovač mléka,' if self.has_milk_frother else ''} cena {self.price}"
