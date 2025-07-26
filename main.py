import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("Longitud de la contraseña:   "))
contra = ""

for i in range(long):
    contra += random.choice(characters)

print(f"Contraseña generada:  {contra}")
