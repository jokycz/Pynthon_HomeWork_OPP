class Device:
    """
    Reprezentuje obecné zařízení s běžnými atributy a operacemi.

    Atributy:
        brand (str): Značka zařízení.
        model (str): Model zařízení.
        power (int): Spotřeba zařízení ve wattech.
        price (float): Cena zařízení v měně.
    """
    def __init__(self, brand, model, power, price):
        """
        Inicializuje zařízení s danou značkou, modelem, spotřebou a cenou.

        Parametry:
            brand (str): Značka zařízení.
            model (str): Model zařízení.
            power (int): Spotřeba ve wattech.
            price (float): Cena zařízení.
        """
        self.brand = brand
        self.model = model
        self.power = power
        self.price = price
        self._switch = False

    def turn_on(self):
        """
        Zapne zařízení.

        Návratová hodnota:
            str: Zpráva oznamující, že zařízení je zapnuté.
        """
        self._switch = True
        return f"{self.brand} {self.model} je nyní zapnuto."

    def turn_off(self):
        """
        Vypne zařízení.

        Návratová hodnota:
            str: Zpráva oznamující, že zařízení je vypnuté.
        """
        self._switch = False
        return f"{self.brand} {self.model} je nyní vypnuto."

    def device_work(self):
        """
        Vypne zařízení.

        Návratová hodnota:
            str: Zpráva oznamující, že zařízení je vypnuté.
        """
        return f"{self.brand} {self.model} je nevím jaký mam učel."

    @property
    def state(self):
        """
        Vrací textový stav zařízení (zapnuto/vypnuto).

        Návratová hodnota:
            str: Textový popis aktuálního stavu zařízení.
        """
        return f"Zařízení {self.brand} {self.model}, Stav: {'Zapnuto' if self._is_on else 'Vypnuto'}"

    def __str__(self):
        return self.state

