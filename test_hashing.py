import bcrypt

# Prueba a generar un hash
password = "mi_contraseña"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashed)
