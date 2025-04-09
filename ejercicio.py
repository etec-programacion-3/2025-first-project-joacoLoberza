def circlePerimeter (radius):
    perimeter = 2*3.1416*radius
    return perimeter
radius = float(input("Introduzca el radio del círculo:\n"))
perimeter = circlePerimeter(radius)
print("El perímetro del círculo es: ", perimeter)