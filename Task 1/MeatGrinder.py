from Device import Device


class MeatGrinder(Device):
    """
    Reprezentuje mlýnek na maso s dodatečnými atributy.

    Atributy:
        max_meat_capacity (float): Maximální kapacita masa v kg.
        number_of_blades (int): Počet čepelí.
    """
    def __init__(self, brand, model, power, price, max_meat_capacity, number_of_blades):
        """
        Inicializuje mlýnek na maso s danými parametry.

        Parametry:
            brand (str): Značka mlýnku.
            model (str): Model mlýnku.
            power (int): Spotřeba ve wattech.
            price (float): Cena mlýnku.
            max_meat_capacity (float): Maximální kapacita masa v kg.
            number_of_blades (int): Počet čepelí.
        """
        Device.__init__(self, brand, model, power, price)
        self.max_meat_capacity = max_meat_capacity
        self.number_of_blades = number_of_blades

    def device_work(self):
        """
        Mele maso.

        Návratová hodnota:
            str: Zpráva oznamující, že mlýnek mele maso.
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
            state = f"{self.brand} {self.model} mele maso."
        else:
            state = f"{self.brand} {self.model} nemele maso, mlýnek na maso je vypnutý."

        return state

    def __str__(self):
        return f"Mlýnek na maso: {self.brand} {self.model} ,výkon {self.power}, Maximální kapacita masa {self.max_meat_capacity} kg, Počet čepelí: {self.number_of_blades}, cena {self.price}"
