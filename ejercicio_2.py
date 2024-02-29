# Second exercise (5)
add_up= float(input("Inserta el primer valor de la operación", )) # Allows the user to add the first value
x= float(input("Inserta el segundo valor de la operación", )) # Allows the user to add the second value
y= float(input("Inserta el tercer valor de la operación")) # Allows te user to add the third value
add_up= add_up + x # Updating the first provided value (add_up)
x= x+ y**2 # Updating the first provided value (x)
add_up= add_up + (x/y) # Updating the variable (add_up)

print(f"El valor de la operación es: {add_up}")
