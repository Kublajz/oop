class Airplane:
    def __init__(self, airplane_type, max_passengers, passengers=0):

        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.passengers = passengers

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type
    # Pro porovnávání letadel

    def __add__(self, other):
        new_passengers = self.passengers + passengers:
        if new_passengers > self.max_passengers:
            print("Nelze přidat pasažéry. Kapacita překročena.")
            return self
        return Airplane(self.airplane_type, self.max_passengers, new_passengers)

    def __sub__(self, passengers):

        new_passen
