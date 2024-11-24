class Airplane:
    def __init__(self, airplane_type, max_passengers, current_passengers=0):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return False

    def __add__(self, other):
        new_count = self.current_passengers + other
        if new_count > self.max_passengers:
            raise ValueError("Počet cestujících překračuje maximální kapacitu.")
        return Airplane(self.airplane_type, self.max_passengers, new_count)

    def __sub__(self, other):
        new_count = self.current_passengers - other
        if new_count < 0:
            raise ValueError("Počet cestujících nemůže být záporný.")
        return Airplane(self.airplane_type, self.max_passengers, new_count)

    def __iadd__(self, other):
        new_count = self.current_passengers + other
        if new_count > self.max_passengers:
            raise ValueError("Počet cestujících překračuje maximální kapacitu.")
        self.current_passengers = new_count
        return self

    def __isub__(self, number):
        new_count = self.current_passengers - number
        if new_count < 0:
            raise ValueError("Počet cestujících nemůže být záporný.")
        self.current_passengers = new_count
        return self

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return False

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return False

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return False

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return False