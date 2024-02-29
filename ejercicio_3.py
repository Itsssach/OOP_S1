# Third exercise (12)
worked_hours= float(input("Inserte el número de horas trabajadas", )) # Allows the user to add the required information
wage= float(input("Inserte el valor de la hora:", )) # Allows to enter the required information
holding= float(input("Inserte el valor de retención a la fuente en números decimales, cuya separación sea un punto", ))

gross_salary= float(wage* worked_hours) # Value of gross salary
withholding= float(gross_salary* holding) # Value of withholding
net_salary= float(gross_salary- withholding) # Value of net salary

print(f"El valor del salario bruto es: {gross_salary}")
print(f"El valor de la retención a la fuente es: {withholding}")
print(f"El valor del salario neto es: {net_salary}")
