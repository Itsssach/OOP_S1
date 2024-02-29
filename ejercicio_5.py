# Fifth exercise (17)
import math # Required library
radius= float(input("Inserte el radio", )) # Allows the user to enter the radius

area_circle= math.pi* (radius**2) # Area cicle
circunference= 2*(math.pi)* radius # Circunference

print(f"El área del círculo es: {area_circle}")
print(f"El perímetro de la circunferencia es: {circunference}")
