class Homan:
    """
    Human representation
    """
    def __init__(self, birthDate):
        self.birthDate = birthDate

    def printAge(self):
        print(2026 - self.birthDate)
    
fernanda = Homan(birthDate = 1995)
mauricio = Homan(birthDate = 1989)

fernanda.printAge()
mauricio.printAge()