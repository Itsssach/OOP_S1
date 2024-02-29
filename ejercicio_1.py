# First exercise ()
Juan_age= int(input("Ingrese la edad de Juan:")) # Allows the user to type Juan's age

Alberto_age= int(Juan_age*(2/3)) # Allows to calculate Alberto's age
Ana_age= int(Juan_age*(4/3)) # Allows to calculate Ana's age
Mom_age= int(Juan_age + Alberto_age + Ana_age) # To finally determine Mom's age

# The following lines allows the user to know the results that have been obtained

print(f"La edad de Juan es: {Juan_age}") 
print(f"La edad de Alberto es: {Alberto_age}")
print(f"La edad de Ana es: {Ana_age}")
print(f"La edad de la mamá es: {Mom_age}")
