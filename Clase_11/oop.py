class Point2d:
    """
    A representation of a point in a 2d plane
    """
    # El punto está en el origen
    x = 0 
    y = 0
    
    # Función para mover el punto
    def movePoint(self, outterX, outterY):
        self.x += outterX
        self.y += outterY

    def printData(self):
        print(f"current point: ({self.x, self.y})")

# Creando una instancia de punto
point1 = Point2d()

print(f"point1 is:  ({point1.x}, {point1.y})")

point1.movePoint(outterX=3, outterY=-4)
print(f"point1 is:  ({point1.x}, {point1.y})")

point1.printData()